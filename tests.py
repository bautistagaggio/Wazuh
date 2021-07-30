import pytest
import sqlite3
import psycopg2


class Test_Tests:
    dic = {'1.txt': 'a', '2.txt': 'b', '3.txt': 'c', '4.txt':'d', '5.txt': 'e'}

    one = dic.get('1.txt')
    two = dic.get('2.txt')
    three = dic.get('3.txt')
    four = dic.get('4.txt')
    five = dic.get('5.txt')


    assert 'a' == one
    assert 'b' == two
    assert 'c' == three
    assert 'd' == four
    assert 'e' == five

    # assuming the database is stored on some server
    def test_assert_structure(self):
        conn = psycopg2.connect("dbname=clients user=postgres")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CLIENTS")
        rows = cur.fetchall()
        assert "[‘id’, ‘name’, ‘country’, ‘age’]" == rows[0]

    def test_assert_age(self):
        conn = psycopg2.connect("dbname=clients user=postgres")
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE Age < 5")
        data = cur.fetchall()
        assert data is False

    def test_assert_null_values(self):
        conn = psycopg2.connect("dbname=clients user=postgres")   
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE ID,NAME,COUNTRY,AGE IS NULL")
        data = cur.fetchall()
        assert data is False
       


# fixture as a "parameter" for a test function
    @pytest.mark.usefixtures("init_driver")
    def test_something(self):
        pass



            
        





        

