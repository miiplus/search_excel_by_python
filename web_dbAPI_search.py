import web_dbAPI_sub
import sys


#function 1: by search
#input = searchKey

iptSearch = sys.argv[1]    #receive php parameter#1

def fx_search (searchKey):
    dbNoList = web_dbAPI_sub.getDbNoList(searchKey)
    if len(dbNoList) == 0:
        return False
    
    webList = web_dbAPI_sub.getWebList(dbNoList)
    if len(webList) == 0:
        return False
    
    return webList


reList = fx_search(iptSearch)
if reList != False:
    print (reList)
else:
    print (0)


#print(reList)


"""
dbNoList = web_dbAPI_sub.getDbNoList(searchKey)
webList = web_dbAPI_sub.getWebList(dbNoList)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1
"""




"""
#function 2: by filters
#input = select filters
filterKeys = [['金融業','傳統產業'], [], ['100'], ['台50']]

dbNoListFsA = web_dbAPI_sub.dbNoListFs (filterKeys)
if len(dbNoListFsA) == 0:
    print ('SORRY, NO DATA')
webList = web_dbAPI_sub.getWebList(dbNoListFsA)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1
"""
