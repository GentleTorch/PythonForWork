import os
import cv2 as cv


def scan_file(directory):
    file_list = []

    for root, sub_dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


file_list = scan_file("./images")

cnt = 1
for path in file_list:
    frame = cv.imread(path)
    print("Processing: " + path)
    cv.imwrite(os.path.join("./afterImg/", str(cnt) + '.jpg'), frame)
    cnt += 1
