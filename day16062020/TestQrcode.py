import qrcode
img = qrcode.make('https://www.baidu.com')
with open('test.png','wb') as  f:
	img.save(f)