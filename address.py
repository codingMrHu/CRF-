#coding:utf-8
import CRFPP
import os
tagger = CRFPP.Tagger('-m '+ os.path.join('data','address_model'))
def crf_segmenter(address_str):
    tags_list = []
    tagger.clear()
    for word in address_str:
        tagger.add(word.encode('utf-8'))
    tagger.parse()
    size = tagger.size()
    xsize = tagger.xsize()
    for i in range(0,size):
        for j in range(0,xsize):
            char = tagger.x(i, j).decode('utf-8')
            tag = tagger.y2(i)
            tags_list.append((char,tag))
    return tags_list


def gen_result(tags_list):
    tags = {}
    full = ''
    result = {}
    for cols in tags_list:
        c = cols[1].split('_')
        tag = c[1]
        if tag not in tags or c[0]=='B':
            tags[tag]=''
        tags[tag]+=cols[0]
        full+=cols[0]

    result['province'] = tags['province'] if 'province' in tags else ''
    result['city'] = tags['city'] if 'city' in tags else ''
    result['district'] = tags['district'] if 'district' in tags else ''
    result['street'] = tags['street'] if 'street' in tags else ''
    result['road'] = tags['road'] if 'road' in tags else ''
    result['roadnum'] =  tags['roadnum'] if 'roadnum' in tags else ''
    result['community'] = tags['community'] if 'community' in tags else ''
    result['building'] = tags['building'] if 'building' in tags else ''
    result['unit'] = tags['unit'] if 'unit' in tags else ''
    result['floor'] = tags['floor'] if 'floor' in tags else ''
    result['house'] = tags['house'] if 'house' in tags else ''

    return result
  

if __name__=="__main__":
    tags_list = crf_segmenter(u'成都市金牛区金房苑东路28号8栋1单元6楼2号')
    print gen_result(tags_list)