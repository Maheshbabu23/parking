import os


def Park (user_responce,floors,Slots):
    print(''' Choose Your Response
            1 . Parking 
            2 . Slots Available
            3 . Get
            4 . View
            5 . Exit ''')
    def parking():
        cnt = 0
        floor = 0
        slot = 0
        for i,j in enumerate(user_responce):
            while cnt < Slots:                
                if i == floor and j[cnt] == '1':
                    floor = floor+1
                    slot = slot+1
                    # print(f"floor : {floor} and slot : {slot} and value is = {j[cnt]}")
                    j[cnt] = '0'
                    print(f"Your Ticket Number {floor} . {slot} ")
                    break
                cnt = cnt + 1
                slot = slot+1
            cnt = 0
            slot = 0
            floor = floor +1
        return ' -'

    def slotsavailable():
        cnt = 0
        floor = 0
        for k in user_responce:
            floor_count = k.count('1')
            cnt+=floor_count
            floor+=1
            print( f"floor :{floor} -- AvailableSlots :{floor_count}")
        return f"Total Available Slots in Building : {cnt}"
        

    def get():
        tkn = input("Enter Your Ticket No ")
        Token = tkn.split('.')
        flr,sl=int(Token[0]),int(Token[1])
        cnt = 0
        floor = 0
        slot=0
        if flr <= floors and sl <= Slots:
            for i,j in enumerate(user_responce):
                while cnt < Slots:
                    if i == floor and j[cnt] == '0':
                        if floor==flr-1 and slot == sl-1:
                            floor = floor+1
                            slot = slot+1
                            # print(f"floor : {floor} and slot : {slot} and value is = {j[cnt]}")
                            j[cnt] = '1'
                            # print(f"floor : {flr} and slot : {sl} and value is = {j[cnt]}")
                            break                        
                    # else:
                    #     return 'wrong parking number'
                        

                    cnt = cnt + 1
                    slot = slot+1 
                cnt = 0
                slot = 0
                floor = floor +1
            
            return f"{tkn} Slot is available for parking "
            
                
        else:
            return 'Please  Enter Valid Token No'

    def view():
        for k in user_responce:
            print(k)
        return ' '

    def save():
        available = 0
        occupied = 0
        floor = 0
        floor1 = 0
        count = floors*Slots
        ls =[]
        for k in user_responce:
            floor_count_a = k.count('1')
            floor_count_o = k.count('0')
            available+=floor_count_a
            occupied +=floor_count_o
            floor+=1
            floor1+=1
            print(k)

            ls.append(str(k))
        print(type(ls))
        print(ls)
        with open('task.txt','w') as tfile:
            tfile.write('  '.join(ls))


        print('Done')
        print(available,' available')
        print(occupied,' occupied')
        print(count,' total')
            
    choice=int(input("You response: "))
    op_dict={1:'print(f" {parking()}")&Park(user_responce,floors,Slots)',2:'print(slotsavailable())&Park(user_responce,floors,Slots)',
             3:'print(f" {get()}")&Park(user_responce,floors,Slots)',4:'print(f" {view()}")&Park(user_responce,floors,Slots)',5:'save()&print("Exiting The Building")'}
    for i in op_dict[choice].split('&'):
      eval(i)
    return
