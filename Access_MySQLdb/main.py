from os import error

import pymysql
import sys

def db_error_handling(error, db):
    print("ERROR", error)
    db.close()
    sys.exit(1)

def main():
    try:
        db = pymysql.connect(db='python_tutorials', user='root', passwd='123', host='localhost', port=3307)
    except pymysql.Error as e:
        print("ERROR", e)
        sys.exit(1)
    cursor = db.cursor()

    # ------------Creating Table --------------
    sql = """CREATE TABLE PERSON (
       ID INT NOT NULL,
       FIRST_NAME  CHAR(20) NOT NULL,
       LAST_NAME  CHAR(20),
       AGE INT,
       SEX CHAR(1),
       PRIMARY KEY (ID) )"""
    try:
        cursor.execute(sql)
    except pymysql.Error as e:
        print("ERROR", e)
        pass

    #-----------------Insert Table----------------
    sql = """INSERT INTO PERSON(ID, FIRST_NAME,
       LAST_NAME, AGE, SEX )
       VALUES (2, 'Dang', 'Ho', 25, 'M')"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except pymysql.Error as e:
        # Rollback in case there is any error
        print("ERROR", e)
        db.rollback()
        pass

    # ---------------Update data in Table----------
    # Update age = 30 if sex is M (men)
    sql = "UPDATE PERSON SET AGE = 30 WHERE SEX = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("ERROR", e)
        db.rollback()
        pass

    # --------------Read data from the table------------
    sql = "select * from person"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[1]
            lname = row[2]
            age = row[3]
            sex = row[4]
            print("fname = %s,lname = %s,age = %d,sex = %s" % \
                (fname, lname, age, sex, ))
    except pymysql.Error as e:
        print("ERROR", e)
        pass

    # # ---------------- Delete data form the table -------------
    # sql = "Delete from person where age > '%d'" % (29)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except:
    #     db.rollback()

    db.close()

if __name__ == '__main__':
    main()