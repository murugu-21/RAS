from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from num2words import num2words as nw
from datetime import date
def generate_check(to, price, filename):
    fontsize = 16
    font = ImageFont.truetype("arial.ttf", fontsize)
    today = date.today()
    d = today.strftime("%d")
    m = today.strftime("%m")
    y = today.strftime("%Y")
    price_word = nw(price).replace(",", "") + " only"
    acc_no = "1234567890"
    path = (
        Path.home()
        / "cheque.jpg"
    )
    sign_path = (
        Path.home()
        / "signature.jpg"
    )
    img = Image.open(path)
    d1 = ImageDraw.Draw(img)
    d1.text((488, 18), d[0], fill=(0,0,0))
    d1.text((503, 18), d[1], fill=(0,0,0))
    d1.text((518, 18), m[0], fill=(0,0,0))
    d1.text((533, 18), m[1], fill=(0,0,0))
    d1.text((548, 18), y[0], fill=(0,0,0))
    d1.text((563, 18), y[1], fill=(0,0,0))
    d1.text((578, 18), y[2], fill=(0,0,0))
    d1.text((593, 18), y[3], fill=(0,0,0))
    d1.text((100,52), to, font = font, fill=(0,0,0))
    d1.text((100,79), price_word, font = font, fill=(0,0,0))
    d1.text((80,136), acc_no, font = font, fill=(0,0,0))
    d1.text((500, 102), str(price),  font = font, fill =(0, 0, 0))
    signature = Image.open(sign_path)
    img.paste(signature, (450, 170))
    img.show()
    img.save(filename)