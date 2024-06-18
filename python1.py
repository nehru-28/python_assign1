'"Ans 1'"
def sum_of_numbers():
    num1 = int(input("Enter the first number: "))  
    num2 = int(input("Enter the second number: "))  
    sum = num1 + num2  
    print("The sum of ", num1 ,"and " ,num2,"is: " sum) 

'"Ans 2'"
def check_even_odd():
    num = int(input("Enter a number: ")) 
    
    if num % 2 == 0:
        print(num," is even.")
    else:
        print(num," is odd.")

'"Ans 3'"
def calculate_factorial():
    num = int(input("Enter a number: "))
    
    factorial = 1
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("The factorial of ",num," is: ",factorial)

'"Ans 4'"
def greet_user():
    name = input("What is your name? ")
    print("Hello, ",name,"! Good Morning.")

'"Ans 5'"
def write_to_file():
    user_input = input("Enter a string to write to the file: ")
    with open("output.txt", "w") as f:
        f.write(user_input)

'"Ans 6'"
def read_from_file():
    with open("output.txt", "r") as f:
        content = f.read()
        print(content)

'"Ans 7'"
def calculate_length():
    user_input = input("Enter a string: ")
    length = len(user_input)
    print("The length of the string is: ",length)

'"Ans 8'"
def concatenate_strings():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = str1 + str2
    print("The concatenated string is: ",result)

'"Ans 9'"
def check_substring():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")
    
    if substring in main_string:
        print(f"The substring '",substring," is present in the main string.")
    else:
        print(f"The substring ",substring," is not present in the main string.")

'"Ans 10'"
def convert_to_uppercase():
    user_input = input("Enter a string: ")
    uppercase_string = user_input.upper()
    print("The string in uppercase is: ",uppercase_string)

'"Ans 11'"
def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

'"Ans 12'"
def sum_of_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits

'"Ans 13'"
def calculate_age(birth_year):
    age = 2024 - birth_year
    return age

'"Ans 14'"
def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("Lines entered:")
    for line in lines:
        print(line)

'"Ans 15'"
import csv
def read_csv_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

'"Ans 16'"
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

'"Ans 17'"
def convert_to_title_case(input_string):
    return input_string.title()

'"Ans 18'"
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

'"Ans 19'"
import string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

'"Ans 20'"
def listSum(lst : list) -> int :
  return sum(lst)

'"Ans 21'"
def countOccurrence(lst : list , element) -> int :
  return lst.count(element)

'"Ans 22'"
def minmax(lst : list) :
  print('Minimum value is :',min(lst))
  print('Maximum value is :',max(lst))

'"Ans 23'"
def convertTemp(scale , temp) -> float :
  if scale == 'Celsius' :
    return temp*1.8 + 32
  elif scale == 'Fahrenheit':
    return (5*temp)/9 - 32
  else :
    pass

'"Ans 24'"
def Calculator(n1 : int , n2 : int ,operation) -> int:
  if operation == '+':
    return n1 + n2
  elif operation == '-':
    return n1 - n2
  elif operation == '*':
    return n1 * n2
  else :
    try :
      return n1/n2
    except ZeroDivisionError :
      pass

'"Ans 26'"
def checkElement (string,element) -> bool :
  n = len(element)
  s1 = string[:n]
  s2 = string[-n:]
  if s1 == element :
    return True
  elif s2 == element :
    return True
  else :
    return False

'" Ans 27 "'
def convertString2List (string) -> list :
  return list(string)
