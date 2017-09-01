#!python3
# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hk_web.settings")

import django
django.setup()


from xml.etree import ElementTree as ET
from corpus.models import Lotus

def main():

    # 解析xml文件
    tree = ET.parse("LotusS6.xml")
    root = tree.getroot()
    
    pk_id = 0
    
    pk_of_code = {}
    # 遍历XML文档的第二层
    for child in root:
        # 第二层节点的标签属性
        my_dict = child.attrib

        # 遍历XML文档的第三层
        for i in child:
            # 第二层节点的标签名称和内容
            my_dict[i.tag] = i.text
            
        code = child.attrib["code"]
        pk_of_code[ code ] = pk_id
        pcode = "-".join( code.split("-")[:-1] )
        if pcode in pk_of_code:
            parent_id = pk_of_code[pcode]
        else:
            parent_id = -1
         
        Lotus.objects.create(
        ##print( dict(
            id = pk_id,
            level = child.attrib["level"],
            parent = parent_id,
            code = child.attrib["code"],
            sanskrit = my_dict["sanskrit"],
            sanskrit_eq = my_dict["sanskrit_eq"],
            tag = my_dict["tag"],
            chinese_explain = my_dict["chinese_explain"],
            note = my_dict["note"],
            d = my_dict["d"],
            k = my_dict["k"],
            dnote = my_dict["dnote"],
            knote = my_dict["knote"]
        )
        pk_id += 1

main()