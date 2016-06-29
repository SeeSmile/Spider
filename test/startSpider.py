#coding=utf-8
import random
import time

from helper import ChinazHelpter

url_first = "http://top.chinaz.com/hangye/"
url_page = "http://top.chinaz.com/hangye/index_"


def get_list_from_file():
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


def get_list_rank():
    for index in range(1, 1708):
        url = ""
        if index == 1:
            url = url_first
        else:
            url = url_page + str(index) + ".html"
        print url

get_list_rank()


# entity = ChinazHelpter.get_search_single("汽车")
# print entity.href


