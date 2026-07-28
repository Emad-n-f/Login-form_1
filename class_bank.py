import sqlite3

class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('create table if not exists info (id integer primary key, name text, lname text, email text,pas text)')
        self.con.commit()

    def insert_info(self, name, lname, email,pas):
        self.cur.execute('insert into info values (null, ?, ?, ?,?)', (name, lname, email,pas))
        self.con.commit()

    def select_info(self):
        self.cur.execute('select * from info')
        return self.cur.fetchall()

    def delete_info(self, id):
        self.cur.execute('delete from info where id=?', (id,))
        self.con.commit()

    def edit_name(self,name,id):
        self.cur.execute('update info set name = ? where id = ?',(name,id))
        self.con.commit()

    def edit_lname(self,lname,id):
        self.cur.execute('update info set lname = ? where id = ?',(lname,id))
        self.con.commit()

    def edit_email(self,email,id):
        self.cur.execute('update info set email = ? where id = ?',(id,email))
        self.con.commit()

    def edit_pass(self,pas,id):
        self.cur.execute('update info set pas = ? where id = ?',(pas,id))
        self.con.commit()