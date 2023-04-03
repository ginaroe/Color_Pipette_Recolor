import cv2
import numpy as np
from sklearn.neighbors import NearestNeighbors
from palette_image import csv2list, list2np

def nearest(image_path, csv_path, result_path):
    image = cv2.imread(image_path)
    r, c = image.shape[:2]
    image_values = np.asarray([[(i[0], i[1], i[2]) for i in j] for j in image]).reshape(r*c, 3)
    palette_list = csv2list(csv_path)
    palette_np = list2np(palette_list)
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(palette_list)
    distances, indices = nbrs.kneighbors(image_values)
    indices = np.asarray(indices).reshape(r, c)

    screen = np.zeros((r,c,3), np.uint8)
    screen[:,:] = palette_np[indices[:,:]]

    while True:
         
        cv2.imshow('recolor', screen)
        if cv2.waitKey(10) == 27: break

    cv2.imwrite(result_path, screen)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("image_path: ")
    csv_path = input("csv_path: ")
    result_path = input("result_path: ")

    nearest(image_path, csv_path, result_path)