import random
from tkinter.simpledialog import * 


def getString():
    result = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return result

def getRGB():
    r, g, b = random.random(), random.random(), random.random()
    result = (r, g, b)
    return result
    
def getXYAS(swidth, sheight):
    tX = random.randint(-swidth/2, swidth/2)
    tY = random.randint(-swidth/2, swidth/2)
    ang = random.randint(0,360)
    size = random.randint(30,50)
    
    return [tX,tY,ang,size]