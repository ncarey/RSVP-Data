import random
from optparse import OptionParser
import subprocess
import os
import time

def rand_rotate_print_dataset(dims, rot_dir_path, sim_dir_path, path, rots, para):
  #clear and create directory
  cmd = 'rm -rf {0}'.format(rot_dir_path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  cmd = 'mkdir -p {0}'.format(rot_dir_path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  print "Generating random rotations of simulated dataset in {0}".format(rot_dir_path)

  rots_per_process = int(rots / para)
  cur_rot = 0
  procs = []
  for i in range(0,para):
    cmd = 'cd {0}; octave {1}/scripts/randomRotationDataset.m {2} {3} {4}'.format(rot_dir_path, path, dims, cur_rot, cur_rot + rots_per_process)
    print cmd
    procs.append(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
    cur_rot += rots_per_process

  for proc in procs:
    tmp = proc.poll()
    while(tmp == None):
      print "status {0}".format(tmp)
      time.sleep(5)

  for proc in procs:
    print proc.stdout.read()
  

  #invert the colors so there is black background with white dots
  for i in range(0, rots):
    cmd = "cd {0}; convert {1}.randrot.1-2.png -color-matrix '6x3: -1  0  0 0 0 1 0 -1 0 0 0 1 0 0 -1 0 0 1' {1}.randrot.1-2.png".format(rot_dir_path, i+1)

    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

if __name__ =='__main__':

  usage = '''\tUse this script to generate the random rotation dataset.\n\tThis is the dataset which we use with RSVP.\n\tBy applying random N dimensional rotations to the simulated dataset,\n\twe hope to find the structure represented in the startSet'''

  parser = OptionParser(usage=usage)

  parser.add_option("-p", "--parallel", type="int", dest="para",
                     default="2", help="Specify parallelism factor. Determines how many processes will be generating random rotations in parallel.",
                     metavar="#PARA")

  parser.add_option("-d", "--dimensions", type="int", dest="dims",
                     default="5", help="Specify how many dimensions are in the dataset. Should be the same number used for the genCubeAndNoise.py script",
                     metavar="#DIMS")
  parser.add_option("-n", "--name", type="string", dest="setname",
                     default="test", help="Specify the name of the dataset. Should be the same name used for the genCubeAndNoise.py script",
                     metavar="#NAME")

  parser.add_option("-r", "--rotations", type="int", dest="rots",
                     default="5", help="Specify how many random rotations to perform. This determins the size of the randomRotation dataset",
                     metavar="#ROTS")
  (options, args) = parser.parse_args()

  try:
    rsvp_data_home = os.environ['RSVP_DATA_HOME']
    sim_dir_path = rsvp_data_home + "/datasets/" + options.setname + "/simulatedSet/"
    rot_dir_path = rsvp_data_home + "/datasets/" + options.setname + "/randRotatedSet/"
    

    rand_rotate_print_dataset(options.dims, rot_dir_path, sim_dir_path, rsvp_data_home, options.rots, options.para)

  except KeyError:
    print "\t ERROR: You need to set the RSVP_DATA_HOME environment variable to the path to the home directory of this project.  It should look something like /home/ncarey/gitrepos/RSVP-Data"

