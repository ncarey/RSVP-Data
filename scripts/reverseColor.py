import subprocess

cmd = "ls"
files = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().split()

for mfile in files:
  cmd = "convert {0} -color-matrix '6x3: -1  0  0 0 0 1 0 -1 0 0 0 1 0 0 -1 0 0 1' {0}".format(mfile)

  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

