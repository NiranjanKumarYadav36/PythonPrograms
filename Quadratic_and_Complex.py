import math

# Function to compute roots of a quadratic equation
def compute_roots():
    while True:
        try:
            # Accept coefficients from the user
            a = int(input("Enter coefficient of x^2: "))
            b = int(input("Enter coefficient of x: "))
            c = int(input("Enter coefficient of constant if not enter zero: "))
            
            # Calculate discriminant
            discriminant = b * b - 4 * a * c
            
            # Check if discriminant is negative
            if discriminant < 0:
                print("Roots are complex numbers.")
                continue
            
            # Calculate roots
            r1 = (-b + math.sqrt(discriminant)) / (2 * a)
            r2 = (-b - math.sqrt(discriminant)) / (2 * a)
            
            print("Roots are:", r1, r2)
        except ValueError:
            print("Please enter valid numerical coefficients.")

# Function to perform operations on complex numbers
def perform_complex_operations():
    print("Enter first complex number:")
    real = float(input("Enter real part: "))
    imag = float(input("Enter imaginary part: "))
    num1 = complex(real, imag)

    print("Enter second complex number:")
    real = float(input("Enter real part: "))
    imag = float(input("Enter imaginary part: "))
    num2 = complex(real, imag)

    op = input("Enter operation (+ or - or * or /): ")
    try: 
        if op == '+':
            print(num1 + num2)
        elif op == '-':
            print(num1 - num2)
        elif op == '*':
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("Invalid operation entered.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except ValueError:
        print("Invalid input for complex numbers.")

# Main program
if __name__ == "__main__":
    print("1. Compute roots of a quadratic equation")
    print("2. Perform operations on complex numbers")

    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        compute_roots()
    elif choice == '2':
        perform_complex_operations()
    else:
        print("Invalid choice.")
