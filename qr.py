import qrcode

img = qrcode.make("https://habiba5205.github.io/My_Card/")
img.save("my_qr.png")