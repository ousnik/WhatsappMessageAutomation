import pyodbc
import os
def getLists(day):
    cwd=os.getcwd()+"\psd.accdb"
    cwd = cwd.replace("\\","\\\\")
    stringConnect="Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+cwd
    cnxn = pyodbc.connect(stringConnect)
    sql = "SELECT * FROM "+day+"Query"
    cursor = cnxn.cursor()
    cursor.execute(sql)
    nameList=[]
    timeList=[]
    waList=[] 
    for row in cursor.fetchall():
        nameList.append(row[1])
        if row[3] is None:
            timeList.append(row[2])
        else:
            timeList.append(row[3])
        temp=[]
        temp.append(row.WA_Contact_Name)
        temp.append(row.WA_Contact_Name_2)
        if None in temp:
            temp.remove(None) 
        waList.append(temp)
    cursor.close()
    cnxn.close()
    # print(nameList)
    # print(timeList)
    # print(waList)
    return nameList,timeList,waList

# getLists("saturday")
