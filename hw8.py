shopping_bag = {}

while True:
    print('[구입]')
    item = input('상품명? ')
    
    if len(item) == 0:
        break
    else:
        howmany = int(input('수량은? '))  
        shopping_bag[item] = howmany
        print(f'장바구니에 {item} {howmany}개가 담겼습니다.')
        print()
print()
print(f'>>>장바구니 보기 : {shopping_bag}')
print()

print('[검색]')
product_name = input('장바구니에서 확인하고자 하는 상품은? ')
if product_name in shopping_bag:
    print(f'{product_name}은(는) {shopping_bag[product_name]}개 담겨 있습니다.')
else:
    print(f'{product_name}은(는) 장바구니에 없습니다.')