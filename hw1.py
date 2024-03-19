import math

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius ** 2
    msg = f"{area}는 원의 넓이입니다."
    return msg

input_radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
result = get_circle_area(input_radius)
print(result)
print('원의 넓이 측정이 완료되었습니다.')
