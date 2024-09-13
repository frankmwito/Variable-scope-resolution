# Global variable
x = 20

def demo():
    # Local variable with the same name
    x = 5
    print("Local x inside the function:", x)  # Prints the local variable

# Call the function
demo()

# Print the global variable
print("Global x outside the function:", x)  # Prints the global variable

