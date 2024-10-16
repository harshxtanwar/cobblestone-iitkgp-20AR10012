# Real-Time Time Series Anomaly Detection

## 1. Summary of Topic: Anomaly Detection
Anomaly detection is the process of identifying unexpected patterns or outliers in data that deviate from the norm. It plays a crucial role in various fields, including finance, healthcare, manufacturing, and cybersecurity, as it helps in:

- **Fraud Detection:** Identifying fraudulent transactions or behaviors.
- **Fault Detection:** Spotting anomalies in machinery that might indicate impending failures.
- **Network Security:** Detecting unusual patterns that may indicate a security breach.
- **Quality Control:** Ensuring products meet quality standards by flagging anomalies during production.

## 2. What Are We Trying to Do
In this project, we aim to implement a real-time anomaly detection system for time series data. The goal is to continuously monitor incoming data, analyze it for anomalies, and visualize the results. By utilizing statistical techniques and machine learning, we can provide insights into the behavior of the system being monitored.

## 3. What Does the Code Exactly Do
The provided code consists of two main components:

- **Server (`server.py`)**: This script simulates a real-time data stream and processes incoming data points for anomaly detection. It:
  - Initializes a socket server to receive data points.
  - Analyzes the received data for anomalies using statistical methods.
  - Generates a plot of the data points and highlights anomalies.

- **Client (`client.py`)**: This script simulates sending data points to the server. It:
  - Sends random floating-point numbers as data points to the server at defined intervals.

The results, including statistical outputs and anomaly indications, are printed in the console, and plots are saved as image files for further analysis.

## 4. Steps to Setup ( for linux only )

### Prerequisites
- Ensure you have Python 3 installed on your Linux environment.
- Install the required packages in a virtual environment to avoid conflicts with system packages.

### Install Required Packages
1. **Install Tkinter**:
   First, install `python3-tk` for Tkinter support:
   `sudo apt-get install python3-tk`

### Prerequisites
- Ensure you have Python 3 installed on your Linux environment.
- Install the required packages in a virtual environment to avoid conflicts with system packages.

### Activate the virtual environment
   `source venv/bin/activate`
### Install the required packages using pip:
pip install -r requirements.txt

### Steps to Run
- Open a terminal and navigate to the project directory.
- Start the server:
`python3 server.py`
- In another terminal, start the client:
`python3 client.py`

### Monitor the console output for anomaly detection results. Check the generated plot images saved in the project directory.



