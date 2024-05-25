<div style="text-align: center;">
    <img src="https://github.com/mdlangeles/Workshop_1/assets/111391755/1efa1459-711a-4b66-b187-1113e46912c8" alt="airf" width="700" height="300">
</div>

# Workshop_3: Machine Learning and Data Streaming :chart_with_downwards_trend: :open_file_folder:
## By: María de los Ángeles Amú Moreno :woman_technologist:
In this project, a comprehensive analysis and development has been carried out to predict the happiness index of different countries using machine learning techniques. From five CSV files containing information about the happiness index in different countries, a regression model was trained to predict the happiness index. The process started with a thorough Exploratory Data Analysis (EDA) and an Extract, Transform and Load (ETL) procedure to extract and prepare the relevant features from the files. Subsequently, the model was trained using a data split of 70\% for training and 30\% for testing.

Once the data was transformed, it was transmitted to a consumer who, using the previously trained model, predicted the happiness index and stored the predictions along with the corresponding features in a database.

Finally, a performance metric was extracted to evaluate the accuracy of the model by comparing the test data with the generated predictions. All the work performed is presented schematically in the following figure, providing a clear and detailed view of the flow and results of the project.

## Technologies Used
The tools I used in this project were:

- Python
- Jupyter Notebook
- PostgreSQL
- Apache Kafka
- Docker Desktop
- CSV files
- Scikit-learn library

## Datasets Used:
Five CSVs files of different years (2015 - 2019) with Happiness information of different countries

## Workflow Project:
![work drawio](https://github.com/mdlangeles/workshop3/assets/111391755/f8bbc043-ff20-48f7-9f7d-720298872b39)


## Project Organization:
The **bd_config** folder contains a file related to creating, inserting and extracting PostgreSQL data.

The **Data** folder contains the csv worked on this project:
  - 2015.csv
  - 2016.csv
  - 2017.csv
  - 2018.csv
  - 2019.csv
  - x_test.csv: this csv is saved when running the project, scan the notebooks for more detail.
  - y_test.csv: this csv is saved when running the project, scan the notebooks for more detail.
    
The **Model** folder contains the model.pkl used to work in this project.

The **Notebooks** folder contains the EDA information of my project, which contains the following notebooks inside:
  - EDA.ipynb: EDA of all the csv and the model Training.
  - metric.ipynb: Contains the metric of the project.

In the **service** folder we find the transformations for the Feature Selection.

We find the **consumer.py** and the **producer.py**

Finally we find a file called **docker-compose.yml** which contains the information that is part of the configuration in Docker.

## Requisites

- Install Python : [Python Downloads](https://www.python.org/downloads/)
- Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)
- Install Power BI : [Power BI Downloads](https://www.microsoft.com/es-es/download/details.aspx?id=58494)
- Install Docker Desktop :[Docker Desktop Downloads](https://www.docker.com/products/docker-desktop/)

## Run This Project
1. Clone the project:
```bash
https://github.com/mdlangeles/workshop3.git
```

2. Go to the project directory
```bash
cd workshop3
```

3. In the root of the project, create a connections.json file, this to set the database credentials:
```bash
{
    "user": "your_user",
    "password": "your_password",
    "port": number_port,
    "server": "your_server",
    "db": "your db_name"
  }
```

4. Create virtual environment for Python
```bash
python -m venv venv
```

5. Activate the enviroment
```bash
venv/bin/activate 
```

6. Install libraries
```bash
  pip install -r requirements.txt
```

7. Create a database in PostgreSQL:
![image](https://github.com/mdlangeles/workshop3/assets/111391755/4f7097d1-2438-46d7-8993-fb5ac639c540)

9. Start looking the notebooks:
- EDA.ipynb
- metric.ipynb

10. Launch the containers:
```bash
  docker compose up
```

11. Enter to the container
```bash
  docker exec -it kafka-workshop3 bash
```

12. Create the topic
```bash
  kafka-topics --bootstrap-server kafka-workshop3:9092 --create --topic workshop3
```

13. List the topic
```bash
  kafka-topics --bootstrap-server kafka-workshop3:9092 --list
```

14. In other terminal, run:
```bash
  python producer.py
```
```bash
  python consumer.py
```
Once the straming is done, your console should look like this:
![Captura de pantalla 2024-05-24 130443](https://github.com/mdlangeles/workshop3/assets/111391755/dc7938e3-6d02-490c-95bd-cffa4aec1013)

15. Go to PostgreSQL and you will see the table already created:
<img width="965" alt="image" src="https://github.com/mdlangeles/workshop3/assets/111391755/0640035c-c9c2-4cd0-b548-3ea903842285">

16. Explore the metric notebook to see the statistics and enjoy the project.

## Thanks 😊

Thank you for visiting my repository, and I hope this project is helpful for your learning :)

I remain open to any questions <3

