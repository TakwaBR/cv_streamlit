import qrcode

# ---- Replace this with your Streamlit link ----
url = "https://cvapp-wg4f6ifg7akwth4hykvkut.streamlit.app/"  

# Generate QR code
qr_img = qrcode.make(url)

# Save QR code
qr_img.save("qr_cv.png")

print("QR code generated and saved as qr_cv.png !")
