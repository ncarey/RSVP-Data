#read in filename to save image to
#arglist = argv ();
#filename = arglist{1};

x = dlmread('datapoints/x.txt',',')
y = dlmread('datapoints/y.txt',',')
z = dlmread('datapoints/z.txt',',')

#x = [1,1,-1,-1,1,1,-1,-1]
#y = [1,-1,-1,1,1,-1,-1,1]
#z = [1,1,1,1,-1,-1,-1,-1]



#generate random rotation matrix

[Q,R] = qr(randn(3))
Q = Q*diag(sign(diag(R)))

rotx=[]
roty=[]
rotz=[]

for i=1:(length(x))
  point=[x(:,i);y(:,i);z(:,i)]
  rot_p = Q*point
  rotx = [rotx,rot_p(1,:)]
  roty = [roty,rot_p(2,:)]
  rotz = [rotz,rot_p(3,:)]
end



#add in integer after xyz to control size of datapoints. Default seems fine for now
#scatter3(x,y,z,5)

#scatter3(x,y,z)
#scatter3(rotx,roty,rotz)
scatter(roty,rotz)
#axis("off")

#print -dpng derp
#print (filename, "-dpng")
