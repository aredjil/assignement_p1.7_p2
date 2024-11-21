import matplotlib.pyplot as plt 
import sys 

# Handling the command line  
assert int(len(sys.argv)) != 1 and int(len(sys.argv)) <= 2, "program needs one argument as the mode"
# Getting the mode from the user
mode = int(sys.argv[1])