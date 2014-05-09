import subprocess
import time




if __name__ =='__main__':

  for n in range(1, 2):
    
    cmd = "./run2.sh {0} {1}".format(n*100, 1)

    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read();

    print ret

    times = []
    for line in ret.split():
      if line[0].isdigit():
        times.append(float(line))

    print "Total: {0}".format(times[-1] - times[0])
    print "Start Set: {0}".format(times[1] - times[0])
    print "Sim Set: {0}".format(times[2] - times[1])
    print "RandRots: {0}".format(times[3] - times[2])
    print "Color: {0}".format(times[4] - times[3])



