import random
from optparse import OptionParser


cube_corners = {"x":[1,1,-1,-1,1,1,-1,-1], "y":[1,-1,-1,1,1,-1,-1,1], "z":[1,1,1,1,-1,-1,-1,-1]}

#take a point from the cube corners:
#  make one element random(1,-1)+noise and add noise to the other two elements

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
  with open("/home/ncarey/gitrepos/RSVP-Data/data/testx.txt", "w") as x_file, open("/home/ncarey/gitrepos/RSVP-Data/data/testy.txt","w") as y_file, open("/home/ncarey/gitrepos/RSVP-Data/data/testz.txt","w") as z_file:
    for coord in dataset:
      x_file.write("{0},".format(coord[0]))
      y_file.write("{0},".format(coord[1]))
      z_file.write("{0},".format(coord[2]))

  
    x_file.write("1")
    y_file.write("1")
    z_file.write("1")




if __name__ =='__main__':

  usage = "Usage: %prog [options]"
  parser = OptionParser(usage=usage)

  parser.add_option("-s", "--cubesize", type="int", dest="csize",
                     default=100, help="Specify how many data points in cube",
                     metavar="#CSIZE")
  parser.add_option("-t", "--tsize", type="int", dest="tsize",
                     default=500, help="Specifty how many data points total per image. Number of background noise datapoints = total points - data points in cube",
                     metavar="#TNOISE")
  parser.add_option("-c", "--cubenoise", type="float", dest="cnoise",
                     default=.01, help="Determine how noisy the generated cube data should be",
                     metavar="#CNOISE")


  (options, args) = parser.parse_args()

  dataset = []

  add_cube(dataset, options.cnoise, options.csize)
  add_background(dataset, options.tsize - options.csize)
  print_dataset(dataset)


