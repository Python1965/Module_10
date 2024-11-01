
'''Практика №1'''
# Практика

# from datetime import datetime
# from PIL import Image
# import microprocessing as mp


#
# def resize_image(image_path, queue):
#     for image_path in image_path:
#         image = image.open(image_path)
#     resize_image = mp.Process(target = resize_image, args = data, queue)
#     change_process = mp.Process(target = change_color,args = data, )
#         image = image.resize(800, 600)
#         queue.put(image_path, image)
# def change_color(queue):
#     while True:
#         try:
#             image_path, image = queue.get(timeout = 5)
#         except Empty:
#             break
#         image = queue.get
#         image = image.convert(дл'L')
#         image.save(image_path)
#
#
# if __name__ == '__main__':
#     data = []
#     queue == mp.Queue()
#     for image in range(1, 201):
#         data.append(f'./image/img_.{image}.jpg')
# start = datetime.now
#
# resize_image = mp.Process(resize_image, data, queue)
# change_process = mp.Process(change_color, data, )
# resize_process start()
# change_process start()
# resize_process join()
# change_process join()
#
#
# end = datetime.now
# print(end - start)

'''Практика №1'''
from threading import Thread
import random
import queue
import time


class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()
    def run(self):
        while True:
            time.sleep(random.randint(1, 4))
            if random.random() > 0.9:
                self.queue.put('подгорелая булка')
            else:
                self.queue.put('нормальная булка')


class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()
    def run (self):
        print(self.queue.qsize())
        while self.count:
            bulka = self.queue.get(timeout = 6)
            if bulka == 'нормальная булка':
                time.sleep(random.randint(1, 3))
                self.count -= 1
            print('булок к приготовлению осталось', self.count)
queue = queue.Queue(maxsize = 8)

t1 = Bulka(queue)
t2 = Kotleta(queue,7)

t1.start()
t2.start()

t1.join()
t2.join()