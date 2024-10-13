#pip install "qrcode[pil]"
import qrcode as qr
img = qr.make("https://www.youtube.com/@ankitasingh-ot3gz")
img.save("ankita_youtube.png")

