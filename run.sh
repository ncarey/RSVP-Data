#!/bin/bash

export RSVP_DATA_HOME=$(pwd)
#echo $RSVP_DATA_HOME

python ./scripts/genCubeAndNoise.py -s 500 -t 500 -c 0 -n noCubeNoise4D -d 4

