import math

def main():
    x = int(input("Enter the first number: "))
    print("X squared is:", square(x))
    r = int(input("Enter the radius: "))
    print("Area of the circle is:", radius(r))

def square(n):
    return n * n

def radius(r):
    return math.pi * r * r

if __name__ == "__main__":
    main()