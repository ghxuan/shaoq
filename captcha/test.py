from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

target = Image.new('RGB', (160, 120))
image = ImageCaptcha()
captcha_image1 = Image.open(image.generate('dasf'))
captcha_image2 = captcha_image1.copy()
captcha_image2 = captcha_image2.convert('L')
captcha_image2 = captcha_image2.point(lambda x: 1 if x > 176 else 0)
target.paste(captcha_image1, (0, 0, 160, 60))
target.paste(captcha_image2, (0, 60, 160, 120))
target.show()
