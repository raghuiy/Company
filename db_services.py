
import mysql.connector


print ('Inside DB Services')

def get_db_conn():
    cnx = mysql.connector.connect(user="raghuiy", passwd="@Krishna10",
                                  host="10.1.3.55",
                                  database="malan",
                                  auth_plugin="mysql_native_password")

    return(cnx)

def write_to_choice_db(rec):
    cnx=get_db_conn()
    cur = cnx.cursor()
    sql="insert into  choice(regid,color)  values(%s,%s)"
    print('Rec value is: ', rec)
    cur.execute(sql,rec)
    cnx.commit()
    read_from_db('choice')

def write_to_reg_db(visitor_name):
    cnx=get_db_conn()
    cur = cnx.cursor()
    sql="insert into REG(name) values ( %s )"
    #print('***Sql= ', sql)
    rec=[visitor_name]
    #rec=visitor_name
    cur.execute(sql,rec)
    cnx.commit()
    read_from_db('REG')


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

print('Today is Friday.This is DB services')
#read_from_db('choice')
#write_to_choice_db(rec= [8817,'Majenta'])
#write_to_reg_db('Mohanan')

