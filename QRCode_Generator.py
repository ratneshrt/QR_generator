import pyqrcode
import png
from pyqrcode import QRCode

s=str(input("Enter url here: "))
url=pyqrcode.create(s)
url.svg("myqrcode.svg",scale=8)
url.png("myqrcode.png",scale=6)