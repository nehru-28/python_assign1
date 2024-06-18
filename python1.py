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
