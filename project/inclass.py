import pandas as pd
import numpy as np
import cv2

df = pd.read_csv('./HWs_hw4_a-z_train.csv')

j = 0
imgid = 0
cnt = 0
for i in range(len(df)):
	if (df.iloc[i][0] == j and cnt < 1):
		img = df.iloc[i][1:].values.reshape(28, 28)
		img = img.astype(np.uint8)

		label = df.iloc[i][0]

		# cv2.imshow("img", img)
		print(label)
		# k = cv2.waitKey(0)
		cv2.imwrite('./newdata/img{}.jpg'.format(imgid), img)
		cnt = cnt + 1
		imgid = imgid + 1
	elif cnt == 1:
		j = j + 1
		cnt = 0

# df.to_csv('./new_a-z_train.csv', index=False)

