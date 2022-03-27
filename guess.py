#猜錯的話 要告訴他 比答案大/小
#印出猜了幾次
#自行決定範圍

import random #載入module
start = input('請輸入範圍開始值: ')
end = input('請輸入範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r: 
		print('答對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
			print('比答案大')
	elif num < r:
			print('比答案小')
	print('這是你猜的第', count, '次')
 
