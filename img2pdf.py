import img2pdf

image = "ilona-frey-0UKyrKCoutM-unsplash.jpg"
output = "ilona-frey-0UKyrKCoutM-unsplash.pdf"

with open(output, "w+") as f:
    f.write(img2pdf.image)
