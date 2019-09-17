import random

class Generator(object):
    def generate_carno(self):
        '''生成随机车牌'''
        carno = "粤ZD"+str(random.randint(1000, 9999))
        print(carno)
        return carno


if __name__=="__main__":
    a =Generator()
    b = a.generate_carno()