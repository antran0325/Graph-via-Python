#Ann Tran
import xml.etree.ElementTree as ET
import csv


tree = ET.parse("simmons_programming_books.xml")
root = tree.getroot()
children = root.getchildren()
count_doctype = open('CountType.csv', 'w')
docwriter = csv.writer(count_doctype)
doc = []
countD = dict()

#find the subject
for child in tree.findall(".//doctype"):
        doc.append(child.text)
#print(doc)

#count and add to dictionary 
for item in doc:
        if item in countD:
                countD[item] = countD[item] + 1
        else:
                countD[item] = 1
for key in list(countD.keys()):
    print(key, ":", countD[key])
    docwriter.writerow([key,str(countD[key])])
    
count_doctype.close()
