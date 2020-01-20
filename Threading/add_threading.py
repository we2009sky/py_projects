# encoding=utf8
import time
import threading


def sorry():
    print('I am sorry')


class Mythreading(threading.Thread):

    # 继承一定要重写run方法
    def run(self):
        for i in range(5):
            msg = '我是' + self.name + str(i)
            print(msg)

if __name__ == '__main__':
    tt = Mythreading()
    tt.start()