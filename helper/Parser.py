import xml.etree.ElementTree as ET
import html
import numpy as np
import pandas as pd
import re
import sys

namePostFile = 'Posts.xml' #sys.argv[1]
# nameExportQuestions = sys.argv[2]
# nameExportAnswer = sys.argv[3]

# if namePostFile == "" or nameExportQuestions == "" or nameExportAnswer == "" :
#     print('stkparser.py <Post.xml> <QuestionsOutput> <AnswerOutput>')
#     sys.exit(2)

def cleanfile(fileName):
    f = open(fileName, 'w')
    f.close()

# def write(question, answer):
#     with open(nameExportQuestions, 'a') as q:
#         q.write(question)
#         q.write("\n")
#     with open(nameExportAnswer, 'a') as q:
#         q.write(answer)
#         q.write("\n")

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext



def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    all_records_complete = []
    answers = {}
    size = len(root)
    for i, child in enumerate(root):
        record = {}
        print("\rLines of Post.xml :: [{0}/{1}] => {2}%".format(i, size,np.around((i * 100) / size) ))
        if child.attrib["PostTypeId"] == "1" and "AcceptedAnswerId" in child.attrib.keys() :
            record["ID"] = child.attrib["Id"]
            record["QUESTION"] = cleanhtml(html.unescape(child.attrib["Body"])).replace('\n', ' ')
            all_records.append(record)
        if child.attrib["PostTypeId"] == "2" :
            answers[child.attrib["ParentId"]] = cleanhtml(html.unescape(child.attrib["Body"])).replace('\n', ' ')
    size = len(all_records)
    print("")
    for i, item in enumerate(all_records):
        print("\rProcessing questions :: [{0}/{1}] => {2}%".format(i, size,np.around((i * 100) / size) ))
        if item["ID"] in answers.keys():
            record = {}
            record["QUESTION"] = item["QUESTION"]
            record["ANSWER"] = answers[item["ID"]]
            all_records_complete.append(record)
    print("")
    return pd.DataFrame(all_records_complete)

# print("Cleanning export files")
# cleanfile(nameExportQuestions)
# cleanfile(nameExportAnswer)
print("Loading Post.xml file")
xml_data = open(namePostFile).read()
data = xml2df(xml_data)

size = len(data)
for item in data.itertuples():
    print("\rLines writes in files :: [{0}/{1}] => {2}%".format(item[0], size,np.around((item[0] * 100) / size) ))
    # write(item[1],item[2])

print("\nFinish script - Final number of Question/Answer is {0}".format(size))