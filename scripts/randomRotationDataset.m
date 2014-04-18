arglist = argv ();
dims = str2num(arglist{1});
#numrots = str2num(arglist{2});
numrotstart = str2num(arglist{2});
numrotend = str2num(arglist{3});
err = .00001

data = []

for i=1:dims
  data = [data;dlmread(sprintf('../simulatedSet/dim%i.txt',i),',')];
end


rotnum = numrotstart


for rotnum=numrotstart:numrotend

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



  #grab simulated rotation matrix to caclulate principle angles
  simrot = []
  simrot = dlmread('../simulatedSet/rotation_matrix.txt',',');
  
  #testing 
  #Q = simrot'
  Q = Q(1:2,:);
  rotdata = Q * data;
  
  A = simrot(:,1:3);

  #B = Q(1:2,:)'

  theta = subspace(A,Q')
  


  #print out rotation matrix
  csvwrite(sprintf('%0.5f.rotation_matrix.txt',theta),Q)

  


  #put corners on for uniform hist bins
  X = [rotdata(1,:)';2.1;2.1;-2.1;-2.1];
  Y = [rotdata(2,:)';2.1;-2.1;2.1;-2.1];
  hist_mat = [X,Y];
  
  #some hacked up code to filter everything outside of -2,2
  idx = ( hist_mat(:,1)<=2.1);
  hist_mat1 = hist_mat(idx,:);
  idx = ( hist_mat1(:,2)<=2.1);
  hist_mat2 = hist_mat1(idx,:);
  idx = ( hist_mat2(:,1)>=-2.1);
  hist_mat3 = hist_mat2(idx,:);
  idx = ( hist_mat3(:,2)>=-2.1);
  hist_mat4 = hist_mat3(idx,:);


  colormap(gray())
  axis([-2,2,-2,2],"square")
  [c,x,y] = hist2d(hist_mat4,60,60); imagesc(x,y,c)
  axis([-2,2,-2,2],"square")
  axis("off")
  set(gca,'ydir','normal');
 
  print (sprintf('hist/%0.5f.hist.randrot.1-2.png',theta), "-dpng", "-S512,512")
  #print (sprintf('hist/%i.hist.randrot.1-2.png',rotnum), "-dpng", "-S512,512")
  
  scatter(rotdata(1,:), rotdata(2,:),[],[0,0,0],"filled")
  set (gcf, 'color', 'black')
 
  axis([-2,2,-2,2],"square")
  axis("off")
  print (sprintf('scatter/%0.5f.randrot.1-2.png',theta), "-dpng", "-S512,512")
  #print (sprintf('scatter/%i.randrot.1-2.png',rotnum), "-dpng", "-S512,512")

  #iterate thru dimensions and print each pair of dims
  #for i=1:(length(data(:,1)))
  #  for j=(i+1):(length(data(:,1)))
  #    scatter(rotdata(i,:), rotdata(j,:))
  #    axis("off")
  #    print (sprintf('%i.randrot.%i-%i.png',rotnum,i,j), "-dpng")
  #  end
  #end

end

