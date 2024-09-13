# function that modifies a global variable
def modify_x():
    global x  # Declare that we're modifying the global x
    x = x + 10  # Modify the global variable

def modify_y():
    global y  # Declare that we're modifying the global y
    y = y * 2  # Modify the global variable

x = 34
y = 56

modify_x()
modify_y()

print(x)  # Output: 44
print(y)  # Output: 112