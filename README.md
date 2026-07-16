# log-pipline
An end-to-end data engineering project demonstrating log generation, data ingestion, ETL processing with PySpark, data storage, and visualization for analytics. 

🚀 Log Pipeline with Apache Flume, Hadoop & PySpark

An end-to-end Data Engineering project that simulates real-time log generation, ingests data using Apache Flume, stores it in Hadoop HDFS, processes it with Apache Spark (PySpark), and visualizes the results using Matplotlib.

---

📌 Project Overview

This project demonstrates a complete Data Engineering pipeline from data generation to visualization.

Architecture

Python Log Generator
        │
        ▼
 Apache Flume
        │
        ▼
   Hadoop HDFS
        │
        ▼
 Apache Spark (PySpark)
        │
        ▼
 Data Processing (ETL)
        │
        ▼
 Matplotlib Visualization

---

🛠 Technologies

- Python 3
- Apache Flume
- Apache Hadoop (HDFS)
- Apache Spark (PySpark)
- Matplotlib
- Linux
- Git & GitHub

---

📂 Project Structure

log_pipeline/
│
├── log.py
├── README.md
│
├── flume-conf/
│   └── taildir-to-hdfs.conf
│
└── images/
    ├── architecture.png
    ├── flowchart.png
    └── dashboard.png

---

⚙️ Project Workflow

1. Generate random log data using Python.
2. Apache Flume monitors the log file.
3. Flume transfers logs into Hadoop HDFS.
4. Spark reads data from HDFS.
5. Spark cleans and transforms the data.
6. Aggregate log levels.
7. Visualize the results using Matplotlib.

---

🚀 Installation & Execution

1️⃣ Create Project Folder

mkdir -p ~/log_pipeline
cd ~/log_pipeline

---

2️⃣ Create Python Log Generator

nano log.py

Paste the Python code and save the file.

Create the log file:

touch ~/Desktop/app.logs

---

3️⃣ Create Flume Configuration

mkdir ~/flume-conf
nano ~/flume-conf/taildir-to-hdfs.conf

Paste the Flume configuration and save.

---

4️⃣ Start Hadoop

start-all.sh

Verify services:

jps

---

5️⃣ Create HDFS Directory

hdfs dfs -mkdir -p /user/bigdata/flume-logs

---

6️⃣ Start Apache Flume

cd ~/apache-flume-1.7.0-bin

bin/flume-ng agent \
--conf conf \
--conf-file /home/bigdata/flume-conf/taildir-to-hdfs.conf \
--name agent \
-Dflume.root.logger=INFO,console

---

7️⃣ Run Python Log Generator

Open another terminal:

python3 ~/log_pipeline/log.py

---

8️⃣ Verify Logs in HDFS

hdfs dfs -ls /user/bigdata/flume-logs

---

9️⃣ Start PySpark

pyspark

---

🔟 Read Logs

df = spark.read.text("hdfs://localhost:9000/user/bigdata/flume-logs/")

df.show(truncate=False)

---

1️⃣1️⃣ Split Log Fields

from pyspark.sql.functions import split

df_split = df.withColumn(
    "date",
    split(df["value"], " ").getItem(0)
).withColumn(
    "time",
    split(df["value"], " ").getItem(1)
).withColumn(
    "level",
    split(df["value"], " ").getItem(2)
)

df_split.show()

---

1️⃣2️⃣ Count Log Levels

log_counts = df_split.groupBy("level").count()

log_counts.show()

---

1️⃣3️⃣ Collect Results

pdf = log_counts.collect()

levels = [row["level"] for row in pdf]
counts = [row["count"] for row in pdf]

---

1️⃣4️⃣ Visualize Data

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.bar(levels, counts)
plt.title("Log Levels Distribution")
plt.xlabel("Log Level")
plt.ylabel("Count")
plt.show()

---

🛑 Stop the Project

Stop Python

Ctrl + C

Stop Flume

Ctrl + C

Exit Spark

exit()

Stop Hadoop

stop-all.sh

---

📊 Expected Output

- Random log generation
- Logs stored in Hadoop HDFS
- Data processed with Apache Spark
- Log level statistics
- Bar chart visualization

---

📚 Learning Outcomes

- Build an end-to-end Data Engineering pipeline.
- Understand Apache Flume data ingestion.
- Store files in Hadoop HDFS.
- Process large-scale data with Apache Spark.
- Perform ETL transformations.
- Visualize processed data.
- Work with Linux and GitHub.

---

👨‍💻 Team Members

- Shenouda Aboelrose
- Abdelrahman Ahmed Mohamed
- Mohamed Mo'men Mohamed Abdullah

---

📄 License

This project is created for educational purposes.
