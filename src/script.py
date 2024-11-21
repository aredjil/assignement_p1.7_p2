# used for plots  
import matplotlib.pyplot as plt 
# used to geenrate x values 
import numpy as np 
# used to handle commandline args
import sys 

# Handling the command line  
assert int(len(sys.argv)) != 1 and int(len(sys.argv)) <= 2, "program needs one argument as the mode"
# Getting the mode from the user
mode = int(sys.argv[1])
# Filling x values list 
xval = np.arange(-5, 5.1, 0.1)
# Function to fill the y values 
def f(x, mode):
    if(mode == 1):
        return x
    else:
        raise Exception("Sorry, the mode you passed is not supported") 

# Filling the y values list 
yval = f(xval, mode)
plt.plot(xval, yval, label="f(x) = x")
plt.title("f(x)")
plt.ylabel("y")
plt.xlabel("x")
plt.xlim(-5, 5.1)
plt.grid(True)
# uncomment to save the result to a png file in the directory ../plots 
plt.savefig(f"./plots/output_mode{mode}.png")
plt.show()