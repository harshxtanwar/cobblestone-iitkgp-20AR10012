# SERVER
import matplotlib
matplotlib.use('TkAgg')

import socket
import pandas as pd
import json
from utils import *
import matplotlib.pyplot as plt
import time

HOST = ''
PORT = 5051

# Generate the data
# data = add_trend(trend_type=1.15, coeff=0.2) + add_pattern(exp1=2, exp2=1, window=30) + add_white_noise() + event(cd_begin=-900, trend_type=1.8, coeff=-0.15, window=80) + event(cd_begin=-1500, trend_type=1.5, coeff=10, window=20)

data = json.load(open("data.json", "r"))["data"]
data_points = []
anomaly_points = []
data_points_iterator = iter(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("socket successfully created")
    s.bind((HOST, PORT))
    print("socket bind to %s" % (PORT))

    s.listen(2)
    print("socket is listening")
    
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            try:
                # Get the next data point from the DataFrame
                data_point = next(data_points_iterator)
                data_points.append(data_point)
                # Convert the data point to bytes and send it to the client
                conn.sendall(str(data_point).encode('utf-8'))
                
                # Receive the response from the client
                client_response = conn.recv(1024).decode("utf-8")
                print(type(client_response), client_response)
                client_response = json.loads(client_response)
                is_anomaly = client_response["is_anomaly"]
                
                if "True" in is_anomaly:

                    anomaly_points.append(len(data_points)-1)
                # Plot actual data and predicted values
                if len(data_points)%100 == 0:
                    plt.figure(figsize=(12, 6))
                    plt.plot(data_points, label='Actual Data', color='blue', linewidth=2)

                    # Highlight anomalies as red straight lines
                    anomaly_indices = anomaly_points
                    for idx in anomaly_indices:
                        plt.axvline(x=idx, color='red', linestyle='--', linewidth=2, label='Anomaly')

                    plt.title('Actual Data vs. Predicted Values with Anomalies')
                    plt.xlabel('Time Step')
                    plt.ylabel('Value')
                    plt.legend(['Data', 'Anomaly'])
                    plt.pause(0.05)
                    plt.show(block=False)
                    plt.close(len(data_points)//100 - 1)


                
            except StopIteration:
                print('All data points sent. Closing connection.')
                break
        plt.savefig(f"plot_{len(data_points)//100}.png")  # Save plot to a file
        plt.close() 