import random
from optparse import OptionParser
import subprocess
import os

cube_corners = {"x":[1,1,-1,-1,1,1,-1,-1], "y":[1,-1,-1,1,1,-1,-1,1], "z":[1,1,1,1,-1,-1,-1,-1]}



#take a random cube corner:
#  make one of x, y, or z = random(1,-1)+noise and then add noise to the others a


def gen_data(dataset, noise_factor, size, cube_size, dims):
  random.seed()
  for i in range(0,size):
    if i < cube_size:
      rand_xyz = random.randint(0,2)
      rand_corner = random.randint(0,7)
      rand_noise_x = random.uniform(-1,1) * noise_factor
      rand_noise_y = random.uniform(-1,1) * noise_factor
      rand_noise_z = random.uniform(-1,1) * noise_factor
    
      x = cube_corners["x"][rand_corner]
      y = cube_corners["y"][rand_corner]
      z = cube_corners["z"][rand_corner]

      if rand_xyz == 0:
        x = random.uniform(-1,1)
      elif rand_xyz == 1:
        y = random.uniform(-1,1)
      elif rand_xyz == 2:
        z = random.uniform(-1,1)
      else:
        print "ERROR MR ROBINSON ERROR"

      x += rand_noise_x
      y += rand_noise_y
      z += rand_noise_z

    else:
      x = random.uniform(-2,2)
      y = random.uniform(-2,2)
      z = random.uniform(-2,2)

    coords = [x,y,z]
    
    #cube coordinates complete, now noise coordinates
    for j in range(3,dims):
      coords.append(random.uniform(-2,2))
    

    
    dataset.append(coords)


def print_dataset(dataset, dims, path):
  #clear and create directory
  cmd = 'rm -rf {0}'.format(path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  cmd = 'mkdir -p {0}'.format(path)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

  print "Generating dataset in {0}".format(path)

  for i in range(0, dims):
    if i < 3:
      #print out pre-rotated cube
      with open(path + "/pre_cube_rot_dim{0}.txt".format(i+1), "w") as dim_file:
        for coord in dataset:
          dim_file.write("{0},".format(coord[i]))
        dim_file.write("1")
    else:
      #simply print out final noise data; no need to rotate with cube
      with open(path + "/dim{0}.txt".format(i+1), "w") as dim_file:
        for coord in dataset:
          dim_file.write("{0},".format(coord[i]))
        dim_file.write("1")
      

def rotateStartCube(path, data_dir_path, dims):
  cmd = "cd {0}; octave {1}/scripts/starting3DCubeRotation.m {2}".format(data_dir_path, path, dims)
  print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
  cmd = "rm {0}/pre_cube_rot_dim*".format(data_dir_path)
  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()


def print_viz(filename):
  cmd = 'octave viz.m "{0}"'.format(filename)
  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()



if __name__ =='__main__':

  usage = '''\tUse this script to generate N dimensions of comma-seperated floats.\n\tThe first three dimensions together form coordinates for a \n\t3D-rotated wire-frame cube while the rest of the dimensions are uniform random floats\n\tbetween -2 and 2'''
  parser = OptionParser(usage=usage)

  parser.add_option("-s", "--cubesize", type="int", dest="csize",
                     default=400, help="Specify how many data points should belong to the cube per dimension",
                     metavar="#CSIZE")
  parser.add_option("-t", "--tsize", type="int", dest="tsize",
                     default=500, help="Specify how many data points total per dimension. Number of background noise points = total points - data points in cube (-s option)",
                     metavar="#TNOISE")
  parser.add_option("-c", "--cubenoise", type="float", dest="cnoise",
                     default=.01, help="Cube noise factor. Determine how noisy the generated cube data should be. Default is .01, no noise is 0.",
                     metavar="#CNOISE")

  parser.add_option("-n", "--name", type="string", dest="setname",
                     default="test", help="Specify the name of the dataset. Data will be put in a $RSVP_DATA_HOME/dataset/<name>/ directory. CAUTION: ANYTHING ALREADY IN THIS DIRECTORY WILL BE DESTROYED",
                     metavar="#NAME")

  parser.add_option("-d", "--dimensions", type="int", dest="dims",
                     default="5", help="Specify how many dimensions of data to produce. The first three dimensions will form coordinates for the cube, the remaining dimensions will be uniform random noise between -2 and 2",
                     metavar="#DIMS")
  
  (options, args) = parser.parse_args()

  try:
    rsvp_data_home = os.environ['RSVP_DATA_HOME']
    data_dir_path = rsvp_data_home + "/datasets/" + options.setname + "/startSet/"
   
    dataset = []

    gen_data(dataset, options.cnoise, options.tsize, options.csize, options.dims)
    print_dataset(dataset, options.dims, data_dir_path)  
    rotateStartCube(rsvp_data_home, data_dir_path, options.dims)

  except KeyError:
    print "\t ERROR: You need to set the RSVP_DATA_HOME environment variable to the path to the home directory of this project.  It should look something like /home/ncarey/gitrepos/RSVP-Data"
