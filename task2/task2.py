import random

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#

def triangle(a):
    for i in range(a+1):
        print(' ' * (a - i), '*' * (2 * i + 1), sep='')

a = 3
triangle(a)        


#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222#
     
def calcHist():
    tdata = []
    
    for i in range(1_000_000):
        tdata.append(random.randint(0, 999))
    
    hist = [0]*10
    
    for i in tdata:
        if i in range(0, 100):
            hist[0] += 1
        if i in range(100, 200):
            hist[1] += 1
        if i in range(200, 300):
            hist[2] += 1
        if i in range(300, 400):
            hist[3] += 1
        if i in range(400, 500):
            hist[4] += 1
        if i in range(500, 600):
            hist[5] += 1
        if i in range(600, 700):
            hist[6] += 1
        if i in range(700, 800):
            hist[7] += 1
        if i in range(800, 900):
            hist[8] += 1
        if i in range(900, 1000):
            hist[9] += 1
    return hist


hist1 = calcHist()
hist2 = calcHist()


def histDistanse(hist1, hist2)->float:
    s = 0
    for i in range(len(hist1)):
        s += ((hist1[i] - hist2[i]) ** 2)
    return s ** 0.5 

print(histDistanse(hist1, hist2))


#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#


def hists_to_file():
    with open('hists.txt', 'w', encoding='utf-8') as fwrite:
        print(hist1, file=fwrite)
        print(hist2, file=fwrite)
    
hists_to_file()


#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444#


def hists_in_file():
    with open('hists.txt', 'r', encoding='utf-8') as fread:
        print(fread.read())
    
hists_in_file()






