import numpy as np
import torch
import joblib
import json
from sklearn.preprocessing import MinMaxScaler
import torch.nn as nn
from scipy.stats import norm
from sklearn.metrics import mean_absolute_error


class AnomalyDetectionLSTM(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(AnomalyDetectionLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])
        return output

def check_over_cont_window(data, window=14, tol=2):

  size = len(data)
  if size<window+1:
    print(f"Needs atleast {window+1} days previous data")
    return False

  # Calculate mean and standard deviation
  mean_value = np.mean(data[-(window+1):-1])
  std_deviation = np.std(data[-(window+1):-1])

  # Check if the last value is 3 standard deviations away from the mean
  last_value = data[-1]
  deviation_threshold = tol * std_deviation

  if abs(last_value - mean_value) > deviation_threshold:
      return True
  else:
      return False


def check_over_same_day(data, window=15, tol=2):
  cur_data = data[-1]
  data = data[:-1]
  size = len(data)
  if size < 105:
    print("Not enough data to make a prediction. Need at least 105 days of data.")
    return False

  days = (size) - np.arange(1, 105, 7)
  days = np.sort(days)
  # Calculate mean of values from the same day of the week 7 days before
  window_mean = data[days].mean()
  window_std = data[days].std()


  # Check if the last value is greater than the mean of values from the same day of the week 7 days before
  if abs(cur_data-window_mean) > tol*window_std:
    return True
  else:
    return False
  

def fit_gaussian_distribution(errors):
    mu, std = norm.fit(errors)
    return mu, std

def load_scaler_and_model(scaler_path, model_path, input_size, hidden_size):
  scaler = joblib.load(scaler_path)
  model = AnomalyDetectionLSTM(input_size, hidden_size)
  model.load_state_dict(torch.load(model_path))
  return scaler, model


def is_last_point_anomaly(data, scaler, model, window_size=100, threshold=0.02):
  if len(data) >= window_size:
      data = np.array(data)
      # Slice the data from the end with size window+1
      input_data = data[-(window_size + 1):-1]
      # input_data_scaled = scaler.transform(input_data.reshape(-1, 1)).astype(np.float32)
      # print(input_data.shape)
      input_data_scaled = torch.tensor(input_data.reshape(1, -1, 1).astype(np.float32))
      
      with torch.no_grad():
          model.eval()
          prediction = model(input_data_scaled)
          error = np.abs(prediction.numpy().flatten() - data[-1])
          gaussian_parms = json.load(open("gaussian_config.json", "r"))
          mu, std = float(gaussian_parms["mu"]), float(gaussian_parms["std"])
          probability = norm.pdf(error[-1], mu, std)
          is_anomaly = probability < threshold

      return is_anomaly
  else:
      return "Error: Atleast {} data points needed".format(window_size)