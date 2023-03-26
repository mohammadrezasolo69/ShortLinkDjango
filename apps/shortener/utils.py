import random
import string
import qrcode


def generate_short_url(length: int = 10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_QR_code(name: str):
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(name)
    qr.make(fit=True)

    # Convert the QR code to an image
    return qr.make_image(fill_color="black", back_color="white")
