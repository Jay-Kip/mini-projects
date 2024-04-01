# import QRcode from pyqrcode

import pyqrcode
import png
from pyqrcode import QRCode


#string which represent the QR code

s = "www.example.com"

# Generate QR code

url = pyqrcode.create(s)

#Create and savce the svg file naming "myqr.svg"

url.svg("myqr.svg", scale = 8)

# Create and save the png file namedf "myqr.png"

url.png(`myqr.png`, scale = 6)
