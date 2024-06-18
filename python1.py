'"Ans 1'"


'"Ans 2'"


'"Ans 3'"


'"Ans 4'"


'"Ans 5'"


'"Ans 6'"


'"Ans 7'"


'"Ans 8'"


'"Ans 9'"


'"Ans 10'"


'"Ans 11'"


'"Ans 12'"


'"Ans 13'"


'"Ans 14'"


'"Ans 15'"


'"Ans 16'"


'"Ans 17'"


'"Ans 18'"


'"Ans 19'"


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
