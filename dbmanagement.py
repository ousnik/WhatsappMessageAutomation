import pyodbc
def getNameList():
    cnxn = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\Docs\\psd.accdb")
    sql = """\
    SELECT * FROM FriQuery
    """
    cursor = cnxn.cursor()
    cursor.execute(sql)
    nameList=[]
    for row in cursor.fetchall():
        nameList.extend(list(row))
    nameList=list(set(nameList))
    nameList.remove(None)
    nameList.sort()
    cursor.close()
    cnxn.close()
    return nameList