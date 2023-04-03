import cv2
import numpy as np

def merge_h(im1, im2, r, c):
    '''
    옆으로 두 개 붙이기
    '''
    screen = np.zeros((r, c * 2, 3,), np.uint8)
    screen[:, :c] = im1[:,:]
    screen[:, c:] = im2[:,:]
    return screen

def merge_v(im1, im2, r, c):
    '''
    아래위로 두 개 붙이기
    '''
    screen = np.zeros((r * 2, c, 3,), np.uint8)
    screen[:r, :] = im1[:,:]
    screen[r:, :] = im2[:,:]
    return screen

def merge(path1, path2):
    im1 = cv2.imread(path1)
    im2 = cv2.imread(path2)
    r, c = im1.shape[:2]
    if r >= c:
        return merge_h(im1, im2, r, c)
    else:
        return merge_v(im1, im2, r, c)

def show_save(screen):
    while True:
        cv2.imshow(path3, screen)
        if cv2.waitKey(10) == 27: break
    cv2.destroyAllWindows()
    cv2.imwrite(path3, screen)

if __name__ == "__main__":
    path1 = input("path1: ")
    path2 = input("path2: ")
    path3 = input("path3 ( where to save ): ")

    show_save(merge(path1, path2))