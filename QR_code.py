import qrcode as qr

# Taking user input for the URL
url = input("Enter the URL for the QR code: ")

# Generating a QR code using the make() function with the user-provided URL
img = qr.make(url)

# Saving the generated QR code image as 'user_qr_code.png'
img.save("user_qr_code.png")
