import sqlite3
import threading
import random

class API():
    def __init__(self,dbfile):
        self.dbfile=dbfile
        # 创建一个数据库连接池
        self.connections = {}
        self.threads = []
        for i in range(10):
            t = threading.Thread(target=self.runsql, args=(i,))
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()


    def runsql(self,sqlstr,thread_id):
        conn = self.get_connection(thread_id)
        curser=conn.cursor()
        curser.execute(sqlstr)
        table_info=curser.fetchall()
        conn.commit()
        conn.close()
        return table_info


    def get_connection(self,thread_id):
        if thread_id not in self.connections:
            self.connections[thread_id] = sqlite3.connect(self.dbfile)
        return self.connections[thread_id]
    # def worker(self,thread_id):
    #     conn = self.get_connection(thread_id)
    #     self.curser=conn.cursor()
    #     self.curser.execute(sqlstr)


   
    def getdatahead (self,tablename):        
        sqlstr="PRAGMA table_info ("+tablename+");" 
        table_info=self.runsql(sqlstr,random.randint(0,100))       

        res=list()
        for item in table_info:
            # print(item[1])
            res.append(item[1])
        # print(res)
        return res
    def getalltablename(self):
        sqlstr="SELECT name FROM sqlite_master"
        table_info=self.runsql(sqlstr,random.randint(0,100))       

        res=list()
        for item in table_info:
            # print(item[1])
            res.append(item[0])
        # print(res)
        return res

    def getdatabody(self,tablename):
        sqlstr="SELECT * FROM "+tablename   
        table_info=self.runsql(sqlstr,random.randint(0,100))

        return table_info
    def getdataone(self,tablename,id):
        sqlstr="SELECT * FROM "+tablename +" WHERE id=" +str(id)
        print(sqlstr)
        table_info=self.runsql(sqlstr,random.randint(0,100))
        # with self.lock:            
        #     table_info=self.curser.fetchall()
        #     self.closeconn()
        # print(table_info)
        print(table_info[0])
        return table_info[0]

    def insertdata(self,tablename,data):
        print(tablename,data)
        datastr=list2str(data)
        print(datastr)
        sqlstr="INSERT INTO "+tablename+" VALUES ("+datastr+")"
        print(sqlstr)
        # self.runsqlcommit(sqlstr)
        self.runsql(sqlstr,random.randint(0,100))
    def updatedata(self,tablename,colums,values,condition):
        if condition=='':
            print("更新记录必须有条件,condition不能为空")
        else:
            # # print(type(data))
            # c='"'
            # for i in data:
            #     print(i)
            #     c+=(str(i)+'","')
            # c=c[:-2]
            # # print(c)
            # # print(condition)
            result = ",".join([f"{x}='{y}'" for x, y in zip(colums[1:], values[1:])])
            print(result)
            sqlstr="UPDATE  "+tablename+" SET "+result+"WHERE "+condition
            print(sqlstr)
            self.runsql(sqlstr,random.randint(0,100))
    def delectdata(self,tablename,condition):
        print(tablename,condition)
        if condition=='':
            print("删除记录必须有条件,condition不能为空")
        else:
            sqlstr="DELETE FROM "+tablename+" WHERE "+condition
            # self.runsqlcommit(sqlstr)
            print(sqlstr)
            self.runsql(sqlstr,random.randint(0,100))
    # def changedata(self,sqlstr):
    #     conn = sqlite3.connect(self.dbfile)
    #     c=conn.cursor()
    #     sqlstr="INSERT INTO renyuanbiao (name,age,sex,workyear) VALUES('赵把',6,'男','2')"
    #     c.execute(sqlstr)
    #     conn.commit()
    #     conn.close()   
    # def getdata(self,tablename):
    #     conn = sqlite3.connect(self.dbfile)
    #     c=conn.cursor()
    #     c.execute("PRAGMA table_info (renyuanbiao);")
    #     table_info=c.fetchall()
    #     print(table_info)
    #     SQLSELECT="SELECT * FROM "+tablename
    #     # print(SQLSELECT)
    #     res=c.execute(SQLSELECT)
    #     listtext=res.fetchall()
    #     # jsontext=json.dumps(listtext)
    #     # # print(type(res))
    #     # for row in res:
    #     #     print(row)
    #     conn.close()
    #     # print(str(jsontext))
    #     return listtext
def list2str(list):
    res="'"
    for item in list:
        print(item)
        res+=(str(item)+"','")
    res=res[:-2]
    print(res)
    return(res)