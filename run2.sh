#!/bin/bash

export RSVP_DATA_HOME=$(pwd)
#echo $RSVP_DATA_HOME

python ./scripts/genCubeAndNoise.py --cubesize $1 --tsize $1 --cubenoise 0 --name paraTest --dimensions 6

python ./scripts/genSimulatedDataset.py --name paraTest --dimensions 6

python ./scripts/genRandRotationDataset.py  --name paraTest --rotations 100 --dimensions 6 --para $2
