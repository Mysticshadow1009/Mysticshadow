name1=input('enter name : ')
name2=input('enter name : ')
list1=[]
list2=[]

for l in name1:
    list1.append(l)        
for l in name2:
    list2.append(l)
common_letters=0

for i in list1:
    if(i in list2):
        try:
            list2.remove(i)
        except:
            continue
        common_letters+=1

uncommon_letters=len(list1)+len(list2)-common_letters
print('total uncommon_letter : ',uncommon_letters)
flames=['friend','love','affection','marriage','enemy','sister']
rolling=True

#refactoring the prog
def remove_lessno_flames():
    flames.pop(uncommon_letters-1)
    
def remove_moreno_flames():
    uncommon=uncommon_letters
    uncommon-=len(flames)
    while True:
        try:
            flames.pop(uncommon-1)
            break
        except:
            uncommon-=len(flames)
        
#main prog rolling
while rolling:
    if(len(flames)==1):
        print(flames[0].upper(),'   <--answer to your relationship')
        break    
    elif(len(flames)<uncommon_letters):
        remove_moreno_flames()
    elif(len(flames)>=uncommon_letters):
        remove_lessno_flames()
    else:
        print("something is wrong")
        break

