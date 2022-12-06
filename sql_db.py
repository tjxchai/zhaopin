import pymysql


def db():
    return {'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123123',
            'db': 'zhipin_com',
            'charset': 'utf8'}


def sqlconn():
    dbset = db()
    conn = pymysql.connect(host=dbset['host'],
                           port=dbset['port'],
                           user=dbset['user'],
                           password=dbset['password'],
                           db=dbset['db'],
                           charset=dbset['charset'])
    return conn


def sql_read(sql, conn, data=[]):
    """sql,conn,data=[]
    返回 sql_read[‘rows’]"""
    execute = {}
    try:
        cursor = conn.cursor()
        execute['try1'] = cursor.execute(sql)
        execute['rows'] = cursor.fetchall()

    except Exception as e:
        execute['except1'] = e

    return execute


def sql_execute(sql, conn, data=[]):
    """sql,conn,data=[]"""
    execute = {}
    try:

        cursor = conn.cursor()
        execute['try1'] = cursor.execute(sql)
        execute['try2'] = conn.commit()

    except Exception as e:
        print(e)
        execute['except1'] = e
        execute['except2'] = conn.rollback()

    return execute
