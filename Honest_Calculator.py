import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer() == True:
        output = True
    else:
        output = False
    return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg = msg + msg_6
    else:
        pass
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    else:
        pass
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    else:
        pass
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    else:
        pass
    
memory = 0
memory = float(memory)
while True:
  print(msg_0)
  calc = input()
  try:
      x, oper, y = calc.split()
      if x == "M":
          if y == "M":
              x = memory
              y = memory
          else:
              x = memory
              y = float(y)
      elif y == "M":
          y = memory
          x = float(x)
      else:
         y = float(y)
         x = float(x)
  except ValueError:
      print(msg_1)
      continue
  if oper == "+" or oper == "-" or oper == "*" or oper == "/":
      check(x, y, oper)
      if oper == "+":
          result = x + y
      elif oper == "-":
          result = x - y
      elif oper == "*":
          result = x * y
      elif oper == "/" and y != 0:
          result = x / y
      elif oper == "/" and y == 0:
          print(msg_3)
          continue
  else:
      print(msg_2)
      continue
  print(result)
  while True:
      print(msg_4)
      answer = input()
      if answer == "y":
          if is_one_digit(result):
              msg_index = 10
              while True:                  
                  msg_ = [0,1,2,3,4,5,6,7,8,9,msg_10,msg_11,msg_12]
                  print (msg_[msg_index])
                  answer = input()
                  if answer == "y":
                      if msg_index < 12:
                          msg_index = msg_index + 1
                          continue
                      else:
                          memory = result
                          break
                  else:
                      if answer == "n":
                          break
                      else:
                          continue
          else:
              memory = result
      elif answer == "n":
          pass
      else:
          continue
      break
  while True:
      print(msg_5)
      answer = input()
      if answer == "y":
          break
      elif answer == "n":
          sys.exit()
      else:
          continue
  continue
