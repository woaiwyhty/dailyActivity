from PIL import Image
import random
from random import randint
import time
import os

class imageGenerate:
    __L = []
    def __init__(self, file_dir):
        self.__L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                self.__L.append(file)

    def removeFile(self, path):
        if os.path.exists(path):
            os.remove(path)
    def process_profile(self):
        # open a profile picture from path
        # todo: check invalidate path
        name = random.choice(self.__L)
        picture_path = './profilephoto/' + name

        img_a = Image.open('./profilephoto/' + name)
        img_a = img_a.convert('RGBA')

        size = img_a.size
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255), 1)
        img_b = Image.new('RGBA', size, random_color)

        img = Image.blend(img_a, img_b, 0.2)
        # img.show()

        new_path = 'generated_profile/' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + str(random.randint(1000, 10000)) + '.png'
        img.save(new_path)
        return new_path


# m_gen = imageGenerate('profilephoto')
#
# print(os.path.abspath(m_gen.process_profile()))