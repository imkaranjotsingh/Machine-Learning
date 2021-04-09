import pymysql
import datetime

class dba:
    def connect(self):
        return pymysql.connect("localhost","root","","python" )

    def read(self):
        con = dba.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM employee  ")
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
            cursor.execute("INSERT INTO test1(name,password) VALUES( '"+data['username']+"','"+data['password']+"')")
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
            cursor.execute("INSERT INTO images(imagename) VALUES(%s)",imagename)
            con.commit()
            print("inserting!!!")
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False
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
