# coding=utf-8
import httplib2
from BeautifulSoup import BeautifulSoup
from data.ChinaEntity import ChinaEntity


def get_search_single(keyword):
    entity = ChinaEntity()
    url = "http://search.top.chinaz.com/Search.aspx?url=" + keyword
    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    soup = BeautifulSoup(content)
    class_text = soup.find(attrs={"id": "ltArealist"})
    if class_text is None:
        return None
    text_first = class_text.contents[0]
    left_img = text_first.img["src"]
    list_title = text_first.findAll(attrs={"class": "SeaCentTxt"})
    title = list_title[0].a["title"]
    href = list_title[0].a["href"]
    introduce = text_first.findAll("p", attrs={"class": "RtCInfo"})[0].string
    entity.left_img = left_img
    entity.title = title
    entity.href = href
    entity.introduce = introduce
    get_detail(entity=entity)
    return entity


def get_detail(entity):
    url = entity.href
    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    soup = BeautifulSoup(content)
    ele_star = soup.find("p", attrs={"class": "pstar fl"}).img["src"]
    ele_point = soup.findAll("p", attrs={"class": "headpoint"})

    for index in range(3):
        try:
            rank = ele_point[index].a.string
        except Exception:
            rank = "0"
        if (index == 0):
            rank_all = rank
        elif (index == 1):
            rank_area = rank
        else:
            rank_net = rank

    star = get_rank(ele_star)
    ele_info = soup.findAll("div", attrs={"class": "Tagone TopMainTag-show"})[0]
    list_info = ele_info.findAll("p")
    info_type, info_area = "", ""
    for t in list_info[0].findAll("a"):
        info_type += " " + t.string

    for t in list_info[1].findAll("a"):
        info_area += " " + t.string

    entity.star = star
    entity.rank_all = rank_all
    entity.rank_area = rank_area
    entity.rank_net = rank_net
    entity.type = info_type
    entity.area = info_area


def get_rank(text):
    text_test = text
    p_start = text.rindex("_")
    p_end = text.rindex(".")
    return text_test[p_start + 1: p_end]




