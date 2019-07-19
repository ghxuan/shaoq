import os
from cnocr import CnOcr
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import string


# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# pytesseract.image_to_string(img, lang='chi_sim')


class FTC(object):
    # font_to_chinese
    def __init__(self, font='HYZiKuTangChangLinTiW-2.ttf'):
        self.img_font = ImageFont.truetype(font, 60)
        self.fill_color = "#000000"
        self.ocr = CnOcr()
        if not os.path.isdir('jpg'):
            os.mkdir('jpg')
        pass

    def make_all_font_img(self):
        img = Image.new('RGB', (70 * 20, 80), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), u'abcdefghigklmnopqrstuvwxyz', font=self.img_font, fill=self.fill_color)
        img.show()
        img.save('jpg/1.jpg')

    def make_img(self):
        img = Image.new('RGB', (140, 80), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), chr(0xe41b), font=self.img_font, fill=self.fill_color)
        # img.show()
        # img.save('jpg/1.jpg')
        # print(pytesseract.image_to_string(img, lang='chi_sim'))
        pass

    def ret_key_font(self):
        self.make_all_font_img()
        res = self.ocr.ocr('jpg/1.jpg')
        return res


def main():
    o = FTC()
    res = o.ret_key_font()
    print(res)


if __name__ == '__main__':
    main()
    # ocr = CnOcr()
    # res = ocr.ocr('jpg/1.jpg')
    # print(res)
    # print(int('0xe41b', 16))
    pass
