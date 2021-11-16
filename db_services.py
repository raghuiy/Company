import mysql.connector

# This host name is for OCI
host_name = "192.168.1.87"
# This host name is for local machine
#host_name = 'localhost'
print('Inside DB Services')


def get_db_conn():
    cnx = mysql.connector.connect(user="raghuiy", passwd="@Krishna10",
                                  host=host_name,
                                  database="malan",
                                  auth_plugin="mysql_native_password")

    return (cnx)


def write_to_choice_db(rec):
    cnx = get_db_conn()
    cur = cnx.cursor()
    sql = "insert into  choice(regid,color)  values(%s,%s)"
    print('Rec value is: ', rec)
    cur.execute(sql, rec)
    #print('Last row inserted into CHOICE was : ', cur.lastrowid)
    cnx.commit()
    return cur.lastrowid


def write_to_reg_db(visitor_name):
    cnx = get_db_conn()
    cur = cnx.cursor()
    sql = "insert into REG(name) values ( %s )"
    # print('***Sql= ', sql)
    rec = [visitor_name]
    # rec=visitor_name
    cur.execute(sql, rec)
    print('Last row inserted into REG  was : ', cur.lastrowid)
    cnx.commit()
    return cur.lastrowid


def read_from_db(tbl_name, pWhr_Clause=""):
    try:
        cnx = get_db_conn()
        print('Table name=', tbl_name, ' Where clause= ', pWhr_Clause)
        fetch_cursor = cnx.cursor()
        print('This is the recd whr clause ' + pWhr_Clause)
        if (pWhr_Clause == "INNER_JOIN"):
            sql = 'select REG.regid,REG.name , color ' \
                  'from choice ' \
                  'inner join REG on choice.regid=REG.regid ' \
                  'order by REG.name'
        else:
            sql = "select * from " + tbl_name
            print('The sql was= ', sql)
        fetch_cursor.execute(sql)
        result = fetch_cursor.fetchall()
    #for row in result:
     #   print('Here is the printed row: ', row)
    except:
        print('Caught some error')
    finally:
        cnx.close()
        return result


print('Today is Tue16-Nov-2021.This is DB services')
# read_from_db('choice')
# write_to_choice_db(rec= [8817,'Majenta'])
# write_to_reg_db('Mohanan')
