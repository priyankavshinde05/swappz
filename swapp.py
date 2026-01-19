import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except IndexError:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
except ValueError:
    print("Please enter valid integers")
    sys.exit(1)

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
