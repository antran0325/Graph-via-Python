#Ann Tran
import xml.etree.ElementTree as ET
import csv


tree = ET.parse("simmons_programming_books.xml")
root = tree.getroot()
children = root.getchildren()
countP = dict()
countS = dict()
# open a file for writing

count_book = open('CountBook.csv', 'w')
count_header = open('CountHeader.csv', 'w')

# create the csv writer object

yearwriter = csv.writer(count_book)
headerwriter = csv.writer(count_header)
year = []
sub = []

#find the year
for child in children:
        dt = child[0][0][2][0]
        publish = dt.attrib['year']
        year.append(str(publish))
        
#count and add to dictionary 
for item in year:
        if item in countP:
                countP[item] = countP[item] + 1
        else:
                countP[item] = 1
for key in list(countP.keys()):
    #print(key, ":", countP[key])
    yearwriter.writerow([key,str(countP[key])])

#find the subject
for child in tree.findall(".//subj"):
        sub.append(child.text)
#print(sub)

#count and add to dictionary 
for item in sub:
        if item in countS:
                countS[item] = countS[item] + 1
        else:
                countS[item] = 1
for key in list(countS.keys()):
    print(key, ":", countS[key])
    headerwriter.writerow([key,str(countS[key])])

count_header.close()
count_book.close()
