'''    TIC TAC TOE     '''
print('welcome to tic tac toe')

import random
numbers=[1,2,3,4,5,6,7,8,9]
table=[[1,2,3],[4,5,6],[7,8,9]]
rows=3
col=3
def correct():
    a = False
    if (table[0][0] == table[0][1] == table[0][2] or
        table[1][0] == table[1][1] == table[1][2] or
        table[2][0] == table[2][1] == table[2][2]):
        a = True
        print("Row win")
    if (table[0][0] == table[1][0] == table[2][0] or
        table[0][1] == table[1][1] == table[2][1] or
        table[0][2] == table[1][2] == table[2][2]):
        a = True
        print("Column win")
    if (table[0][0] == table[1][1] == table[2][2] or
        table[2][0] == table[1][1] == table[0][2]):
        a = True
        print("Diagonal win")
    return a

for i in range(rows):
    print(table[i])

print('you are x')
while True:
    player=int(input('position : '))
    for i in range(rows):
        for j in range(col):
            if(table[i][j]==player):
                numbers.remove(player)
                table[i][j]='x'
    if correct():
        print('you are the winner')
        break
      
    cpu=random.choice(numbers)
    for i in range(rows):
        for j in range(col):
            if(table[i][j]==cpu):
                numbers.remove(cpu)
                table[i][j]='o'
    
    for i in range(rows):
        print(table[i])
    print('------------')

    if correct():
        print('cpu won the winner')
        break
if(correct()):
    print("thank you")
else:
    print('game tie')
