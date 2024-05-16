from json import loads
import joblib
from kafka import KafkaConsumer
import pandas as pd

#from bd_config.db_query import create_table
import bd_config.db_query as db


# Cargar el modelo una sola vez fuera de la función predict
model = joblib.load('Notebooks/model.pkl')


def predict(m):
    # Decodificar el mensaje
    s = loads(m.value)
   
    # Crear un DataFrame a partir de los datos del mensaje
    df = pd.DataFrame(s, index=[0])

    # Predecir utilizando el modelo cargado
    prediction = model.predict(df.drop(columns=['happiness_score'], axis=1))

    # Añadir la columna de predicciones al DataFrame
    df['predicted_happiness_score'] = prediction

    return df


def kafka_consumer():
    # Configurar el consumidor de Kafka
    consumer = KafkaConsumer(
        'test-data',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092'],
    )

    while True:
        # Esperar por mensajes durante 5 segundos
        message = consumer.poll(timeout_ms=5000)

        # Salir si no hay más mensajes
        if not message:
            break
        
        # Procesar los mensajes recibidos
        for _, messages in message.items():
            for m in messages:
                # Predecir y cargar los datos en la base de datos
                row = predict(m)
                db.load(row)


if __name__ == '__main__':
    # Crear la tabla en la base de datos si no existe
    db.create_table()

    # Ejecutar el consumidor de Kafka
    kafka_consumer()
