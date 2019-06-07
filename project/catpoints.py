import cv2
import pandas as pd
import glob
import csv


#img = cv2.imread('./cats/CAT_00/00000001_000.jpg')
#text_file = open("./cats/CAT_00/00000001_000.jpg.cat", "r")
#lines = text_file.read().split(' ')

cat_id = 1
before = 1000
# from CAT_00 file

for i in range(0,7):
    # path = '.cats/CAT_0{}/'.format(i)
    ls = glob.glob('cats/CAT_0{}/*.jpg'.format(i))
    cnt = 0

    for path in ls:
        if cnt > before:
            break
        cat_path = path + '.cat'
        catfiles = open(cat_path, "r")
        img = cv2.imread(path)
        width = img.shape[1]
        height = img.shape[0]
        dim = (100,100)
        cnt = cnt + 1
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        lines = catfiles.read().split(' ')

        # cv2.waitKey()
        items = []
        to_save_items = []
        tp = -1
        for i in range(1, 19):
            if (tp == -1):
                tp = int((int(lines[i]) * 100 / width) * 100 / 100)
            else:
                items.append((tp, int((int(lines[i]) * 100 / height) * 100 / 100)))
                to_save_items.append(tp)
                to_save_items.append(int((int(lines[i]) * 100 / height) * 100 / 100))
                tp = -1

        print(resized.reshape(1,30000))

        with open('cat_data{}.csv'.format(cat_id), mode='a') as employee_file:
            employee_writer = csv.writer(employee_file)

            to_save_items.extend(resized.ravel())
            employee_writer.writerow(to_save_items)
            



        # print(items)
        # for item in items:
        #     cv2.circle(resized, item, 2, (0,255,0), -1)
        # cv2.imshow('resized',resized)
        # cv2.waitKey()



    

# df = pd.read_csv('./HWs_hw4_a-z_train.csv')

# j = 0
# imgid = 0
# cnt = 0
# for i in range(len(df)):
# 	if (df.iloc[i][0] == j and cnt < 1):
# 		img = df.iloc[i][1:].values.reshape(28, 28)
# 		img = img.astype(np.uint8)

# 		label = df.iloc[i][0]

# 		# cv2.imshow("img", img)
# 		print(label)
# 		# k = cv2.waitKey(0)
# 		cv2.imwrite('./newdata/img{}.jpg'.format(imgid), img)
# 		cnt = cnt + 1
# 		imgid = imgid + 1
# 	elif cnt == 1:
# 		j = j + 1
# 		cnt = 0

# df.to_csv('./new_train.csv', index=False)

# for item in items:
#     cv2.circle(img, item, 3, (0,255,0), -1)

# cv2.imshow('img', img)
# print(items)
# cv2.waitKey()
