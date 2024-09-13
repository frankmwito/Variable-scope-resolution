# function where a global variable is updated inside a loop.

def global_loop():
    for i in range(3):
        global x
        x += i
        print(i)
    
x = 3

global_loop()