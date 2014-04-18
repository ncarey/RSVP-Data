#!/bin/bash

export RSVP_DATA_HOME=$(pwd)
#echo $RSVP_DATA_HOME

python ./scripts/genCubeAndNoise.py --cubesize 1500 --tsize 1500 --cubenoise 0 --name 2sphere5D --dimensions 5

python ./scripts/genSimulatedDataset.py --name 2sphere5D --dimensions 5

python ./scripts/genRandRotationDataset.py  --name 2sphere5D --rotations 1500 --dimensions 5
