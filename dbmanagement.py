import pyodbc
def getLists(day):
    cnxn = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\Docs\\psd.accdb")
    sql = "SELECT * FROM "+day+"Query"
    cursor = cnxn.cursor()
    cursor.execute(sql)
    timeList=[]
    waList=[]
    for row in cursor.fetchall():
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
    # print(timeList)
    # print(waList)
    return timeList,waList

# getLists("Friday")
