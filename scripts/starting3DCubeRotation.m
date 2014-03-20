# This script applies a random 3D rotation to the starting unit cube.
# We do this so that the hidden cube is not always the same.
# All we are doing is a simple rotation before hiding the cube in extra dimensions
# of noise.
arglist = argv ();
total_dims = str2num(arglist{1})

dims = 3

err = .00001

data = [];

for i=1:dims
  data = [data;dlmread(sprintf('pre_cube_rot_dim%i.txt',i),',')];
end


#generate random rotation matrix
# code taken from http://www.mathworks.com/matlabcentral/newsreader/view_thread/298500

[Q,R] = qr(randn(dims));
Q = Q*diag(sign(diag(R)))

#verify Q is a rotation matrix
d = det(Q)
if (d < (1.0 + err) && d > (1.0 - err))
  printf("det(Q) is 1. \n")
else
  printf("det(Q) is not 1. Will attempt to fix. \n")
  Q(:,1) = Q(:,1) * -1
  d = det(Q)
  if (d < (1.0 + err) && d > (1.0 - err))
    printf("det(Q) is now 1. Q is fixed \n")
  else
    printf("Could not fix Q. det(Q) is not 1")
    quit(1)
  endif
  
endif

V = Q' - inverse (Q)
if all( all( V < err ))
  printf("Q' == inverse (Q). Q is a rotation matrix \n")
else
  printf("Q' != inverse (Q).  Q is not a rotation matrix \n")
  quit(1)
endif


rotdata = [];

rotdata = Q * data;

#iterate thru dimensions and print each dimension to file
for i=1:(length(data(:,1)))
  csvwrite(sprintf('dim%i.txt',i),rotdata(i,:))
end

#print 3D picture of starting cube
scatter3(rotdata(1,:), rotdata(2,:), rotdata(3,:))
axis("off")
print -dpng startingCube



#iterate thru all dimensions and print picture of pair of dims
#this is so we can visualize the starting dataset. This is what 
#we are searching for when performing random rotations on the 
#simulated dataset
alldata = [];
for i=1:total_dims
  alldata = [alldata;dlmread(sprintf('dim%i.txt',i),',')];
end

for i=1:(length(alldata(:,1)))
  for j=(i+1):(length(alldata(:,1)))
    scatter(alldata(i,:), alldata(j,:))
    axis("off")
    print (sprintf('startdata.%i-%i.png',i,j), "-dpng")
  end
end


