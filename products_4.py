import os

products = []
#讀取檔案 
if os.path.isfile('products.csv'): #先確認檔案在不在?
	print('Yeah! 找到檔案了!')
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品, 價格' in line:
				continue #繼續下一回,跳掉下面兩行
			name, price= line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: 跳出請按q ')
	if name == 'q': 
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price]) #3 
print(products)

#印所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open ('products.csv', 'w') as f:
		f.write('商品, 價格\n')
	
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


