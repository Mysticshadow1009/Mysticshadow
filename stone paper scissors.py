print('+----------ROCK PAPER STONE------------+')

import random
playing=True
c,p=0,0
n=int(input('no of round : '))
for i in range(n):
    while playing:
        player=input('enter [r,p,s] : ')
        cpu=random.choice(['r','p','s'])
        if (player=='r' and cpu=='s' or
                player=='s' and cpu=='p' or
                player=='p' and cpu=='r'):
            p+=1
            print('point for player')
            break
        elif (player=='s' and cpu=='r' or
                player=='p' and cpu=='s' or
                player=='r' and cpu=='p'):
                c+=1
                print('point for cpu')
                break
        elif(player==cpu):
                print('draw for both')
                break
        else:
                print('your input is wrong')
                break
if(p>c):
      print(f"player won {p} and cpu won {c}")
      print('player won the league')
elif(p<c):
      print(f"player won {p} and cpu won {c}")
      print('cpu won the league')
elif(p==c):
      print(f"player won {p} and cpu won {c}")
      print('league is tie')
else:
      print('something went wrong')
