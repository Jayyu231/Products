products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': 
    	break
    price = input('請輸入商品價格: ')
    #1 p = []
    #1 p.append(name)
    #1 p.append(price)
    #2 p = [name, price]
    products.append([name, price]) #3 
print(products)
