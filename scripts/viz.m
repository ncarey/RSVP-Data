arglist = argv ();
filename = arglist{1};

x = dlmread('/home/ncarey/gitrepos/RSVP-Data/data/testx.txt',',')
y = dlmread('/home/ncarey/gitrepos/RSVP-Data/data/testy.txt',',')
z = dlmread('/home/ncarey/gitrepos/RSVP-Data/data/testz.txt',',')

#x = [1,1,-1,-1,1,1,-1,-1]
#y = [1,-1,-1,1,1,-1,-1,1]
#z = [1,1,1,1,-1,-1,-1,-1]

scatter3(x,y,z)

axis("off")
print -dpng filename
