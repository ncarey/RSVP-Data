RSVP-Data
=========

Datasets created for RSVP.  Uses python scripts for data generation and octave for visualization.

Requirements: 
  - octave
  - python
  - (optional) mplayer (to show a 'movie' of the generated .png images)

How to run:
  - Look at the ./run.sh script
  - make sure to set the RSVP_DATA_HOME environment variable as this directory.
    - look at the run.sh script
  - To play a movie similar to what RSVP will show the subject:
    - mplayer mf://*.png  -loop 0 -fps 4
  - To print a movie similar to above but to a file:
    - mencoder mf://*.png -mf type=png:w=512:h=512:fps=4 -ovc x264 -x264encopts preset=slow:tune=film:threads=auto:crf=18 -o 5Dhist.mov


Set of scripts used for creating image (.png) datasets for use on testing the RSVP Brain-Computer
Interface System.  RSVP monitors human brain P300 waves - we typically fire off a P300 wave when
we see something 'interesting.'  RSVP shows a person images in rapid succession and records when 
we emit a P300.  The hope is that we will emit a P300 wave when we see an interesting image.

These scripts generate images of x-y plots.  Most of these plots just show random noise, however
some of the plots show some structure.  We hope that the RSVP system will correctly classify the
dataset into noise images and structure images.

The dataset is generated as follows:
  - Start with N dimensions of data. This is the 'startSet' and is located in ./datasets/<datasetName>/startSet
    - Each dimension is a file of comma-seperated floats.
    - The first three dimensions together will form coordinates that make up a wire-frame cube.
      - This is the structure we are going to hide 
    - Each dimension after the first three will be uniform random noise.
    - The scripts 'genCubeAndNoise.py' and 'starting3DCubeRotation.m' generate the startSet
  - Apply a random N-dimensional rotation to the 'startSet' to create the Simulated Datset.
    - The simulated dataset will be located in ./datasets/<datasetName>/simulatedSet
    - The 3D cube structure should be hiddin by the N-dimensional rotation.
      - Visualizations of the simulated dataset should look like noise
      - This is the 'simulated dataset' because this set is what mimics a real-life dataset
        - In some datasets, low-dimensional structure is hidding in high-dimensional data
    - The scripts 'genSimulatedDataset.py' and 'simulatedDatasetRotation.m' create the simulated dataset
  - Apply many random N-dimensional rotations to the simulated set to attempt to find the cube structure
    - Randomly Rotated Dataset is located in ./datasets<datasetName>/randRotatedSet
    - This is the big dataset that will be used in RSVP. 
    - Most of the random rotations applied to the simulated dataset will produce more noise
    - Very few of the random rotations will get lucky and show some structure of the cube
      - These lucky rotations will have applied a close-to-opposite rotation applied to the startSet
      - Goal of RSVP is to find these images with some cubic structure
    - The scripts 'genRandRotationDataset.py' and 'randomRotationDataset.m' generate the randRotatedSet
   
    


