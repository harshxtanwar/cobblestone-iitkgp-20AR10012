# CLIENT
import socket
from anomaly import *

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5051  # The port used by the server
WINDOW = 20

class data_window:
  def __init__(self):
    self.data = []
    
  def insert(self, pt):
    if len(self.data) < WINDOW*7+1:
      self.data.append(pt)
    else:
      self.data[:-1] = self.data[1:]
      self.data[-1] = pt

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    return self.data[idx]


data = data_window()
scaler, model = load_scaler_and_model('models/scaler.joblib', 'models/lstm_model.pth', 1, 50)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        # Receive the data point from the server
        signal = s.recv(1024).decode('utf-8')
        if not signal:
            break
        print('Received data point:', signal)
        data.insert(float(signal))

        is_anomaly = is_last_point_anomaly(data, scaler, model, threshold=0.5)
      
        print(f"Is Anomaly?: {is_anomaly}")
        # Process the data point and send a response to the server
        response = f'{{"response": "Processed: {signal}" , "is_anomaly": \"{str(is_anomaly)}\" }}'
        s.sendall(response.encode('utf-8')) 