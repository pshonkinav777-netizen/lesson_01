from sqlalchemy import create_engine
from sqlalchemy import text
from CreateLesson import DatabaseManager
import pytest

db_connection = "postgresql://postgres:Kawasaki09041988@localhost:5432/QA"
db = create_engine(db_connection)


def test_create_lesson():
    connection = db.connect()
    sql = text(
        "insert into subject(\"subject_title\") values (:new_lesson)")
    db.execute(sql, new_lesson='Skypro')
    sql_statement = text(
        "select * from subject where subject_title = :sub_title")
    rows1 = db.execute(sql_statement, sub_title='Skypro').fetchall()
    assert rows1[0]["subject_title"] == 'Skypro'
    connection.close()
    sql = text("DELETE FROM subject WHERE subject_title = :title")
    db.execute(sql, title='Skypro')


def test_update_lesson():
    sq = DatabaseManager()
    sq.create_lesson()
    sql = text(
        "UPDATE subject SET subject_id = :id WHERE subject_title = :title")
    db.execute(sql, id=17, title='Skypro')
    sql_statement = text(
            "select * from subject where subject_title = :sub_title")
    rows1 = db.execute(sql_statement, sub_title='Skypro').fetchall()
    assert rows1[0]["subject_id"] == 17
    sql = text("DELETE FROM subject WHERE subject_title = :title")
    db.execute(sql, title='Skypro')


def test_delete_lesson():
    sq = DatabaseManager()
    sq.create_lesson()
    sql = text("DELETE FROM subject WHERE subject_title = :title")
    db.execute(sql, title='Skypro')
    ret = db.execute(
        text("SELECT * FROM subject WHERE subject_title = 'Skypro'")
        ).fetchone()
    assert ret is None
