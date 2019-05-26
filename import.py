import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

database_url = 'postgres://igebfuidzqsctq:0feaad99b38613562d4a4f3ce1fdda2f668e845cd274c45b75f0024170f2221f@ec2-54-75-238-138.eu-west-1.compute.amazonaws.com:5432/d5a2jrhp1v74ts'

drop_query = 'DROP TABLE books;'
create_query = 'CREATE TABLE IF NOT EXISTS books(id SERIAL PRIMARY KEY, isbn VARCHAR(13), title VARCHAR(60), author VARCHAR(60), year INTEGER);'

def main():
    engine = create_engine(database_url)
    db = scoped_session(sessionmaker(bind=engine))
    #db.execute(drop_query)
    db.execute(create_query)
    db.commit()

    with open("books.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for isbn, title, author, year in reader:
            db.execute("INSERT INTO books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn":isbn, "title":title, "author":author, "year":year})
            print(isbn)
        db.commit()

    print(db.execute("SELECT COUNT(*) FROM books"))

if __name__ == "__main__":
    main()
