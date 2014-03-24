import random
from optparse import OptionParser
import subprocess
import os


def rotate_print_dataset(dims, data_dir_path, sim_dir_path, path):
  #clear and create directory
  cmd = 'rm -rf {0}'.format(sim_dir_path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  cmd = 'mkdir -p {0}'.format(sim_dir_path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  print "Generating simulated dataset in {0}".format(sim_dir_path)


  cmd = 'cd {0}; octave {1}/scripts/simulatedDatasetRotation.m {2}'.format(sim_dir_path, path, dims)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()



if __name__ =='__main__':

  usage = '''\tUse this script to generate the simulated dataset.\n\tThis is the dataset where we hide the 3D cube in N dimensions by applying\n\tan N dimensional random rotation to all N dimensions\n'''
  parser = OptionParser(usage=usage)

  parser.add_option("-d", "--dimensions", type="int", dest="dims",
                     default="5", help="Specify how many dimensions are in the dataset. Should be the same number used for the genCubeAndNoise.py script",
                     metavar="#DIMS")
  parser.add_option("-n", "--name", type="string", dest="setname",
                     default="test", help="Specify the name of the dataset. Should be the same name used for the genCubeAndNoise.py script",
                     metavar="#NAME")

  (options, args) = parser.parse_args()

  try:
    rsvp_data_home = os.environ['RSVP_DATA_HOME']
    data_dir_path = rsvp_data_home + "/datasets/" + options.setname + "/startSet/"
    sim_dir_path = rsvp_data_home + "/datasets/" + options.setname + "/simulatedSet/"
   

    rotate_print_dataset(options.dims, data_dir_path, sim_dir_path, rsvp_data_home)

  except KeyError:
    print "\t ERROR: You need to set the RSVP_DATA_HOME environment variable to the path to the home directory of this project.  It should look something like /home/ncarey/gitrepos/RSVP-Data"

