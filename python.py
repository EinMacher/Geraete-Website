import qrcode, csv
with open('geraete.csv') as f:
    for row in csv.DictReader(f):
        url = f"https://uni-domain.de/geraet.html?id={row['ID']}"
        img = qrcode.make(url)
        img.save(f"etiketten/{row['ID']}.png")
