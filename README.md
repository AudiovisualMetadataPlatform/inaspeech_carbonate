# inaspeech_carbonate
INA Speech Segmenter for Carbonate

Odelay.

Run the INA Speech Segmenter singularity container on IU's carbonate system

It requires a couple of things:
1) the singularity container must be on carbonate
2) the SSH keypair agreement must be signed for IU's HPC and a keypair with
   passphrase must be created & installed

The syntax for the command is:
````
usage: inaspeech_carbonate.py [-h] [--debug] [--quiet] [--nocleanup]
                              [--email EMAIL] [--memory MEMORY]
                              config input output

Run the inaspeech singularity container on carbonate and retrieve the results

positional arguments:
  config           Configuration file
  input            input audio file
  output           INA Speech Segmenter output

optional arguments:
  -h, --help       show this help message and exit
  --debug          Turn on debugging
  --quiet          Turn off output
  --nocleanup      Don't clean up the remote directories
  --email EMAIL    Email address for status reports
  --memory MEMORY  Memory allocation request in GB

````

When this is run, a working directory is created for this particular instance and the input file copied to it.  A job file is created and submitted to the slurm queueing system that will start the singularity container with the right parameters AND create a finished file that has the return code of the container.   Then the program waits for the finished file to appear.  When it does, the files are copied from the remote system to the destinations specified on the command line.

