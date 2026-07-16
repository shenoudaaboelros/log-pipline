# log-pipline

An end-to-end Data Engineering project demonstrating real-time log generation, data ingestion using Apache Flume, fault-tolerant storage in Hadoop HDFS, ETL processing with Apache Spark (PySpark), and analytics visualization using Matplotlib.

🚀 **Log Pipeline with Apache Flume, Hadoop & PySpark**

---

## 📌 Project Overview
This project simulates a real-world big data pipeline. It continuously generates application logs, captures them via a streaming ingestion tool, stores them in a distributed file system, and processes them using an in-memory compute engine to extract structured analytics. 

**Architecture Flow:**
Python Log Generator ➡️ Apache Flume ➡️ Hadoop HDFS ➡️ Apache Spark (PySpark) ➡️ Matplotlib Visualization

---

## 🛠 Technologies & Tools
*   **Data Generation:** Python 3 (time, random, datetime)
*   **Ingestion:** Apache Flume
*   **Storage:** Apache Hadoop (HDFS)
*   **Processing (ETL):** Apache Spark (PySpark)
*   **Visualization:** Matplotlib, Pandas
*   **Environment:** Linux (Ubuntu/Arch)

---

## 📁 Project Structure
```text
log-pipline/
├── .gitignore               # Ignores __pycache__, local logs, and system files
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── run_pipeline.sh          # Master bash script for automated execution
├── log.py                   # Script to generate mock application logs
├── process.py               # PySpark script for ETL and aggregation
├── visualize.py             # Script to generate log distribution charts
├── flume-conf/
│   └── taildir-to-hdfs.conf # Flume agent configuration
└── images/                  # Diagrams and output charts
```

## ⚙️ Project Workflow
Generate Logs: log.py generates continuous, random application logs (INFO, DEBUG, ERROR, etc.) and appends them to a local file.
Ingest Data: Apache Flume monitors the local log file using a Taildir source and streams new entries.
Store Data: Flume sinks the ingested data directly into a distributed Hadoop HDFS directory.
Process (ETL): PySpark reads the raw text from HDFS, applies schema-on-read by splitting the strings into date, time, and level columns, and aggregates the log level counts.
Visualize: The aggregated DataFrame is converted to Pandas and plotted into a bar chart via Matplotlib.

## 🚀 Installation & Execution
### 1. Prerequisites & Environment Setup

Ensure Hadoop and Spark are installed and your environment variables ($HADOOP_HOME, $SPARK_HOME) are properly configured.

Install the required Python dependencies:
```Bash
pip install -r requirements.txt
```
### 2. Start Hadoop Services

Initialize your HDFS and YARN daemons, then create the target directory for Flume:
```Bash
start-all.sh
hdfs dfs -mkdir -p /user/bigdata/flume-logs
```
### 3. Run the Pipeline

Instead of running interactive terminal commands, you can execute the entire pipeline using the included shell script or run the components manually:

Terminal 1: Start the Log Generator
```Bash
python3 log.py
```
Terminal 2: Start the Apache Flume Agent
```Bash

flume-ng agent \
  --conf conf \
  --conf-file flume-conf/taildir-to-hdfs.conf \
  --name agent \
  -Dflume.root.logger=INFO,console
```
Terminal 3: Execute PySpark ETL and Visualization
Bash
```
# Submit the Spark job for processing
spark-submit process.py

# Generate the visualization
python3 visualize.py
```
## 📈 System Expandability
A core requirement for this system is that it remains expandable as data velocity increases. To achieve this, future iterations will focus entirely on improving internal algorithm scalability (such as migrating from batch PySpark processing to Spark Structured Streaming for true real-time updates). The pipeline is designed to handle heavier computational loads natively without requiring an increase in team size to manage or maintain the infrastructure.

## 📊 Expected Output
Continuous random log generation stored locally.
Fault-tolerant log storage replicated in Hadoop HDFS.
Clean, structured tabular data processed by Apache Spark.
A generated bar_chart.png visualizing the frequency distribution of system log levels.

## 🎓 Learning Outcomes
Architecting an end-to-end Data Engineering pipeline.
Configuring and deploying Apache Flume for continuous data ingestion.
Managing distributed storage with Hadoop HDFS.
Performing scalable ETL transformations with Apache Spark.
Writing automated, reproducible execution scripts.

## 👨‍💻 Team Members
- Shenouda Aboelrose
- Abdelrahman Ahmed Mohamed
- Mohamed Mo'men Mohamed Abdullah

## 📄 License
This project is created for educational purposes.
