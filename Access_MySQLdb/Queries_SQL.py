from os import error

import pymysql
import sys

def db_error_handling(error, db):
    print("ERROR", error)
    db.close()
    sys.exit(1)

def main():
    try:
        db = pymysql.connect(db='birthdays', user='root', passwd='123', host='localhost', port=3307)
    except pymysql.Error as e:
        print("ERROR", e)
        sys.exit(1)
    cursor = db.cursor()
    sql = """Create table tourneys(
            name varchar(30),
            wins real,
            best real,
            size real)"""
    try:
        cursor.execute(sql)
    except:
        pass
    # sql = """INSERT INTO tourneys (name, wins, best, size)
    #         VALUES  ('Dolly', 7, 245, 8.5),
    #                 ('Etta', 4, 283, 9),
    #                 ('Irma', 9, 266, 7),
    #                 ('Barbara', 2, 197, 7.5),
    #                 ('Gladys', 13, 273, 8)"""
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except pymysql.Error as e:
    #     print("ERROR", e)
    #     db.rollback()
    #     pass
    sql = """CREATE TABLE dinners (
            name varchar(30),
            birthdate date,
            entree varchar(30),
            side varchar(30),
            dessert varchar(30)
            )"""
    try:
        cursor.execute(sql)
    except pymysql.Error as e:
        print(e)
        pass


    # sql = """insert into dinners (name, birthdate, entree, side, dessert)
    #          Values ('Dolly', '1946-01-19', 'steak', 'salad', 'cake'),
    #                 ('Etta', '1938-01-25', 'chicken', 'fries', 'ice cream'),
    #                 ('Irma', '1941-02-18', 'tofu', 'fries', 'cake'),
    #                 ('Barbara', '1948-12-25', 'tofu', 'salad', 'ice cream'),
    #                 ('Gladys', '1944-05-28', 'steak', 'fries', 'ice cream')"""
    #
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except pymysql.Error as e:
    #     print(e)
    #     pass

    sql = """SELECT COUNT(name) FROM dinners WHERE name = '%s'""" %('Dolly')
    sql = """select avg(best) from tourneys"""
    sql = """select sum(wins) from tourneys"""
    sql = """select min(wins) from tourneys"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except pymysql.Error as e:
        print(e)
        pass
    sql = """select count(name), entree from dinners group by entree"""
    sql = """SELECT name, birthdate FROM dinners ORDER BY birthdate DESC"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except pymysql.Error as e:
        print(e)
        pass

    # --------- Querying Multiple Tables ------------
    sql = """SELECT table1.column1, table2.column2
            FROM table1
            JOIN table2 ON table1.related_column=table2.related_column"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except pymysql.Error as e:
        print(e)
        pass

    db.close()
if __name__ == '__main__':
    main()