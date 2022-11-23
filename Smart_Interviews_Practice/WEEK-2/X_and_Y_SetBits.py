"""
Create a number with Xth place Set bit and Yth place set bits.
 
NOTE: Must be carefull at corner case "x=y"
"""
def fun_x_y(x,y):
    return (1<<x)|(1<<y)

x,y=map(int.input().split())
print(fun_x_y(x,y))