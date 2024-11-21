# used for plots  
import matplotlib.pyplot as plt 
# used to geenrate x values 
import numpy as np 
# used to handle commandline args
import sys 

# Handling the command line  
assert int(len(sys.argv)) != 1 and int(len(sys.argv)) <= 2,"""
Program needs one argument as the mode.
Useage example:
    python ./program <mode>
Suppoerted mode:
    1: f(x) = x
    2: f(x) = x*x
    3: f(x) = x * x * x
    4: f(x) = sin(x)
    5: f(x) = cos(x)
    6: f(x) = tan(x)
"""
mode = int(sys.argv[1])
# Getting the mode from the user
# Filling x values list 
xval = np.arange(-3, 3.1, 0.1)
# Function to fill the y values 
def f(x, mode):
    if mode == 1:
        return x
    elif mode == 2:
        return x * x
    elif mode == 3:
        return x * x * x
    elif mode == 4:
        return np.sin(x)
    elif mode == 5:
        return np.cos(x)
    elif mode == 6:
        return np.tan(x)
    else:
        raise Exception("Sorry, the mode you passed is not supported") 

# Filling the y values list 
yval = f(xval, mode)
plt.plot(xval, yval, label="f(x) = x")
plt.title("f(x)")
plt.ylabel("y")
plt.xlabel("x")
# plt.xlim(-5, 5.1)
plt.grid(True)
# uncomment to save the result to a png file in the directory ../plots 
# plt.savefig(f"./plots/output_mode{mode}.png")
plt.show()