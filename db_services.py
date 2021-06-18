
import mysql.connector


def get_db_conn():
    cnx = mysql.connector.connect(user="root", passwd="password",
                                  host="localhost",
                                  database="malan",
                                  auth_plugin='mysql_native_password')

    return(cnx)

def write_to_db(tbl_name, rec):
    cnx=get_db_conn()
    cur = cnx.cursor()
    sql="insert into " + tbl_name + " values (%s,%s,%s)"

    cur.execute(sql,rec)
    cnx.commit()
    read_from_db('choice')

def write_to_reg_db(visitor_name):
    cnx=get_db_conn()
    cur = cnx.cursor()
    sql="insert into regs (name)  values('" +visitor_name+"')"
    print('***Sql= ', sql)
    #rec=visitor_name
    cur.execute(sql)
    cnx.commit()
    read_from_db('regs')


def read_from_db(tbl_name):

    try:
        cnx = get_db_conn()
        fetch_cursor=cnx.cursor()
        sql="select * from " + tbl_name
        fetch_cursor.execute(sql)
        result = fetch_cursor.fetchall()
        cnx.close()
        for row in result:
            print(row)
    except:
        print('Caught some error')

print('This is DB services')
#write_to_db('choice',rec= ('296','Plony','Voilet'))
#write_to_reg_db('Roha')