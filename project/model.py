import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self, num_classes=18):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0))
        self.layer2 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0))
        self.fc = nn.Linear(128 * 25 * 25, num_classes)

    def forward(self, x):
        # print('1')
        # print(x.shape)
        out = self.layer1(x)
        # print('2')
        # print(out.shape)
        out = self.layer2(out)
        # print(out.shape)
        out = out.view(-1, 128 * 25 * 25)
        # print('3')
        # print(out.shape)
        out = self.fc(out)
        # print('4')
        # print(out.shape)
        return out
