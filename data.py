from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json
import pandas as pd
import csv
words = pd.read_table('data/glove.840B.300d.txt', sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)

engine = create_engine('sqlite:///glovedata.db', echo=True)
# Base = declarative_base()


# class data(Base):
#     __tablename__ = "glovedata"
#     word = Column(String, primary_key=True)
#     vector = Column(String)
#
#     def __init__(self, word, vector):
#         self.word = word
#         self.vector = vector
#
# Base.metadata.create_all(engine)

def insert(engine,word, vector, ):
    engine.execute(f"INSERT INTO glovedata (word , vector) VALUES ('{word}','{vector}')")
    return True

def serach(engine, word:str):
    result = engine.execute(f"SELECT word, vector FROM 'glovedata' where word='{word}' ")
    vector = 0
    for i in result:
        vector = i['vector']
    return vector

i =0
for word in words.index:
    word = word
    v = words.loc[word]
    insert(engine, word, v)
    i+=1
    if i ==50:
        break

def GloVeEmbeddings(words):
    for word in words.index:
        insert(word, words.loc[word], engine)
        print(word, words.loc[word])
        break
