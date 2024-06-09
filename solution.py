Here is a Python console application that solves the problem:

```python
import math

def check_sum_of_squares(n):
    if n < 0:
        return False
    for i in range(int(math.sqrt(n)) + 1):
        j = math.sqrt(n - i*i)
        if j == int(j):
            return True
    return False

def main():
    num = int(input("Enter a number: "))
    if check_sum_of_squares(num):
        print("The number can be expressed as a sum of two squares.")
    else:
        print("The number cannot be expressed as a sum of two squares.")

if __name__ == "__main__":
    main()
```

This program first asks the user to input a number. It then checks if the number can be expressed as a sum of two squares by iterating through all possible square numbers less than or equal to the input number. For each square number, it checks if the difference between the input number and the square number is also a square number. If it finds such a pair of square numbers, it prints that the number can be expressed as a sum of two squares. If it doesn't find such a pair, it prints that the number cannot be expressed as a sum of two squares.