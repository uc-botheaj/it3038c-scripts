import time

start_time = time.time()

print('What is your name?') 
myName = input()

## prompt for a specific name
# while myName != 'your name':
#   print('This is not "your name". Please type "your name"?')
#   myName = input()


# while myName != "AJ":
#   if myName == 'your name':
#     print('ha ha, very funny. Seriously, who are you?') 
#     myName = input()
#   else:
#     print("That's not your name. Please tell me your real name.")
#     myName = input()

while True:
  print("please type your name.")
  myName = input()
  if myName == 'your name':
    break
print("thank you")

print('hello, ' + myName + '. That is a good name. How old are you?') 
myAge = int(input())

# determine message based on age 
if myAge < 13:
  print("Learning young, that's good")
elif myAge == 13:
  print("You're a teenager now... that's cool I guess")
elif myAge > 13 and myAge < 30:
  print("Still young, still learning")
elif myAge >= 30 and myAge <= 65:
  print("Now you're adulting")
else:
  print("... you've lived a long time!")

time.sleep(2)
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old" % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2)) 

time.sleep(1)
print("I'm tired. I go sleep now.")


