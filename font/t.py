import os
import pytesseract
from cnocr import CnOcr
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import string

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


class OCR(object):
    def __init__(self, font='shaoq.woff'):
        self.img = Image.new('RGB', (70, 70), color='white')
        self.img_font = ImageFont.truetype(font, 60)
        self.fill_color = "#000000"
        if not os.path.isdir('jpg'):
            os.mkdir('jpg')
        pass

    def make_img(self):
        img = self.img.copy()
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), chr(0xe41b), font=self.img_font, fill=self.fill_color)
        img.show()
        # img.save('jpg/efeb.jpg')
        # print(pytesseract.image_to_string(img, lang='chi_sim'))
        pass


def main():
    o = OCR()
    o.make_img()


if __name__ == '__main__':
    main()
    # ocr = CnOcr()
    # print(dir(ocr))
    pass
