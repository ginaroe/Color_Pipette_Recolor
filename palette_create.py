import cv2
import numpy as np

def init_file(csv_path:str):
    '''
    initializing csv file with BGR columns
    '''
    f = open(csv_path, 'w')
    f.write("B,G,R")
    f.write('\n')
    f.close()

def write2file(B:int, G:int, R:int, csv_path:str):
    '''
    save selected color values in the file
    '''
    f = open(csv_path, 'a')
    f.write(f"{B},{G},{R}")
    f.write('\n')
    f.close()

def image2csv(event, x, y, flags, param):
    '''
    mouse callback function
    '''

    B = image[y, x][0]
    G = image[y, x][1]
    R = image[y, x][2]
    color_explore[:] = (B, G, R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected[:] = (B, G, R)

    if event == cv2.EVENT_RBUTTONDOWN:
        B = color_selected[10,10][0]
        G = color_selected[10,10][1]
        R = color_selected[10,10][2]
        print(f"Blue: {B}           Green: {G}          Red: {R}")
        print(f"Blue: {hex(B)}      Green: {hex(G)}     Red: {hex(R)}")
        write2file(B, G, R, csv_path)

if __name__ == "__main__":

    image_path = input("image_path: ")
    csv_path = input("csv_path: ")

    color_explore = np.zeros((100,100,3), np.uint8)
    color_selected = np.zeros((100,100,3), np.uint8)
    image = cv2.imread(image_path)

    init_file(csv_path)

    cv2.namedWindow("color_explore")
    cv2.namedWindow("color_selected")
    cv2.namedWindow("image")
    
    cv2.setMouseCallback('image', image2csv)

    while True:   
        cv2.imshow('image', image)
        cv2.imshow('color_explore', color_explore)
        cv2.imshow('color_selected', color_selected)
        if cv2.waitKey(10) == 27: break

    cv2.destroyAllWindows()