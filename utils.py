import numpy as np


def add_trend(periods=2000, trend_type=1, coeff=0.4):
  time = np.arange(periods)
  values = (time**trend_type)*coeff
  
  return values

def add_pattern(periods=2000, window=10, exp1=3, exp2=2):
  # Just a random pattern
  time = np.arange(window*5)
  values = np.where(time < window, (time*np.random.uniform(low=0, high=0.6))**exp1, ((time-9)*np.random.uniform(low=0, high=0.8))**exp2)
  # Repeat the pattern 5 times
  seasonal = []
  for i in range(periods//50):
      for j in range(50):
          seasonal.append(values[j])

  return seasonal

def add_white_noise(periods=2000, mean=0, std=1, mul=100):
  noise = np.random.normal(mean, std, size=periods)*mul

  return noise

def event(periods=2000, cd_begin=-500, window=50, trend_type=1, coeff=-10):
  event = np.zeros(periods)
  event[cd_begin:cd_begin+window] = add_trend(window, trend_type, coeff)
  event[cd_begin+window:cd_begin+2*window] = add_trend(window, trend_type, coeff)[::-1][:len(event[cd_begin+window:cd_begin+2*window])]

  return event