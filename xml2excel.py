

import pandas as pd
import numpy as np
# 创建一个3行四列的DataFrame数组, 并指定DataFrame的行索引和列索引
d1 = pd.DataFrame(columns=["depart","departLane","id","edges"])



from xml.etree import ElementTree as ET

tree = ET.parse("map.rou.xml")
i=0
for children in tree.iter():
    d=[]
    if children.tag == 'vehicle':
        d.append(children.attrib['depart'])
        d.append(children.attrib['departLane'])
        d.append(children.attrib['id'])
        for child in children:
            if child.tag == 'route':
                d.append(child.attrib['edges'])
                
                d1.loc[i]=d
                i=i+1
            




d1.to_excel("test.xlsx",sheet_name="Sheet1",na_rep="",float_format=None,columns=None,header=True,index=True,index_label=None,startrow=0,startcol=0,engine=None,merge_cells=True,encoding=None,inf_rep="inf",verbose=True,freeze_panes=None)
