from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import numpy as np
import random

import string

characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
print(characters)

width, height, n_len, n_class = 170, 80, 4, len(characters)


# generator = ImageCaptcha(width=width, height=height)
# random_str = ''.join([random.choice(characters) for j in range(4)])
# img = generator.generate_image(random_str)
#
# plt.imshow(img)
# plt.title(random_str)

def gen(batch_size=32):
    X = np.zeros((batch_size, height, width, 3), dtype=np.uint8)
    y = [np.zeros((batch_size, n_class), dtype=np.uint8) for i in range(n_len)]
    generator = ImageCaptcha(width=width, height=height)
    while True:
        for i in range(batch_size):
            random_str = ''.join([random.choice(characters) for j in range(4)])
            print(random_str)
            X[i] = generator.generate_image(random_str)
            for j, ch in enumerate(random_str):
                y[j][i, :] = 0
                y[j][i, characters.find(ch)] = 1
        yield X, y


def decode(y):
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])


X, y = next(gen(1))
# print(X, y)
print('real: %s\npred:%s' % (decode(y), 1))
plt.title('real: %s\npred:%s' % (decode(y), 1))
plt.imshow(X[0], cmap='gray')
