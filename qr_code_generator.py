import qrcode
import os

data = input('Enter the text or URL: ').strip()

filename = input(' Enter the filename: ').strip()
if not filename:
    filename = "qrcode.png"
elif not filename.lower().endswith(".png"):
    filename += ".png"

fill = input('Enter fill color (default black): ').strip() or "black"
back = input('Enter background color (default white): ').strip() or "white"

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color=fill, back_color=back)

image.save(filename)
print(f'✅ QR code saved as {filename}')

try:
    os.startfile(filename)  
except AttributeError:
    try:
        os.system(f'open "{filename}"')  
    except:
        os.system(f'xdg-open "{filename}"')  
