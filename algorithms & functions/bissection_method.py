import matplotlib.pyplot as plt
import numpy as np

def fx(x): ## Function function... i think no more words are needed here
    return(((x+5)**2)-10)

## INPUTS ##
range_l = float(-3) ## This entry and the one below it represent the initial values for the algorithm, it must contain at least and prefferably for this algo, exactly one root anywhere in it
range_r = float(-1) ## Narrower intervals imply lower computing time and more precise approximations.
step = float(0.00001) ## <- Non-continuous increments x for computing f(x), lower values will make it faster but at a huge cost for precision. Consider step between [0.1, 0.0001]
precision_raw = 0.1 ## <- This is the desired size of the approximated interval which contains the root of the function, Consider step between [a, 0.0001], a must be smaller than range
iterations_max = 100 ## Max number of iterations so the algo wont fry your computer up, or for more controled tests
## INPUTS ##
precision_weighted = 0
range = (range_r - range_l) ## Size of the initial interval

if(precision_raw > 0.0001):
    precision_weighted = (precision_raw/range)## Weights the precision based on the initial interval size, an equal amount for precision_raw implies higher precision as the initial interval gets bigger, and vice-versa. Fact not represented mathematically given precision_raw only.
else:
    print("Mathplotlib cant handle precision_raw values lower than 0.0001!! Automatically setting it to 0.0001.")
    precision_raw = 0.0001
    precision_weighted = (precision_raw/range)

if(step < 0.0001):
    print("Mathplotlib cant handle precision_raw values lower than 0.0001!! Automatically setting it to 0.0001.")
    precision_raw = 0.0001
known_root = [-1.838, 0]
aprox_root = []
function_img = []
function_dom  = []
i = range_l
while(i <= range_r):
    function_img.append(fx(i))
    function_dom.append(i)
    i += step
plt.plot(function_dom, function_img,'o', color = "red", markersize=1, label = "(x, f(x))")
plt.plot([range_l, range_r], [0, 0], color = "black", label = "X-Axis")
plt.plot(known_root[0], known_root[1], "r+", markersize=10, label = "Exact Root")
k = 0
print(range)
print(precision_weighted)
divisons_x = []
range = range/2
##if fx(range+range_l) * fx(range_l) > 0:
##    range_l = range+range_l
##    range_r = range_r
##else:
##    range_r = range_r-range
##    range_l = range
a = range_l
b = range_r
x = (range_r+range_l)/2
k = 0
temp = 0    
while(k <= iterations_max):
    temp




plt.legend()
plt.title("Root approximation by the bissection method")
plt.show()