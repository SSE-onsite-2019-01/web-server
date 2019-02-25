#!/usr/bin/env python3
import csv

print ("Content-type: text/html\n\n")
print ("")
f = open('/home/ubuntu/value.csv', 'r')
dataReader = csv.reader(f)
i = 0
for row in dataReader :
    if (i == 1) :
        print(str(row))
    i = i + 1
f.close()
print(u'あ')
