#!/usr/bin/env python
# coding: utf-8

from kafka import KafkaProducer
from datetime import datetime
import time
import requests
import json

brokers, topic = 'localhost:9092', 'coincap'
producer = KafkaProducer(bootstrap_servers=[brokers])

i = 0
while True:
    url = 'https://api.coincap.io/v2/assets/ethereum'
    r = requests.get(url)
    k = f'{datetime.now()}t'.encode()
    v = json.dumps(r.json()).encode()
    print(k, v)
    producer.send(topic, key=k, value=v)
    time.sleep(5)
    i = i + 1



