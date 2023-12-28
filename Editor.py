from PIL import Image, ImageEnhance, ImageFilter
import os
cwd = os.getcwd()
print(os.getcwd())
Edited = os.path.join(cwd + r"\Edited")
Images = os.path.join(cwd + r"\Images")

if os.path.isdir(Edited) != True:
    os.mkdir(Edited)
if os.path.isdir(Images) != True:
    os.mkdir(Images)

user = input("Smooth, Sharpen Or Blur [S, Sr, B] or Enhance Using Colour, Contrast or Sharpness [Cl, C, Sh] > ").upper()

for filename in os.listdir(Images):
    Img = Image.open(f"{Images}/{filename}")
    if user == "S":
        Edit = Img.filter(ImageFilter.SMOOTH)
    elif user == "SR":
        Edit = Img.filter(ImageFilter.SHARPEN)
    elif user == "B":
        Edit = Img.filter(ImageFilter.BLUR)
    elif user == "CL":
        factor = int(input("Factor (RECOMMENDED: 1.5)"))
        enhancer = ImageEnhance.Color(Img)
        Edit = enhancer.enhance(factor)
    elif user == "C":
        factor = int(input("Factor (RECOMMENDED: 1.5)"))
        enhancer = ImageEnhance.Contrast(Img)
        Edit = enhancer.enhance(factor)
    elif user == "SH":
        factor = int(input("Factor (RECOMMENDED: 1.5)"))
        enhancer = ImageEnhance.Sharpness(Img)
        Edit = enhancer.enhance(factor)
    else:
        print("Error")
        break
    CleanName = os.path.splitext(filename)[0]
    Edit.save(f"{Edited}/{CleanName}_Edited.jpg")