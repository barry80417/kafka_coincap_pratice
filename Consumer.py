#!/usr/bin/env python
# coding: utf-8

# In[3]:


from kafka import KafkaConsumer
import pymongo
import pandas as pd
import json

brokers, topic = 'localhost:9092', 'coincap'
consumer = KafkaConsumer(topic, bootstrap_servers=[brokers])

client = pymongo.MongoClient('localhost', 27017)
database = client["mongo-sample"]
collection = database["coincap"]

for msg in consumer:
    key = {}
    k1 = str(msg.key)[2:21]
    key = {'time':k1}
    d = json.loads(msg.value)
    d['data'].update(key)
    df = pd.DataFrame(d)
    df= df.drop(columns = ['timestamp'],axis = 1)
    df = df.T
    df.reset_index(inplace = True)
    df = df.drop(columns = ['index'],axis = 1)
    records = df.to_dict('records') 
    collection.insert_many(records)
    
    print("key=%s, value=%s" % (msg.key, msg.value))

