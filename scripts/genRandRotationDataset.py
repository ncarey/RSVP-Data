import random
from optparse import OptionParser
import subprocess
import os
import time
import multiprocessing

def work(cmd):
  #return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  FNULL = open(os.devnull, 'w')
  return subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)
  #return subprocess.call(cmd, shell=True)


def rand_rotate_print_dataset(dims, rot_dir_path, sim_dir_path, path, rots, para):
  #clear and create directory
  FNULL = open(os.devnull, 'w')
  cmd = 'rm -rf {0}'.format(rot_dir_path)
  subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)

  cmd = 'mkdir -p {0}/hist'.format(rot_dir_path)
  subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)
  cmd = 'mkdir -p {0}/scatter'.format(rot_dir_path)
  subprocess.call(cmd, shell=True, stdout=FNULL, stderr=FNULL)

  print "Generating random rotations of simulated dataset in {0}".format(rot_dir_path)
  print time.time()

  rots_per_process = int(rots / para)
  cur_rot = 0
  procs = []
  cmd = 'cd {0}; octave {1}/scripts/randomRotationDataset.m {2} {3} {4}'.format(rot_dir_path, path, dims, cur_rot, cur_rot + rots_per_process)
 
  pool = multiprocessing.Pool(processes=para)
  pool.map(work, [cmd] * para)
  pool.close()
  pool.join()
  print "Finished generating random rotations. inverting color scheme now"
  print time.time()
#  for i in range(0,para):
#    cmd = 'cd {0}; octave {1}/scripts/randomRotationDataset.m {2} {3} {4}'.format(rot_dir_path, path, dims, cur_rot, cur_rot + rots_per_process)
#    print cmd
#    procs.append(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
#    cur_rot += rots_per_process


#  for proc in procs:
#    tmp = proc.poll()
#    while(tmp == None):
#      print "status {0}".format(tmp)
#  time.sleep(10)

#  time.sleep(10)
#  for proc in procs:
#    proc.stdout.read()
#    print "subprocess finished..."

  #invert the colors so there is black background with white dots
  cmd = "cd {0}/scatter; ls".format(rot_dir_path)
  files = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().split()
  
  for mfile in files:
    #cmd = "cd {0}/scatter; convert {1}.randrot.1-2.png -color-matrix '6x3: -1  0  0 0 0 1 0 -1 0 0 0 1 0 0 -1 0 0 1' {1}.randrot.1-2.png".format(rot_dir_path, i+1)
    cmd = "cd {0}/scatter; convert {1} -color-matrix '6x3: -1  0  0 0 0 1 0 -1 0 0 0 1 0 0 -1 0 0 1' {1}".format(rot_dir_path, mfile)

    subprocess.call(cmd, shell=True)

  print "Complete"
  print time.time()
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

