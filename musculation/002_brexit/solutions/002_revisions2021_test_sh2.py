def drapeau (T):
    y = 0
    #print(T)
    #print('|',(T-1)*'X',y*'X','|')
    while T >0:
        print('|'+y*'X',(T-1)*'X'+' '+(T-1)*'X',y*'X'+'|') #haut du drapeau
        #print('|',y*'X',(T-1)*'X',' ',(T-1)*'X',y*'X','|') #haut du drapeau avec espace avant le pipe --KO
        T-=1
        y+=1
    #print('T=',T)
    #print('y=',y)
    print('|'+2*y*' '+' '+'|') #milieu du drapeau
  
    while y>0:
        print('|'+(y-1)*'X',(T)*'X'+' '+(T)*'X',(y-1)*'X'+'|') #bas du drapeau
        T+=1
        y-=1


print('------ test drapeau 10')
        
drapeau(10)
print('------ test drapeau 2')

drapeau(2)
print('----- test drapeau 1')

drapeau(1)
"""
print('test drapeau 1')
drapeau(0)
print('test drapeau 0')


drapeau (11)
"""