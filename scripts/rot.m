#read in filename to save image to; read in number of dimensions in data
arglist = argv ();
filename = arglist{1};
dims = str2num(arglist{2});

data = []

for i=1:dims
  data = [data;dlmread(sprintf('datapoints/dim%i.txt',i),',')]
end


#generate random rotation matrix
# code taken from http://www.mathworks.com/matlabcentral/newsreader/view_thread/298500

[Q,R] = qr(randn(dims))
Q = Q*diag(sign(diag(R)))

rotdata = []

#iterate thru points
for i=1:(length(data(1,:)))
  point = data(:,i)
  rotdata = [rotdata,Q*point]
end

#iterate thru dimensions and print each pair of dims
for i=1:(length(data(:,1)))
  for j=(i+1):(length(data(:,1)))
    scatter(rotdata(i,:), rotdata(j,:))
    axis("off")
    print (sprintf('%s.%i-%i.png',filename,i,j), "-dpng")
  end
end


#scatter3(x,y,z)
#scatter3(rotdata(1,:),rotdata(2,:),rotdata(3,:))
#scatter3(data(1,:),data(2,:),data(3,:))
#scatter(roty,rotz)

#axis("off")

#print -dpng derp
#print (filename, "-dpng")
