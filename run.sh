#!/bin/bash

export RSVP_DATA_HOME=$(pwd)
#echo $RSVP_DATA_HOME

python ./scripts/genCubeAndNoise.py --cubesize 1000 --tsize 1000 --cubenoise 0 --name noCubeNoise5D --dimensions 5 --spherenoise 0

python ./scripts/genSimulatedDataset.py --name noCubeNoise5D --dimensions 5

python ./scripts/genRandRotationDataset.py  --name noCubeNoise5D --rotations 100 --dimensions 5
