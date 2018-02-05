#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
from __future__ import print_function
from __future__ import unicode_literals
from io import open

def split_line2word(s):
    raw_list = s.strip().split()
    word_list = []
    biaodian = ["0", "1","2","3","4","5","6","7","8","9",\
                ".", "!", "?", ";",'"','*','-','~',',']

    for word in raw_list:
        # 从后检查非字母字符
        while True and len(word)>0:
            lastchar = word[-1]
            if lastchar in biaodian:
                word = word[0:len(word)-1]
            else:
                break
        # 从前检查非字母字符
        while True and len(word)>0: 
            firstchar = word[0] 
            if firstchar in biaodian:
                word = word[1:]
            else:
                break
        if len(word)==0:
            continue
        word_list.append(word.lower())

    return word_list

#@profile
def read_file(file_name):
    f=open(file_name,'rt')
    line_num = 0
    word_dict = {}
    while True:
        try:
            x=f.readline()
            line_num+=1
            
            if x=='' or line_num>100000:
                break
            
            word_list = split_line2word(x)

            # 统计单词出现次数
            for word in word_list:
                word_dict[word] = word_dict.get(word, 0) + 1
        except:
            print(line_num, x)
    f.close()
    print("文件行数：",line_num)
    
    #排序
    from future.utils import viewitems
    # 按字典的value对字典进行排序
    sorted_list = sorted(viewitems(word_dict),key=lambda x:x[1],reverse=True)  
    return sorted_list

if __name__ == '__main__':

    filename = 'day05/001.txt'
    print(filename)
    a = read_file(filename)
    
    print(a[:100])