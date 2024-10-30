# Function to perform calculations
def calculate_operations(a, b, c):
    total_sum = a + b + c
    difference = a - b - c
    product = a * b * c
    average = total_sum / 3
    
    return total_sum, difference, product, average

# Main part of the program
if __name__ == "__main__":
    # Input: Getting three numbers from the user
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    
    # Calculating operations
    total_sum, difference, product, average = calculate_operations(a, b, c)
    
    # Output: Displaying the results
    print(f"Sum: {total_sum}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Average: {average}")
                                #Q2 start 
import math

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_square(side):
    return side * side

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def area_of_rectangle(length, width):
    return length * width

def main():
    print("Select the shape to calculate the area:")
    print("1. Triangle")
    print("2. Square")
    print("3. Circle")
    print("4. Rectangle")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_of_triangle(base, height)
        print(f"Area of the triangle: {area}")

    elif choice == '2':
        side = float(input("Enter the side length of the square: "))
        area = area_of_square(side)
        print(f"Area of the square: {area}")

    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = area_of_circle(radius)
        print(f"Area of the circle: {area}")

    elif choice == '4':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_of_rectangle(length, width)
        print(f"Area of the rectangle: {area}")

    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()














        



    


                           










