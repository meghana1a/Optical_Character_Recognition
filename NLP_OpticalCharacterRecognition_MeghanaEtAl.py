import easyocr
import PIL
from PIL import ImageDraw

reader=easyocr.Reader(['en','hi'], gpu=False) #languages: english (en), hindi (hi), tamil (ta)
path="h_hindi.jpg" #image name
img=PIL.Image.open(path)

result=reader.readtext(path)

print('\n\nTHE TEXT IN THIS IMAGE IS: \n')
for i in result:
    print(i[1], " - with accuracy ", i[2])
print("\n")

def underline(image, bounds, colour='green', width=5):
    draw=ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3=bound[0]
        draw.line([*p2,*p3], fill=colour, width=width)
    return image

underline(img,result)
img.save("output.jpg") #saving image with underlined word