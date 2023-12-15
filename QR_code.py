# Importing the qrcode library and aliasing it as 'qr'
import qrcode as qr
# Generating a QR code using the make() function with a URL
img = qr.make ("http://rachitinfo.42web.io/index.html")

# Saving the generated QR code image as 'rachit_cv.png'
img.save("rachit_cv.png")