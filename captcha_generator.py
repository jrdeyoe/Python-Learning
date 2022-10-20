from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha(width=300, height=100)

txt = input("Enter your Captcha Text: ")
data = image.generate(txt)

image.write(txt, "output.png")
Image.open("output.png")
