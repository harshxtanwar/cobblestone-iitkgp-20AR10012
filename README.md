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

## Explaination of the graph:
![image](https://github.com/user-attachments/assets/02df6f8d-d9bf-4960-8dd6-352154099bee)

This graph represents a time series analysis where the blue line indicates the actual data values over time, while the red dashed vertical lines highlight the detected anomalies. Here's a breakdown:

X-axis (Time Step): This represents the time or sequence of the data points. The timeline progresses from left to right, showing how values change over time.

Y-axis (Value): This represents the value of the data points. It could represent any metric being tracked, such as temperature, stock prices, or sensor data, depending on the context.

Blue Line (Data): The blue line represents the actual data values or predictions over time. The jagged nature suggests variability in the data with fluctuations both upward and downward.

Red Dashed Lines (Anomalies): The red vertical dashed lines indicate where anomalies have been detected in the time series. Anomalies are points in the data that deviate significantly from the expected pattern. For example:

Spikes or dips in the data.
Changes in trend or behavior.
In this graph, the anomalies are spaced at various intervals, suggesting that unusual behaviors occur at those time steps, potentially signaling a fault, error, or unexpected behavior in the system being monitored.





