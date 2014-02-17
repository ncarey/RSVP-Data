import random
from optparse import OptionParser
import subprocess


cube_corners = {"x":[1,1,-1,-1,1,1,-1,-1], "y":[1,-1,-1,1,1,-1,-1,1], "z":[1,1,1,1,-1,-1,-1,-1]}

#take a random cube corner:
#  make one of x, y, or z = random(1,-1)+noise and then add noise to the others 

def add_cube(dataset, noise_factor, size):
  random.seed()
  for i in range(0,size):
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
    
    dataset.append([x,y,z])

def add_background(dataset, size):
  random.seed()
  for i in range(0,size):
    x = random.uniform(-2,2)
    y = random.uniform(-2,2)
    z = random.uniform(-2,2)

    dataset.append([x,y,z])


def print_dataset(dataset):
  with open("datapoints/x.txt", "w") as x_file, open("datapoints/y.txt","w") as y_file, open("datapoints/z.txt","w") as z_file:
    for coord in dataset:
      x_file.write("{0},".format(coord[0]))
      y_file.write("{0},".format(coord[1]))
      z_file.write("{0},".format(coord[2]))

  
    x_file.write("1")
    y_file.write("1")
    z_file.write("1")


def print_viz(filename):
  cmd = 'octave viz.m "{0}"'.format(filename)
  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()



if __name__ =='__main__':

  usage = "Usage: %prog [options]"
  parser = OptionParser(usage=usage)

  parser.add_option("-s", "--cubesize", type="int", dest="csize",
                     default=400, help="Specify how many data points in cube",
                     metavar="#CSIZE")
  parser.add_option("-t", "--tsize", type="int", dest="tsize",
                     default=500, help="Specifty how many data points total per image. Number of background noise datapoints = total points - data points in cube",
                     metavar="#TNOISE")
  parser.add_option("-c", "--cubenoise", type="float", dest="cnoise",
                     default=.01, help="Determine how noisy the generated cube data should be",
                     metavar="#CNOISE")

  parser.add_option("-f", "--fnprefix", type="string", dest="fnpre",
                     default="../data/images/default/default", help="Specify the path and filename prefix for the output images. Parameter example: /home/ncarey/data/test will produce a set of images in directory /home/ncarey/data/ with filenames test-XXX.cube.png",
                     metavar="#FNPRE")

  parser.add_option("-i", "--imagecount", type="int", dest="imgc",
                     default="5", help="Specify how many total images to produce",
                     metavar="#IMGC")
  parser.add_option("-k", "--cubeimgcount", type="int", dest="imgcc",
                     default="1", help="Specify how many images with cubes to produce",
                     metavar="#IMGCC")
  (options, args) = parser.parse_args()

  num_images = options.imgc
  num_cubes = options.imgcc

  for i in range(100, 100+num_images):
    dataset = []

    if (i-100) < num_cubes:
      add_cube(dataset, options.cnoise, options.csize)
      add_background(dataset, options.tsize - options.csize)
      viz_filename = options.fnpre + "-{0}.cube.png".format(i)
    else:
      add_background(dataset, options.tsize)
      viz_filename = options.fnpre + "-{0}.noise.png".format(i)
    
    print_dataset(dataset)
   # print_viz(viz_filename)



