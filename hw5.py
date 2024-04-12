def read_single_digit(kor):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits[kor]

def read_number(n):
    if 100 <= n <= 999:
        hundred = n // 100
        ten = (n % 100) // 10
        one = n % 10
        return ' '.join([read_single_digit(hundred), read_single_digit(ten), read_single_digit(one)])

num = int(input("세 자리 정수 입력: "))
result = read_number(num)
print(result)