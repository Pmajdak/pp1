current_price = 140
previous_price = 200

price_reduce = abs(100 * (previous_price-current_price)/previous_price)


print(f'Current product price: {current_price}')
print(f'Previous product price: {previous_price}')

if price_reduce >= 10:
    print("Buy the product!!")


print(f'Product price reduced by {price_reduce}%')