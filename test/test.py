#coding=utf-8
import random
import time

from helper import ChinazHelpter


f = open("..\\name.txt", "r")
index = 1
for line in f:
    if index > 8837:
        print "%d : %s" % (index, line)
        entity = ChinazHelpter.get_search_single(line.strip())
        if entity is None:
            print "不存在列表"
        else:
            print entity.href

        sec = random.randint(1, 3)
        time.sleep(sec)
    index += 1

f.close()

# entity = ChinazHelpter.get_search_single("汽车")
# print entity.href


