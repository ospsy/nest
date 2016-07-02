import pylab as pl  # import pylab (for plotting)
import nest         # import NEST module
nest.ResetKernel()  # reset simulation kernel 
# create leaky IaF neuron with delta-shaped synaptic currents
neuron = nest.Create('iaf_psc_delta') 
# create a spike generator
spikegenerator = nest.Create('spike_generator')
# ... and let it spike at 10 and 50 ms
nest.SetStatus(spikegenerator, {'spike_times': [10., 50.]})
# create a voltmeter
voltmeter = nest.Create('voltmeter')
# connect spike generator and voltmeter to the neuron
nest.Connect(spikegenerator, neuron)
nest.Connect(voltmeter, neuron)
# run simulation for 100ms
nest.Simulate(100.) 
# read out recording time and voltage from voltmeter
times = nest.GetStatus(voltmeter)[0]['events']['times']
voltage = nest.GetStatus(voltmeter)[0]['events']['V_m']
# plot results
pl.plot(times, voltage)
pl.xlabel('time (ms)'); pl.ylabel('membrane potential (mV)')
pl.show() 
