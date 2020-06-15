import qrcode
img = qrcode.make('Hello')
with open('Qrcode.png','wb') as f:
	img.save(f)
