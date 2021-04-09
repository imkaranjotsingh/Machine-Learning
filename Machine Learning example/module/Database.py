import pymysql
import datetime

class dba:
    def connect(self):
        return pymysql.connect("localhost","root","","test" )

    def read(self, id):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM test2 order by name asc")
            else:
                cursor.execute("SELECT * FROM test2 where id = %s order by name asc", (id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def insert(self,data):
        con = dba.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO test1(name) VALUES( %s )", (data['name']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def check_login(self,data):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM login WHERE username = %s and password = %s ",(data['username'],data['password']))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def insert_item(self,imagename):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO webimage(imagename) VALUES(%s)",imagename)
            con.commit()
            print("inserting!!!")
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False
        finally:
            con.close()

    def image_get(self,data):
        con = dba.connect(self)
        cursor = con.cursor()
        print("database imagename:")
        print(data)
        try:
            cursor.execute("SELECT * FROM webimage Where imagename = %s",data)
            return cursor.fetchall()
        except:
            print("Error in retriving!!!!!")
            return()
        finally:
            con.close()
            
    def update(self, id, data):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            print("UPDATE test2 set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            cursor.execute("UPDATE test2 set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM test2 where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
