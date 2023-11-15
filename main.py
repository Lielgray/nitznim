Aelevator = int(input("enter elevator A floor"))
Belevator = int(input("enter elevator B floor"))
Ellis = int(input("enter ellis floor"))

if ((Aelevator < -3) or (Aelevator > 9) and (Belevator < -3) or (Belevator >9)):
  print("not avaiable")
if ((Ellis < -3) or (Ellis > 9)):
  print("not avaiable")
  
find = (Aelevator - Ellis)
findB = (Belevator - Ellis)

if (find < -1):
  find = find * -1
if (findB < -1):
  findB = findB * -1
  
if (find) < (findB):
    print("elevator A is closer")
elif (find) == (findB):
    print("elevator A will come")
else:
    print("elevator B is closer")