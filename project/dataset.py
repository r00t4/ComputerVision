import pandas as pd
import numpy as np
import cv2

import torch
from torch.utils.data import Dataset

class Dataset(Dataset):

	def __init__(self):
		self.csv = pd.read_csv('./cat_data1.csv')

	def __len__(self):
		return len(self.csv)

	def __getitem__(self, ind):
		X = self.csv.iloc[ind][18:].values
		X = X.reshape(3, 100, 100)
		# print(X)
		Y = self.csv.iloc[ind][:18].values
		# print(X)
		# print(Y.astype('float').reshape(-1, 18))

		X = torch.from_numpy(X).float()
		Y = torch.from_numpy(Y).float()
		return X, Y

