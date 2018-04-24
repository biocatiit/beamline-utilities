import subprocess
import time

proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)

proc.stdin.write('plot sin(x)\n')
time.sleep(2)
proc.stdin.write('plot 2*x+3\n')
time.sleep(2)
proc.stdin.write('quit\n')
