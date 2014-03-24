#read in filename to save image to
arglist = argv ();
filename = arglist{1};

x = dlmread('datapoints/x.txt',',')
y = dlmread('datapoints/y.txt',',')
z = dlmread('datapoints/z.txt',',')

#add in integer after xyz to control size of datapoints. Default seems fine for now
#scatter3(x,y,z,5)

scatter3(x,y,z)
axis("off")

#print -dpng derp
print (filename, "-dpng")
