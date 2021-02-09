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

for p in products:
	print(p[0], '的價格是', p[1])

with open ('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		print(type(p))
		f.write(p[0] + ',' + p[1] + '\n')
#f.write(p[0] + ',' + p[1] + '\n')

