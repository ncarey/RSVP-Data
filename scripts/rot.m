#read in filename to save image to; read in number of dimensions in data
arglist = argv ();
filename = arglist{1};
dims = str2num(arglist{2});

err = .00001

data = [];

for i=1:dims
  data = [data;dlmread(sprintf('datapoints/dim%i.txt',i),',')];
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

#iterate thru dimensions and print each pair of dims
for i=1:(length(data(:,1)))
  for j=(i+1):(length(data(:,1)))
    scatter(rotdata(i,:), rotdata(j,:))
    axis("off")
    print (sprintf('%s.%i-%i.png',filename,i,j), "-dpng")
  end
end

