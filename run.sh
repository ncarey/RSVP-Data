#!/bin/bash

export RSVP_DATA_HOME=$(pwd)
#echo $RSVP_DATA_HOME

python ./scripts/genCubeAndNoise.py --cubesize 500 --tsize 500 --cubenoise 0 --name noCubeNoise5D --dimensions 5

python ./scripts/genSimulatedDataset.py --name noCubeNoise5D --dimensions 5

python ./scripts/genRandRotationDataset.py  --name noCubeNoise5D --rotations 1000 --dimensions 5
