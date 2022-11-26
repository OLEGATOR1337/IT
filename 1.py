import random
import time

#11111111111111111111111111111111111111111111111111111111111111111111111111#

tdata = []
def func():
    for i in range(1_000_000):
        tdata.append(random.randint(0, 999))
        
func()

#22222222222222222222222222222222222222222222222222222222222222222222222222#

hist = [0]*10  
def calcHist(tdata):
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


#33333333333333333333333333333333333333333333333333333333333333333333333333#

time_of_calc = []
def calcSumm(): 
    summ = 0
    while summ != 100:      
        summ += 1
        start = time.time()
        calcHist(tdata)
        end = time.time()
        time_of_calc.append(end - start)
        
calcSumm()

print("MAX Runtime of the calcSumm is ", max(time_of_calc))
print("MIN Runtime of the calcSumm is ", min(time_of_calc))
print("Runtime of the calcSumm is ", sum(time_of_calc) / 100)
print(time_of_calc)
