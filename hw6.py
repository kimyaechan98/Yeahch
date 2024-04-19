def display_multiplication_table(n) :
    for i in range(1, 10) :
        print(f'{n} x {i} = {n*i}',end = ' ') ,
        print(f'{n+1} x {i} = {(n+1)*i}',end = ' ')
        print(f'{n+2} x {i} = {(n+2)*i}',end = ' ')
        print(f'{n+3} x {i} = {(n+3)*i}')
        
        i = 1
        
for n in range(2, 3) :
    display_multiplication_table(n)
print()
for n in range(6, 7) :
    display_multiplication_table(n)
print()



