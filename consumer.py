from json import loads
import joblib
from kafka import KafkaConsumer
import pandas as pd
import os
import bd_config.db_query as db

model = joblib.load('Model/model.pkl')


def predict(m):
    s = loads(m.value)
    df = pd.DataFrame(s, index=[0])
    prediction = model.predict(df.drop(columns=['happiness_score'], axis=1))
    df['predicted_happiness_score'] = prediction
    return df


def kafka_consumer():
    consumer = KafkaConsumer(
        'test-data',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092'],
    )

    while True:
        message = consumer.poll(timeout_ms=5000)
        if not message:
            break            # Exit if there are no more messages
        
        # Processing incoming messages
        for _, messages in message.items():
            for m in messages:
                row = predict(m)
                db.load(row)


if __name__ == '__main__':
    db.create_table()
    kafka_consumer()  # Running Kafka's consumer
