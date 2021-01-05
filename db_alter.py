import datetime

import mysql.connector

from dbconf import (db_host, db_name, db_passwd, db_user)

mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_passwd,
        database=db_name)

cursor = mydb.cursor()

high = datetime.datetime.now()
medium = datetime.datetime.now() - datetime.timedelta(days=1)
low = datetime.datetime.now() - datetime.timedelta(days=2)

print('Med: ', medium)
print('high: ', high)
print('low: ', low)

def add_values():
    lang = '294'
    qid = '7'
    lid = '7'
    version = '9'

    print('Inserting random valuesf for rejected')

    qry = """INSERT INTO matches  
    SET timestamp="%s",
    lang=%s,
    QID=%s,
    LID=%s,
    status=%s,
    version=%s 
    """
    qry = qry % (high, lang, qid, lid, -1,
        version)

    try:
        cursor.execute(qry)
    except Exception as e:
        print('Itgem may have been added')
    else: 
        print('item added')
        mydb.commit()

    print(' Inserting random for added values')
    lang = '256'
    qid = '8'
    lid = '8'
    version = '10'
    qry = """INSERT INTO matches  
    SET timestamp="%s",
    lang=%s,
    QID=%s,
    LID=%s,
    status=%s,
    version=%s 
    """
    qry = qry % (low, lang, qid, lid, 1,
        version)
        
    try:
        cursor.execute(qry)
    except Exception as e:
        print('Itgem may have been added')
    else:
        print('Item added') 
        mydb.commit()


def update_values():
    print('Updating a rejected')

    qry = """UPDATE matches  
    SET timestamp="%s"
    WHERE status="-1" and lang=188
    """
    qry = qry % high
        
    cursor.execute(qry)
    mydb.commit()

    print('Updating a todo')

    qry = """UPDATE matches 
    SET timestamp="%s"
    WHERE status=0 and lang=150
    """
    qry = qry % low
        
    cursor.execute(qry)
    mydb.commit()

    print('Updating an Added')

    qry = """UPDATE matches  
    SET timestamp="%s"
    WHERE status=1  and lang=143
    """
    qry = qry % low
        
    cursor.execute(qry)
    mydb.commit()