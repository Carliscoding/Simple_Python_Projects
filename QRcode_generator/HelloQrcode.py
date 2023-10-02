import qrcode

img = qrcode.make("Hello world!")

img.save("MaQR_basic.png")