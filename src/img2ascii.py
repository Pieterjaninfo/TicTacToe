import cv2
import numpy as np
import itertools


def get_gray_image(path):
    img = cv2.imread(path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img


def get_ascii(img):
    result = ''
    for i, j in itertools.product(range(0, len(img)), range(0, len(img[0]))):
        x = img[i, j]
        if 0 <= x < 100:
            result += '0'
        elif 100 <= x < 150:
            result += '#'
        elif 150 <= x < 200:
            result += '1'
        else:
            result += ' '
        if j == len(img[0]) - 1:
            result += '\n'
    return result


def write_img(data):
    with open('../resources/textfiles/queery.txt', 'w') as text_file:
        text_file.write(data)


img = get_ascii(get_gray_image('../resources/images/query.png'))
write_img(img)

print('Done writing.')
