import qrcode
import archiveis
import tldextract

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

data = input("What site would you like to archive?\n")
data_archived = archiveis.capture(data)

ext = tldextract.extract(data)
domain = ''.join(ext[:2])
filename = data.split('/')[-1]

qr.add_data(data_archived)
qr.make(fit=True)

img = qr.make_image()

img.save(domain + '.' + filename + '.jpg')