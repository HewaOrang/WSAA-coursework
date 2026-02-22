# This program reads an XML from URL and prints it out using minidom.
# Author: Hewa Orang

import requests
import csv
from xml.dom.minidom import parseString

retriveTags=['TrainStatus',
             'TrainLatitude',
             'TrainLongitude',
             'TrainCode',
             'TrainDate',
             'PublicMessage',
             'Direction',
             ]


url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
# print (doc.toprettyxml())

with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    objTrainPositiionNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionNode in objTrainPositiionNodes:
        traincodenode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        
        dataList = []
        for retrivetag in retriveTags:
            datanode = objTrainPositionNode.getElementsByTagName(retrivetag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)





