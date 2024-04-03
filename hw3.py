def get_fixed_price(discounted_price, discount_rate):
    discount_rate = discount_rate / 100
    fixed_price = discounted_price / (1 - discount_rate)
    return fixed_price


discount_rate = float(input("할인율은? "))

discounted_price_a = float(input("A상품의 할인된 가격은? "))
fixed_price_a = get_fixed_price(discounted_price_a, discount_rate)

discounted_price_b = float(input("B상품의 할인된 가격은? "))
fixed_price_b = get_fixed_price(discounted_price_b, discount_rate)

print(f"A상품의 정가는 {int(fixed_price_a)}원")
print(f"B상품의 정가는 {int(fixed_price_b)}원")