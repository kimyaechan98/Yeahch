def get_integer(prompt) :
    res = int(input(prompt))
    return res;

def set_all_bits(n) :
    return(1 << n) - 1

n = get_integer('설정할 비트 수는? ')
b = set_all_bits(n)

print(n, '비트를 모두 1로 설정한 수는' , b, '(', bin(b), ') 이다.')