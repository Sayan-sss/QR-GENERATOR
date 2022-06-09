import qrcode
import image
qr = qrcode.QRCode(
    version=15,  # 15 means the qrcode is 15*15
    box_size=10,  # size of the box where the qrcode is drawn
    border=5  # border around the qrcode, the white space around the qrcode
)

# data to be encoded in the qrcode
data = "https://www.linkedin.com/in/sayan-mondal-10a734221/"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
