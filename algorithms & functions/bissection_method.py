import matplotlib.pyplot as plt
import numpy as np

def fx(x):
    return(((x+5)**2)-10)

## INPUTS ##
range_l = float(-5) ## This entry and the one below it represent the initial values for the algorithm, it must contain at least and prefferably for this algo, exactly one root anywhere in it
range_r = float(5) ## Narrower intervals imply lower computing time and more precise approximations.
step = float(0.0001) ## <- Non continuous increments x, lower values will make it so the computer evaluates f(x) more precisely, the size of this value may imply on the target precision if is set too high(ex. >0.001)
precision_raw = 5 ## <- This is the desired size of the approximated interval which contains the root of the function
## INPUTS ##

range = (range_r - range_l)
precision_weighted = (range-precision_raw)/range

i = range_l
function_img = []
function_dom  = []

while(i <= range_r):
    function_img.append(fx(i))
    function_dom.append(i)
    i += step

known_root = [-1.838, 0]
aprox_root = []

plt.plot(function_dom, function_img,'o', color = "red", markersize=1, label = "(f(x), y)")
plt.plot([range_l, range_r], [0, 0], color = "black", label = "X-Axis")
plt.plot(known_root[0], known_root[1], "r+", markersize=10, label = "Exact Root")
plt.legend()
plt.title("Root approximation by the bissection method")
plt.show()