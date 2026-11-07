from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
engine = create_engine('postgresql://postgres:Kawasaki09041988@localhost:5432/QA')
Session = sessionmaker(bind=engine)

# Конструктор
class DatabaseManager:
    def __init__(self):
        self.session = Session()

    def create_lesson(self):
        sql = text("insert into subject(subject_title) values (:new_lesson)")
        self.session.execute(sql, {'new_lesson': 'Skypro'})
        self.session.commit()

    def return_create(self):
        sql_statement = text("select * from subject where subject_title = :sub_title")
        result = self.session.execute(sql_statement, {'sub_title': 'Skypro'}).fetchall()
        assert result[0]['subject_title'] == 'Skypro'

    def update(self):
        sql = text("UPDATE subject SET subject_id = :id WHERE subject_title = :title")
        self.session.execute(sql, id=17, title='Skypro')

    def close_connection(self):
        self.session.close()