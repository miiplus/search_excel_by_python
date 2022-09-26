import web_dbAPI_sub
import sys

"""
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

"""
iptSearch = sys.argv[1]    #receive php parameter#1
print (iptSearch)



dbNoList = web_dbAPI_sub.getDbNoList(searchKey)
webList = web_dbAPI_sub.getWebList(dbNoList)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1
"""



#function 2: by filters
#input = select filters

iptFilter = sys.argv[1]    #receive php parameter#1
#iptFilter = '台50'    #over php parse limited: [['金融業', '百貨零售', '電子科技', '其它'], ['上市', '興櫃'], ['100'], ['台50']]
pyFKeyList = iptFilter.split(',')

filterKeys = [[],[],[],[]]
#filterKeys = [['金融業','傳統產業'], [], ['100'], ['台50']]
for i in range (0, len(pyFKeyList)):
    j = web_dbAPI_sub.getFKeyIndex (pyFKeyList[i])
    filterKeys[j].append(pyFKeyList[i])
    i+=1


dbNoListFsA = web_dbAPI_sub.dbNoListFs (filterKeys)
if len(dbNoListFsA) == 0:
    dbNoListFsA = False
webList = web_dbAPI_sub.getWebList(dbNoListFsA)
if len(webList) == 0:
    webList = False
print (webList)


"""
def fx_filter (filters):
    dbNoListFsA = web_dbAPI_sub.dbNoListFs (filters)
    if len(dbNoListFsA) == 0:
        return False
    
    webList = web_dbAPI_sub.getWebList(dbNoListFsA)
    if len(webList) == 0:
        return False
    
    return webList


reList = fx_filter(filterKeys)
if reList != False:
    print (reList)
else:
    print (0)
"""

"""
for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1
"""
