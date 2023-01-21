import pandas as pd
from xml.etree import ElementTree
from xml.dom import minidom
df = pd.read_excel(r'test.xlsx',header=0, usecols=[1,2,3,4], sheet_name="Sheet1")
route_root = ElementTree.Element('routes') # 根节点
for i in range(df.shape[0]):
    
    



    vehicle_element = ElementTree.SubElement(route_root, 'vehicle')
    vehicle_element.set('depart', str(df.iloc[i]['depart']))
    vehicle_element.set('id', str(df.iloc[i]['id']))
    vehicle_element.set('departLane', df.iloc[i]['departLane'])
    route_element = ElementTree.SubElement(vehicle_element, 'route', {'edges':str(df.iloc[i]['edges'])})
    print(i)
    xmlstr = minidom.parseString(ElementTree.tostring(route_root)).toprettyxml(indent="   ")
    xmlstr = '\n'.join([line for line in xmlstr.split('\n') if line.strip()]) # 去掉换行
    with open('test.rou.xml', "w", encoding='utf-8') as f:
        f.write(xmlstr)

