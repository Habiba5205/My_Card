import qrcode

img = qrcode.make("https://github.com/Habiba5205/My_Card")
img.save("my_qr.png")