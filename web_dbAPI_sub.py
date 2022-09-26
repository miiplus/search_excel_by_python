from cmath import nan
import pandas

reptPath = 'C:\\SUROS_BI\\dbData_PN_220815A1\\'
excelFile = 'dbData_forAPI_220815.xlsx'
baseData = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,1,2,3,4,6,7,8,10])
reptList = pandas.read_excel(excelFile, sheet_name=1, usecols=[0,1,2,3,22])
baseHead = ['DB編號', '中文全名', '中文簡稱', '英文全名', '英文簡稱', '別名1', '別名2', '別名3', '股票簡稱']
reptHead = ['DB編號', '報告檔案夾', 'Date', 'pdfSummary', 'csvByVulnerability']

baseDataF = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,16,11,13,14])
baseHeadF = ['DB編號', '產業別', '上市櫃', '百大', '附註1']

cateListHtml = ['教育知識', '金融業', '政府機關', '能源環境', '醫藥業', '電網資訊', '傳統產業', '服務業', '百貨零售', '電子科技', '其它']
cateList = ['edu', 'fin', 'gov', 'life', 'medi', 'net', 'manu', 'serv', 'stor', 'tech', 'com']    #usecols = [16]
stockList = ['上市', '上櫃', '興櫃']    #usecols = [11]
rankList = ['100', '300']    #usecols = [13]
tw50 = ['台50']    #usecols = [14]
filterKeysCate = [cateListHtml, stockList, rankList, tw50]


#input search key word to get dbNoList
def getDbNoList (searchKey):
    dbNoList = []
    for j in range (1, 9):    #BaseData search columns length
        for i in range (0, 1903):    #BaseData search rows length
            cellValue = baseData[baseHead[j]].values[i]    #get cell value on columns by rows
            if searchKey.lower() in str(cellValue).lower():    #if cell contains search key
                dbNo = str(baseData[baseHead[0]].values[i]).strip()    #get dbNo
                if dbNo not in dbNoList:    #exclude same dbNo
                    dbNoList.append(dbNo)    #add new dbNo to list
            i+=1
        j+=1
    return dbNoList


#input dbNo List to get webList
def getWebList (dbNoList):
    countDbNo = len (dbNoList)
    webList = []
    for i in range (0, countDbNo):    #get web List by dbNoList orders
        for m in range (0, 1673):    #ReportList search rows length
            aList = []
            reptCell = reptList[reptHead[0]].values[m]    #get cell value on dbNo col by rows
            if str(dbNoList[i]).strip() in str(reptCell):    #if find match dbNo
                reptDate = reptList[reptHead[2]].values[m]    #get report date
                aList.append(reptDate)
                
                reptFolder = reptList[reptHead[1]].values[m].strip()    #get report dir
                reptPdf = reptList[reptHead[3]].values[m].strip()    #get pdf file name
                if reptPdf == 'no.pdf':
                    pdfPath = False
                else:
                    pdfPath = reptPath + reptFolder + '\\' + reptPdf    #get pdf path
                aList.append(pdfPath)
                
                reptCsv = reptList[reptHead[4]].values[m].strip()    #get csv file name
                if reptCsv == 'no.csv':
                    csvPath = False
                else:
                    csvPath = reptPath + reptFolder + '\\' + reptCsv    #get csv path
                aList.append(csvPath)
                
                for n in range (0, 1903):    #basedata search rows length
                    baseCell = str(baseData[baseHead[0]].values[n]).strip()    #get cell value on dbNo col by rows
                    if str(dbNoList[i]).strip() in str(baseCell):    #if find match dbNo
                        comFull = str(baseData[baseHead[1]].values[n]).strip()    #get comFull cell value
                        if comFull == 'nan':    #if no chinese full name
                            comFull = str(baseData[baseHead[4]].values[n]).strip()    #company = eng short name
                        aList.insert(0, comFull)
                        break
                    n+=1
                webList.append(aList)
            m+=1    
        i+=1    
    return webList


#get filter key category
def getFKeyCate (filterKey):
    for i in range (0, 4):
        if filterKey not in filterKeysCate[i]:
            i+=1
        else:
            fKeyCate = str(baseHeadF[i+1])
            if i == 0:
                p = cateListHtml.index(filterKey)
                filterKey = cateList[p]
            return fKeyCate, filterKey



#get filter key category type index
def getFKeyIndex (filterKey):
    for i in range (0, 4):
        if filterKey not in filterKeysCate[i]:
            i+=1
        else:
            return i





#get dbNoList by filtering single column
def getDbNoListF1 (filterKey):
    fKeyCate = getFKeyCate (filterKey)[0]
    filterKey = getFKeyCate (filterKey)[1]
    dbNoList = []
    for i in range (0, 1903):    #BaseData search rows length
        cellValue = str(baseDataF[fKeyCate].values[i]).strip()    #get cell value on columns by rows
        if filterKey in cellValue:    #if cell contains filter Key
            dbNo = str(baseDataF[baseHeadF[0]].values[i]).strip()    #get dbNo
            if dbNo not in dbNoList:    #exclude same dbNo
                dbNoList.append(dbNo)    #add new dbNo to list
        i+=1
    return dbNoList



#get dbNoList by multiple filters
def dbNoListFs (filterKeys):
    fKeysLenList = [len(filterKeys[0]), len(filterKeys[1]), len(filterKeys[2]), len(filterKeys[3])]
    dbNoListFsA = []
    for i in range (0, 4):    
        if fKeysLenList[i] == 0:
            i+=1
            continue
        if fKeysLenList[i] == 1:
            globals()['dbNoListFs'+str(i)] = getDbNoListF1(filterKeys[i][0])
            iListLen = len(globals()['dbNoListFs'+str(i)])
            aListLen = len(dbNoListFsA)
            if aListLen == 0:
                if iListLen == 0:
                    i+=1
                    continue
                dbNoListFsA = globals()['dbNoListFs'+str(i)]
                i+=1
                continue
            for a in range (0, aListLen):
                dbNo = dbNoListFsA[a]
                if dbNo not in globals()['dbNoListFs'+str(i)]:
                    dbNoListFsA[a] = 'x'
                a+=1
            while 'x' in dbNoListFsA:
                dbNoListFsA.remove('x')
            i+=1
            continue
        if fKeysLenList[i] > 1:
            for j in range (0, fKeysLenList[i]):
                if j == 0:
                    globals()['dbNoListFs'+str(i)] = getDbNoListF1(filterKeys[i][0])
                    j+=1
                    continue
                globals()['dbNoListFs'+str(i)+'-'+str(j)] = getDbNoListF1 (filterKeys[i][j])
                jListLen = len(globals()['dbNoListFs'+str(i)+'-'+str(j)])
                for m in range (0, jListLen):
                    dbNo = globals()['dbNoListFs'+str(i)+'-'+str(j)][m]
                    if dbNo not in globals()['dbNoListFs'+str(i)]:
                        globals()['dbNoListFs'+str(i)].append(dbNo)
                    m+=1
                j+=1
            iListLen = len(globals()['dbNoListFs'+str(i)])
            aListLen = len(dbNoListFsA)
            if aListLen == 0:
                if iListLen == 0:
                    i+=1
                    continue
                dbNoListFsA = globals()['dbNoListFs'+str(i)]
                i+=1
                continue
            for b in range (0, aListLen):
                dbNo = dbNoListFsA[b]
                if dbNo not in globals()['dbNoListFs'+str(i)]:
                    dbNoListFsA[b] = 'x'
                b+=1
            while 'x' in dbNoListFsA:
                dbNoListFsA.remove('x')
        i+=1
    return dbNoListFsA


