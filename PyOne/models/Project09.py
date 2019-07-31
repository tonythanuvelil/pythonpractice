# Clock
from time import clock, sleep
import sys
start = clock()
print("Started.")
sleep(1)
stop = clock() - start
print("Slept for", stop, "seconds.")
print(sys.version)  # Prints the version of Python running
