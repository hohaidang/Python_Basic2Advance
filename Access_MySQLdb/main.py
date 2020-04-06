import pymysql


def main():
    db = pymysql.connect(db='python_tutorials', user='root', passwd='123', host='localhost', port=3307)
    cursor = db.cursor()
    sql = """CREATE TABLE PERSON (
       ID INT NOT NULL,
       FIRST_NAME  CHAR(20) NOT NULL,
       LAST_NAME  CHAR(20),
       AGE INT,
       SEX CHAR(1),
       PRIMARY KEY (ID) )"""

    cursor.execute(sql)

if __name__ == '__main__':
    main()