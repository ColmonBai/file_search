# -*- coding: utf-8 -*-

from docx import Document
import os
import re
import xlwt
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import json
import codecs

#读取pdf文件 返回整个字符串
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content
# 根据关键字查找
# 参数(文件名,关键字)
# 返回值 字典{关键词:次数}
def countByDocName(docName, keyWords):
   # print(docName)
    resultSet = {}
    for keyWord in keyWords:
        resultSet [keyWord] = 0
        #print(keyWord)
    # 验证docx文档
    if(re.search(".docx$",docName)):
        document = Document(docName)  #打开文件demo.docx
        counter = 0;
        for paragraph in document.paragraphs:
            for resultKey in resultSet.keys():
                resultSet[resultKey]+= paragraph.text.count(resultKey)
        return resultSet
    elif (re.search(".pdf$",docName)):
        pdfFile = open(docName, 'rb')
        outputString = readPDF(pdfFile)
        for resultKey in resultSet.keys():
            resultSet[resultKey]+= outputString.count(resultKey)
        return resultSet

# 根据目录查找
def countByDir(mydirs,keyWords):

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet 1')
    ws.write(0, 0, "文件名")
    ws.write(0, 1, "位置")
    counter = 2
    for keyWord in keyWords:
        ws.write(0, counter, keyWord )
        counter += 1

    yAxis = 1
    for dir in mydirs:
        for root, dirs, files in os.walk(dir):
            for file in files:
                abs_file = os.path.join(root, file)
                ws.write(yAxis, 0, file)
                ws.write(yAxis, 1, abs_file)

                resultDict = countByDocName(abs_file,keyWords)
                xAxis = 2
                for sum in resultDict.values():
                    ws.write(yAxis, xAxis, sum)
                    xAxis += 1
                yAxis += 1

    wb.save('统计结果.xls')

if __name__=="__main__":

    if (os.path.exists("统计结果.xls")):
        os.remove( "统计结果.xls")
    # myDirs = ["C:\\Users\\Administrator\\Desktop\\workspace\\cnki\\dir\\dir0"
    #         ,"C:\\Users\\Administrator\\Desktop\\workspace\\cnki\\dir\\dir1"
    #           ]
    # keyWords = ["风险", "跨境支付"]
    #
    # fw = open('search.config', 'w', encoding='utf-8')
    # counter = 0
    # for dir in myDirs:
    #     if (counter):
    #         fw.write(',')
    #     fw.write(str(dir))
    #     counter+=1
    # fw.write(';')
    # counter = 0
    # for keyWord in keyWords:
    #     if (counter):
    #         fw.write(',')
    #     fw.write(str(keyWord))
    #     counter +=1
    # fw.close()

    fr = open('search.config', 'r', encoding='utf-8')
    resultStr = fr.read()
    fr.close()
    #print (resultStr)
    resultSet = resultStr.split(';')
    #print(resultSet)
    myDirs = resultSet[0].split(',')
    #print (myDirs)
    keyWords = resultSet[1].split(',')
    countByDir(myDirs, keyWords)