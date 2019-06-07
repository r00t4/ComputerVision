import cv2
import numpy as np
import glob
import torch

from model import NeuralNetwork

net = NeuralNetwork()
net.load_state_dict(torch.load('./model.pth'))

ls = glob.glob('./newdata/*.jpg')
for path in ls:
	img = cv2.imread(path, 0)
	print(img.shape)
	x = img.reshape((1, 784))
	x = torch.from_numpy(x).float()

	pred = net(x)
	pred = pred.data.numpy()
	print(pred[0].argmax())

	cv2.imshow("img", cv2.resize(img, (500, 500)))
	cv2.waitKey(0)