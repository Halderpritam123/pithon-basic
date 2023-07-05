# please commant out and check


print("Hello, World!")

# Integer
var_int = 10
print("Type of var_int:", type(var_int), "Value:", var_int)

# Float
var_float = 3.14
print("Type of var_float:", type(var_float), "Value:", var_float)

# String
var_string = "Hello, World!"
print("Type of var_string:", type(var_string), "Value:", var_string)

# Boolean
var_bool = True
print("Type of var_bool:", type(var_bool), "Value:", var_bool)

# List
var_list = [1, 2, 3]
print("Type of var_list:", type(var_list), "Value:", var_list)

# Tuple
var_tuple = (4, 5, 6)
print("Type of var_tuple:", type(var_tuple), "Value:", var_tuple)

# Dictionary
var_dict = {'a': 7, 'b': 8, 'c': 9}
print("Type of var_dict:", type(var_dict), "Value:", var_dict)

# Set
var_set = {10, 11, 12}
print("Type of var_set:", type(var_set), "Value:", var_set)

# List Operation
numbers = list(range(1, 11))
print(numbers)

numbers.append(20)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.sort()
print(numbers)


#sum and average

def calculate_sum_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

numbers = [10, 20, 30, 40]
total, average = calculate_sum_average(numbers)
print("Sum:", total, "Average:", average)

#string reverse
def reverse_string(input_str):
    return input_str[::-1]

input_str = "Python"
reversed_str = reverse_string(input_str)
print(reversed_str)

#count vowel
def count_vowels(input_str):
    vowels = "aeiou"
    count = 0
    for char in input_str.lower():
        if char in vowels:
            count += 1
    return count

input_str = "Hello"
vowel_count = count_vowels(input_str)
print(f"Number of vowels: {vowel_count}")

#prime no
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 13
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#factorial calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}.")

#fibonacci
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

number = 5
fib_sequence = fibonacci(number)
print(fib_sequence)

#list comprehension
squared_list = [x ** 2 for x in range(1, 11)]
print(squared_list)


#1: Print the following pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#2. Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break 
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

# 3: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

middle = len(s1) // 2 

s3 = s1[:middle] + s2 + s1[middle:] 

print(s3)

# 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"

sorted_str = sorted(str1, key=lambda x: x.isupper())
# print(sorted_str)

arranged_str = "".join(sorted_str)

print(arranged_str)

# 5: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = [x + y for x, y in zip(list1, list2)] + list1[len(list2):] + list2[len(list1):]

print(new_list)


# 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = [x + y for x in list1 for y in list2]

print(new_list)

# 7: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, reversed(list2)):
    print(x, y)

# 8: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {employee: defaults for employee in employees}

print(result)

# 9: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)

# 10: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1) 
list1[1][0] = 222  
tuple1 = tuple(list1)  

print("tuple1:", tuple1)


# Tuple Unpacking
people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")


# Dictionary Manipulatio
def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]
person_dict = {}

add_person(person_dict, "John", 25)
print(person_dict)  

update_age(person_dict, "John", 26)
print(person_dict)

delete_person(person_dict, "John")
print(person_dict)

  
# Two Sum Problem
def find_two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
  
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum(nums, target)
print(result) 


# Palindrome Check
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."

word = "madam"
result = is_palindrome(word)
print(result)  

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr) 

# Implement Stack using Queue
from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  
stack.push(3)
print(stack.pop())
print(stack.pop()) 
print(stack.pop()) 

# FizzBuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")

# File I/O
def count_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            output_content = f"Number of words: {word_count}"

        with open(output_file, 'w') as file:
            file.write(output_content)

        print(f"Word count saved to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except:
        print("An error occurred while processing the file.")

input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)


# Exception Handling
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

result = divide_numbers(5, 0)
print(result)


