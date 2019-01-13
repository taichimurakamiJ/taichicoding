# -*- coding: utf-8 -*-
import csv
def egg():
    file = open('a.py', encoding='utf-8')
    spam = file.read()
    elem=spam.split()
    

    spam_file = input('ファイル名を入力してください>>>')
    spam_file = open(spam_file, encoding='utf-8')
    bacon=spam_file.read()
    bacons=str(bacon)
    ham=bacons.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace(',','')
    hams=ham.split()

    result = []
    for item in elem:
        for target in hams:
            if item==target:
                result.append(item)
    
    name=input('学校名を入力してください>>>')


    with open('highschoolword.csv','a',encoding='UTF-8') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([name,result])
            

    csvFile.close()

    file2=open('ed.py',encoding='utf-8')
    edms=file2.read()
    edm=edms.split()

    result2=[]
    for house in edm:
        for target in hams:
            if house==target:
                result2.append(house)

    name=input('学校名を入力してください>>>')


    with open('schooledword.csv','a',encoding='UTF-8') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([name,result2])

    csvFile.close()

    file3=open('ec.py',encoding='utf-8')
    basses=file3.read()
    bass=basses.split()

    result3=[]
    for trap in bass:
        for target in hams:
            if trap==target:
                result3.append(trap)
    
    name=input('学校名を入力してください>>>')


    with open('schoolecword.csv','a',encoding='UTF-8') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([name,result3])

    csvFile.close()

    file4=open('sports.py',encoding='utf-8')
    houses=file4.read()
    future=houses.split()

    result4=[]
    for progressive in future:
        for target in hams:
            if progressive==target:
                result4.append(progressive)
    
    name=input('学校名を入力してください>>>')


    with open('schoolspword.csv','a',encoding='UTF-8') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([name,result4])

    csvFile.close()
                



    
    
egg()
            


