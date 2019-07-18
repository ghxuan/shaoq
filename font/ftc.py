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
    def __init__(self, font='shaoq.woff'):
        self.img_font = ImageFont.truetype(font, 60)
        self.fill_color = "#000000"
        self.font = TTFont('shaoq.woff')
        self.keys = list(key for key in self.font['glyf'].keys() if key.startswith('uni'))
        self.ocr = CnOcr()
        if not os.path.isdir('jpg'):
            os.mkdir('jpg')
        pass

    def make_all_font_img(self):
        img = Image.new('RGB', (70 * len(self.keys), 80), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), ''.join(chr(int(f'0x{key.strip("uni")}', 16)) for key in self.keys),
                  font=self.img_font, fill=self.fill_color)
        # img.show()
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
        return dict(zip(self.keys, res[0]))


def main():
    o = FTC()
    o.ret_key_font()


if __name__ == '__main__':
    main()
    # ocr = CnOcr()
    # res = ocr.ocr('jpg/1.jpg')
    # print(res)
    # print(int('0xe41b', 16))
    pass
