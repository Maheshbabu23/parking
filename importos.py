import os
from ParkingTask import Park



if os.path.exists("task.txt"):
  myfile = open("task.txt","r")
  user_responce = myfile.readlines()
  print(type(user_responce))
  a = user_responce[0].split('  ')
  floors = len(a)
  # print(floors)
  # Slots = 
  ll= []
  for i in range(len(a)):
    # print(type(i))
    # print(a[i])
    # print((len(a[i])))
    ll.append(eval(a[i]))
  available = 0
  occupied = 0
  floor = 0
  floor1 = 0
  for k in ll:
    floor_count_a = k.count('1')
    floor_count_o = k.count('0')
    available+=floor_count_a
    occupied +=floor_count_o
    floor+=1
    floor1+=1
  # print(available,occupied)
  Slots = (available+occupied)/floors
  # print(Slots)
  user_responce=ll
  
  print(user_responce)
  Park(user_responce,floors,Slots)


else:
  floors = int(input("Enter How Many Floors in Building : "))
  Slots = int(input("Enter How Many Slots in Each Floor Building : "))
  user_responce=[["1" for i in range(Slots)] for j in range(floors)]
  print(f"floors= {floors} ,per_floor_slots = {Slots}")
  Park(user_responce,floors,Slots)


