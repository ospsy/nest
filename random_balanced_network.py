# global imports
import time
import pylab as pl

# import simulator
import nest

# import nest rasterplot
import nest.raster_plot

nest.ResetKernel()

startbuild = time.time()

###################################################################
# parameters #
###################################################################

# simulation parameters
simtime = 1000.            # simulation time (ms)
dt = 0.1                   # simulation resolution (ms)

# network parameters
NE = 1000                # number of excitatory neurons
gamma = 0.25             # relative number of inhibitory connections
NI = int(gamma * NE)     # number of inhibitory neurons
epsilon = 0.1            # connection probability (determines fixed indegree)

nu_ext = 15e3            # external poisson rate

# synapse paramters
w = 0.1                  # excitatory synaptic weight (mV)
g = 5.                   # relative inhibitory to excitatory synaptic weight
d = 1.5                  # synaptic transmission delay (ms)


# neuron paramters
neuron_params = {
    'C_m': 250.0,   # (pF)
    'E_L': 0.,      # (mV)
    'I_e': 0.0,     # (pA)
    'V_m': 0.,      # (mV)
    'V_reset': 0.,  # (mV)
    'V_th': 15.,    # (mV)
    't_ref': 2.0,   # (ms)
    'tau_m': 10.0,  # (ms)
}

###################################################################
# set up and run network #
###################################################################

# reset and configure kernel
nest.ResetKernel()
nest.SetKernelStatus({
    'resolution': dt,    # set simulation resolution
    'print_time': True   # enable printing of simulation progress
})

# create network nodes

# Set default parameters for neurons and create neurons (model:
nest.SetDefaults('iaf_psc_delta', neuron_params)
neurons_e = nest.Create('iaf_psc_delta', NE)
neurons_i = nest.Create('iaf_psc_delta', NI)


# Create poisson generator and set 'rate' to nu_ext
pgen = nest.Create('poisson_generator', params={'rate': nu_ext})

# Create spike detectors
spikes_e = nest.Create('spike_detector')
spikes_i = nest.Create('spike_detector')
nest.SetStatus(spikes_e, [{'withtime': True,
                           'withgid': True,
                           'to_file': False}])
nest.SetStatus(spikes_i, [{'withtime': True,
                           'withgid': True,
                           'to_file': False}])

# connect network

# excitatory connections
# Connect the excitatory population to itself and to the inhibitory
# population using nest.Connect with 'fixed_indegree'. Calculate the
# indegree from 'NE' and 'epsilon'.

# Synapse specification
syn_exc = {'delay': d, 'weight': w}
# Connection
conn_exc = {'rule': 'fixed_indegree', 'indegree': int(epsilon * NE)}
nest.Connect(neurons_e, neurons_e, conn_exc, syn_exc)
nest.Connect(neurons_e, neurons_i, conn_exc, syn_exc)


# inhibitory connections
# Connect the inhibitory population to itself and to the excitatory
# population using nest.Connect with 'fixed_indegree'. Calculate the
# indegree from 'NI' and 'epsilon'.

# Synapse specification
syn_inh = {'delay': d, 'weight': - g * w}
# Connection Specification
conn_inh = {'rule': 'fixed_indegree', 'indegree': int(epsilon * NI)}
nest.Connect(neurons_i, neurons_e, conn_inh, syn_inh)
nest.Connect(neurons_i, neurons_i, conn_inh, syn_inh)


# Connect poisson generator using the excitatory connection weight
nest.Connect(pgen, neurons_i, syn_spec=syn_exc)
nest.Connect(pgen, neurons_e, syn_spec=syn_exc)


# Connect spike detector
nest.Connect(neurons_e, spikes_e)
nest.Connect(neurons_i, spikes_i)

# Simulate

nest.Simulate(simtime)

###################################################################
# Analysis of network activity #
###################################################################

# Analyse mean firing rates
# todo: uncomment the following code-lines

events_ex = nest.GetStatus(spikes_e, 'n_events')[0]
rate_ex = events_ex / simtime * 1000.0 / NE
events_in = nest.GetStatus(spikes_i, 'n_events')[0]
rate_in = events_in / simtime * 1000.0 / NI
mean_rate = (rate_ex + rate_in) / 2.
print 'mean firing rate: ', rate_ex, rate_in

# Raster plot of spiking activity
# todo: uncomment the following code-lines

nest.raster_plot.from_device(spikes_e,hist=True)
pl.show()
