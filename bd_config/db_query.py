import json
import psycopg2
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, '../db_config.json')

def connection():
    try:
        with open(config_path) as config_json:
            config = json.load(config_json)

        conn = psycopg2.connect(**config)
        return conn
    
    except psycopg2.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def create_table():
    try:
        conn = connection()
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS happiness (
                        ID SERIAL PRIMARY KEY,
                        year INT,
                        social_support FLOAT,
                        gdp_per_capita FLOAT,
                        healthy_life_expectancy FLOAT,
                        freedom FLOAT,
                        generosity FLOAT,
                        government_corruption FLOAT,
                        continent_africa INT,
                        continent_america INT,
                        continent_asia INT,
                        continent_europe INT,
                        continent_oceania INT,
                        happiness_score FLOAT,
                        predicted_happiness_score FLOAT)""")

  
        conn.commit()
        cursor.close()
        conn.close()
        print("Table created successfully!")

    except psycopg2.Error as err:
        print(f"Error to create the table: {err}")

def load(data):
    try: 
        conn = connection()
        cursor = conn.cursor()

        insert = """INSERT INTO happiness(year, social_support, gdp_per_capita, healthy_life_expectancy, freedom, generosity, government_corruption, continent_africa,
                      continent_america, continent_asia, continent_europe, continent_oceania, happiness_score, predicted_happiness_score)
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        data = (
            float(data['year'].iloc[0]),
            float(data['social_support'].iloc[0]),
            float(data['gdp_per_capita'].iloc[0]), 
            float(data['healthy_life_expectancy'].iloc[0]), 
            float(data['freedom'].iloc[0]), 
            float(data['generosity'].iloc[0]),
            float(data['government_corruption'].iloc[0]), 
            int(data['continent_Africa'].iloc[0]),
            int(data['continent_America'].iloc[0]), 
            int(data['continent_Asia'].iloc[0]), 
            int(data['continent_Europe'].iloc[0]), 
            int(data['continent_Oceania'].iloc[0]), 
            float(data['happiness_score'].iloc[0]), 
            float(data['predicted_happiness_score'].iloc[0])
        )
        
        cursor.execute(insert, data)

        conn.commit()
        cursor.close()
        conn.close()

        print("Row inserted successfully!")

    except psycopg2.Error as err:
        print(f"Error to insert the data: {err}")

def get_happiness_data():   
    try: 
        conn = connection()
        cursor = conn.cursor()

        get_data = "SELECT * FROM happiness"
        
        cursor.execute(get_data)

        data = cursor.fetchall()
        columns = ['id', 'year', 'social_support', 'gdp_per_capita', 'healthy_life_expectancy', 'freedom', 'generosity', 'government_corruption',
                    'continent_africa', 'continent_america', 'continent_asia', 'continent_europe', 'continent_oceania',
                    'happiness_score', 'predicted_happiness_score']

        
        df = pd.DataFrame(data, columns=columns)

        conn.commit()
        cursor.close()
        conn.close()
        print("Data successfully obtained")
        return df

    except psycopg2.Error as err:
        print(f"Error getting data: {err}")


