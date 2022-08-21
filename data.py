# from sqlalchemy import create_engine
# from sqlalchemy import text
#
# engine = create_engine('sqlite:///../data.db.')

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# engine = create_engine('sqlite:///C:\\sqlitedbs\\school.db', echo=True)

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()


class data(Base):
    __tablename__ = "woot"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, name):

        self.name = name

Base.metadata.create_all(engine)
# where name= 'reza'

# engine.execute("INSERT INTO woot (name) VALUES ('krupal')")
result = engine.execute("SELECT name FROM 'woot' ")
for row in result:

    print("name:", row['name'])


import pandas as pd
import csv
words = pd.read_table('chatbot/data/glove.840B.300d.txt', sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)


def GloVeEmbeddings(words):
    # List containing all the embeddings for each word in the sentence
    emb_arr = []
    # Representing the embeddings by taking the mean of each in case its
    for word in words.index:
        print(word, words.loc[word])
        break

GloVeEmbeddings(words)