# implement a function that modifies an enclosing scope using nonlocal.

def outer_function():
    x = 10
    y = 45
    
    print(f"sum of local variables: {x + y}")
    
    def inner_function():
        nonlocal x, y  # use nonlocal to modify enclosing scope variables
        x = 3 * x
        y = 3 * y
        print(f"sum of local variables after being modified using nonlocal keyword: {x + y}")
        
    inner_function()

outer_function()


def func1():
    x = 10
    def func2():
        print(x) # If you want to modify x inside func2(), you would need to use the nonlocal keyword.
    func2()

func1()