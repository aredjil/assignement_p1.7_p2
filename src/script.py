# used for plots  
import matplotlib.pyplot as plt 
# used to geenrate x values 
import numpy as np 
# used to handle commandline args
import sys 

def main():
    pass 
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
modes_dict ={1:"x", 2:"x*x", 3:"x * x * x", 4:"sin(x)", 5:"cos(x)", 6:"tan(x)"}
# Getting the mode from the user
mode = int(sys.argv[1])
# checking if the passed mode is supported 
assert mode in np.arange(1, 7, 1), """The mode you selected is not supported, please use one of the available modes
Suppoerted mode:
    1: f(x) = x
    2: f(x) = x*x
    3: f(x) = x * x * x
    4: f(x) = sin(x)
    5: f(x) = cos(x)
    6: f(x) = tan(x)
"""
# Filling x values list 
xval = np.arange(-3, 3.1, 0.1)
# Function to fill the y values 
def f(x:int, mode:int)->int:
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
def plot_list(xval:np.array, yval:np.array, mode:int):
    plt.plot(xval, yval, label=f"f(x) = {modes_dict[mode]}")
    plt.title("f(x)")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(loc="best")
    # plt.xlim(-5, 5.1)
    plt.grid(True)
    # uncomment to save the result to a png file in the directory ../plots 
    # plt.savefig(f"./plots/output_mode{mode}.png")
    return plt.show()
plot_list(xval, yval, mode)
if __name__ == "__main__":
    main()