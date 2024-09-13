# use of nonlocal keyword
 
def outer_function():
    x = 10  # Local variable in outer_function
    print("Initial x in outer_function:", x)
    
    def inner_inner_function():
        nonlocal x  # Accessing the outer function's variable
        x = 20 * x  # Modifying the x variable
        print("Modified x in inner_inner_function:", x)
        
    inner_inner_function()  # Calling the inner function
    
    print("x after modification in outer_function:", x)

# Calling the outer function
outer_function()

