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

# Set default parameters for neurons and create neuron populations (model: 'iaf_psc_delta')
# todo: nest.SetDefaults(???)
# todo: neurons_e = ???
# todo: neurons_i = ???

# Create poisson generator and set 'rate' to nu_ext
# todo: pgen = ???

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
# Connect the excitatory population to itself and to the inhibitory population using nest.Connect with 'fixed_indegree'. Calculate the indegree from 'NE' and 'epsilon'.

# Excitatory synapse specification
# todo: syn_exc = ???
# Connection specification
# todo: conn_exc = ???
# nest.Connect(???)
# nest.Connect(???)

# inhibitory connections
# Connect the inhibitory population to itself and to the excitatory population using nest.Connect with 'fixed_indegree'. Calculate the indegree from 'NI' and 'epsilon'.

# Inhibitory synapse specification
# todo: syn_inh = ???
# Connection specification
# todo: conn_inh = ???
# todo: nest.Connect(???)
# todo: nest.Connect(???)


# Connect poisson generator using the excitatory connection weight
# todo: nest.Connect(???)
# todo: nest.Connect(???)

# Connect spike detector
# todo: nest.Connect(???)
# todo: nest.Connect(???)

# Simulate

# todo: nest.Simulate(???)

###################################################################
# Analysis of network activity #
###################################################################

# Analyse mean firing rates 
# todo: uncomment the following code-lines

# events_ex = nest.GetStatus(spikes_e, 'n_events')[0]
# rate_ex = events_ex / simtime * 1000.0 / NE
# events_in = nest.GetStatus(spikes_i, 'n_events')[0]
# rate_in = events_in / simtime * 1000.0 / NI
# mean_rate = (rate_ex + rate_in) / 2.
# print 'mean firing rate: ', mean_rate

# Raster plot of spiking activity
# todo: uncomment the following code-lines

# nest.raster_plot.from_device(spikes_e)
# pl.show()

