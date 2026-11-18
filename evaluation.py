import numpy as np 

# accuracy 
def calculate_accuracy(predictions: np.ndarray, labels: np.ndarray): 
    correct_predictions = np.sum(predictions == labels) 
    accuracy = (correct_predictions / len(labels)) * 100 
    return accuracy

# sensitivity
def calculate_sensitivity(predictions: np.ndarray, labels: np.ndarray):
  tp = 0
  fn = 0
  for i in range(len(predictions)):
    if labels[i] == 1 and predictions[i] == 1:
      tp += 1
    elif labels[i] == 1 and predictions[i] == 0:
      fn += 1
  denom = tp + fn
  return tp / denom if denom > 0 else 0.0

# precision
def calculate_precision(predictions: np.ndarray, labels: np.ndarray): 
   tp = 0 
   fp = 0
   for i in range(len(predictions)):
      if labels[i] == 1 and predictions[i] == 1: 
         tp += 1 
      elif labels[i] == 0 and predictions[i] == 1: 
         fp += 1
   denom = tp + fp
   return tp / denom if denom > 0 else 0.0

# f score
def calculate_f1(predictions: np.ndarray, labels: np.ndarray):
   sensitivity =  calculate_sensitivity(predictions, labels)
   precision =  calculate_precision(predictions, labels)
   denom = precision + sensitivity
   return (2 * sensitivity * precision) / denom if denom > 0 else 0.0






