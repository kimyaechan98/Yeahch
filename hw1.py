import math

def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(반지름) :
    원의_넓이 = (3.14*반지름**2)
    return 원의_넓이
    
    
원의반지름 =get_radius('넓이를 구하고자 하는 원의 반지름은?')
result = get_circle_area(원의반지름)
print('반지름', 원의반지름, '인 원의 넓이 = 3.14 x ', 원의반지름, 'X', 원의반지름, '=' , result)
