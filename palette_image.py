import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def csv2list(csv_path:str):
    df = pd.read_csv(csv_path)
    palette_list = df.loc[:].values.tolist()
    return palette_list

def csv2scatter(csv_path:str):
    df = pd.read_csv(csv_path)
    B = df['B']
    G = df['G']
    R = df['R']
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title("Distribution of non/Pretty Colors")
    ax.scatter(B, G, R)

    plt.show()

def list2np(palette_list:list):
    return np.asarray(palette_list)

def list2image(palette_list:list):
    colors = len(palette_list)
    screen = np.zeros((100, 100 * colors, 3), np.uint8)
    for color in range(colors):
        screen[:, color*100 : color*100 + 100] = palette_list[color]
    return screen

if __name__ == "__main__":
    csv_path = input("csv_path: ")
    palette_path = input("palette_path: ")

    palette_list = csv2list(csv_path)
    palette_np = list2np(palette_list)
    print(palette_np.shape)
    print(palette_np)

    screen = list2image(palette_list)
    while True:
        cv2.imshow("palette", screen)
        if cv2.waitKey(10) == 27: break
    cv2.imwrite(palette_path, screen)

    csv2scatter(csv_path)

    cv2.destroyAllWindows()