import finalCsvSearch2
import numpy
import time
from math import floor
import csv


start = time.time()

#gold oil wheat iron

with open("GoldCsv.csv", 'r') as f:
    r1 = list(csv.reader(f, delimiter=","))
r1 = numpy.array(r1, dtype=numpy.int)

with open("OilCsv.csv", 'r') as f:
    r2 = list(csv.reader(f, delimiter=","))
r2 = numpy.array(r2, dtype=numpy.int)

with open("WheatCsv.csv", 'r') as f:
    r3 = list(csv.reader(f, delimiter=","))
r3 = numpy.array(r3, dtype=numpy.int)

with open("IronCsv.csv", 'r') as f:
    r4 = list(csv.reader(f, delimiter=","))
r4 = numpy.array(r4, dtype=numpy.int)

#r1 = numpy.genfromtxt('CsvExample1.csv', delimiter=',')
#r2 = numpy.genfromtxt('CsvExample2.csv', delimiter=',')
#r3 = numpy.genfromtxt('CsvExample3.csv', delimiter=',')
#r4 = numpy.genfromtxt('CsvExample4.csv', delimiter=',')

#end = time.time()
#print("CSV Load = %s" % (end - start))

#--------#

#start = time.time()

res = finalCsvSearch2.fastcomb(r1, r2,r3,r4)

#end = time.time()
#print("Table Generation = %s" % (end - start))
#---------#

#start = time.time()

#print(res[0][0])

res = numpy.delete(res,numpy.s_[-9:],1)
res = numpy.delete(res,numpy.s_[-9:],0)

resIndx = numpy.argpartition(res,-50,axis=None)
resIndx = resIndx[-50:]
resIndx = numpy.sort(resIndx)

for val in resIndx:
    x= val%991
    y= floor(val/991)
    print(str(x+1)+":"+str(y+1) +" = "+str(res[y][x]))

end = time.time()
print("Finished = %s" % (end - start))
#------------#