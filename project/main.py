import numpy as np
import cv2

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from dataset import Dataset
from model import NeuralNetwork

batch_size = 64
train_dataset = Dataset()
data_loader = DataLoader(train_dataset,
                         shuffle=True,
                         batch_size=batch_size)

net = NeuralNetwork()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.0001)

nepoch = 20
for epoch in range(nepoch):
    running_loss = 0.0
    for X, Y in data_loader:
        optimizer.zero_grad()

        pred = net(X)

        loss = criterion(pred, Y)

        # loss.backward()
        # optimizer.step()

        running_loss += loss.item()
        print("loss:" + str(loss))

    running_loss /= len(data_loader)
    print(running_loss)

torch.save(net.state_dict(), './model.pth')
