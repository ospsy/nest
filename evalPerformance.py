#!/bin/env python

#comments to come - perhaps

import nest
import time

clock=2.5
mul_add=2
n_cores=2
vector_length=4
theoretical_peak_GFLOPS=clock*mul_add*n_cores*vect
print "theoretical_peak GFLOPS", theoretical_peak_GFLOPS

n_neuron=1
simulation_time=100000
n_fpo_lms=5
dt=1.

nest.SetKernelStatus({"local_num_threads":1,"resolution":dt})
nest.Create("iaf_neuron",n_neuron)
start_time=time.time()
nest.Simulate(simulation_time)
computation_time=(time.time() - start_time)
print("---%s calculation time (sec) ---" %computation_time)

n_fpo_totoal=n_fpo_lms * simulation_time * n_neuron
print "number of flops: ", n_fpo_total

effective_GFLOPS = n_fpo_total / computation_time / (100**9)
print "effective GFLOPS:", effective_GFLOPS

efficiency=effective_GFLOPS / theoretical_peak_GFLOPS
print "efficiency", efficiency * 100., "%"
