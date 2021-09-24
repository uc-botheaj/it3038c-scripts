def isDigit(s):
  if s.strip().isdigit():
    return True
  else:
    return False

myNum = input("What is your number?")
print(myNum)

while not isDigit(myNum):
  print("please enter a number.")
  myNum = input()
  if isDigit(myNum):
    break

print("thank you")



