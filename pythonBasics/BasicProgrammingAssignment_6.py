# 1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
# 2.	Write a Python Program to Find Factorial of Number Using Recursion?
# 3.	Write a Python Program to calculate your Body Mass Index?
# 4.	Write a Python Program to calculate the natural logarithm of any number?
# 5.	Write a Python Program for cube sum of first n natural numbers?
import math

class BasicProgrammingAssignment6:

    """Display Fibonacci Sequence Using Recursion"""
    n1, n2 = 0, 1

    def generate_fibonacci(self, n):
        if n >= 1:
            n3 = self.n1 + self.n2
            print(n3, end=" ")
            self.n1 = self.n2
            self.n2 = n3
            self.generate_fibonacci(n - 1)

    """Factorial of Number Using Recursion"""

    def factorial(self, n):
        if n == 1:
            return n
        else:
            return n * self.factorial(n - 1)
         

    """Calculate BMI"""

    def calculateBMI(self):
        weight = float(input("Enter weight in kgs: "))
        height = float(input("Enter height cms: "))
        calc_bmi = weight / ((height / 100) ** 2)
        if calc_bmi < 18.5:
            status = "Underweight"
        elif calc_bmi >= 18.5 and calc_bmi <= 24.9:
            status = "Normal"
        elif calc_bmi >= 25 and calc_bmi <= 29.9:
            status = "Overweight"
        elif calc_bmi >= 30:
            status = "Obese"
        print(f"Your BMI is \"{calc_bmi}\" and the status is \"{status}\"")
         

    """calculate the natural logarithm of any number"""

    def find_natural_log(self, n):
        print(f"Natural logarithm of {n} is {math.log(n)}")
         

    """cube sum of first n natural numbers"""

    def cube_sum_natural_num(self, n):
        sum1 = 0
        for i in range(n + 1):
            sum1 = sum1 + (i ** 3)
        print(f"Cube sum of first {n} natural numbers is {sum1}")
         


obj = BasicProgrammingAssignment6()
print("\n======================================================================================")
# Fibonacci series
fib_num = int(input("Enter non negative number to generate its fibonacci series: "))
print(f"First {fib_num} fibonacci series numbers are:")
if fib_num <= 1:
    print(obj.n1, obj.n2)
else:
    print(obj.n1, obj.n2, end=" ")
    obj.generate_fibonacci(fib_num-2)
print("\n======================================================================================")

# factorial
fact_num = int(input("Enter a non-negative number to find its factorial: "))
if fact_num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"Factorial of {fact_num} is \n", obj.factorial(fact_num))
print("\n======================================================================================")

# BMI
obj.calculateBMI()
print("\n======================================================================================")

# natural log
obj.find_natural_log(12)
print("\n======================================================================================")

# cube sum of natural numbers
obj.cube_sum_natural_num(2)
obj.cube_sum_natural_num(5)
print("\n======================================================================================")

