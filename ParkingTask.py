import math
floors = int(input("Enter How Many Floors in Building : "))
Slots = int(input("Enter How Many Slots in Each Floor Building : "))

def parking ():

    myfile = open("task.txt","r")
    lines = myfile.readlines()
    print(type(lines))
    print(lines)
    ll = lines[0].replace('[',"").replace(']',"")
    a = ll.split(',')
    Available,Occupied = int(a[0]),int(a[1])
    print(type(Occupied))
    print(''' Choose Your Response
            1 . Parking 
            2 . Get
            3 . Slots Available
            4 . Exit ''')
    val = int(input('Enter a Menu Value : '))
    
    flr = 1
    # Occupied = 0
    # Available = 0
    count = Slots*floors
    # print(f"the c value is {count}")
    # print(Occupied)


    # val = input('Enter a Menu Value : ')
    # string = val.lower()
    if 1 == val:
        if Occupied == count:
            return f" There is No Available Space to park "
    
        # elif Occupied<0:
        #     return f" There is No cars Available Parking Lot "
        else:
            flr = math.ceil(Occupied/Slots)
            print( f"  Park The vechicle At Floor Number {flr} ")
            Available -= 1
            Occupied += 1
            
            
    elif 2 == val:
        return f'Total Vehicles Available in Parking :{Occupied} '
    elif 3 == val:
        return f" Total Availables Slots For Parking {Available}"
    
    else:
        if  Available == count:
            return f"Parking Lot is Empty"
        else:
            Occupied -=  1
            Available += 1


    ls = [Available,Occupied,count]
    f = open('task.txt','w+')
    f.write(str(ls))
    f.close()
    # print('Parked At  : ',count)
    print('Total Vehicles Available : ',Available)
    print('Total Vehicles Occupied : ',Occupied)
    print( f'Total Slots For Building :{count} ')
 
parking()