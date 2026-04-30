"""
click_points.py
---------------
Based on Listing 1 from the assignment.
Run this from the terminal before running the Q3 notebook:

    python click_points.py

Click 6 corresponding points on c1, then the same 6 on c2.
Points are saved to points.npz for use in the notebook.
"""

import cv2 as cv
import numpy as np

N = 6        # number of points (assignment uses 5, we use 6 for better homography)
global n
n = 0

p1 = np.empty((N, 2))
p2 = np.empty((N, 2))

# mouse callback function — same as Listing 1
def draw_circle(event, x, y, flags, param):
    global n
    p = param[0]
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(param[1], (x, y), 5, (255, 0, 0), -1)
        p[n] = (x, y)
        n += 1

# image paths updated to match our folder structure
im1 = cv.imread('c1.jpg', cv.IMREAD_REDUCED_COLOR_4)
im2 = cv.imread('c2.jpg', cv.IMREAD_REDUCED_COLOR_4)

im1copy = im1.copy()
im2copy = im2.copy()

# ── Click on Image 1 (c1) ─────────────────────────────────────────────────────
cv.namedWindow('Image 1', cv.WINDOW_AUTOSIZE)
param = [p1, im1copy]
cv.setMouseCallback('Image 1', draw_circle, param)

while (1):
    cv.imshow('Image 1', im1copy)
    if n == N:
        break
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()

# ── Click on Image 2 (c2) ─────────────────────────────────────────────────────
param = [p2, im2copy]
n = 0

cv.namedWindow('Image 2', cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('Image 2', draw_circle, param)

while (1):
    cv.imshow('Image 2', im2copy)
    if n == N:
        break
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()

# ── Print and save — same as Listing 1 + save step ───────────────────────────
print(p1)
print(p2)

# Save points for use in the notebook
np.savez('points.npz', pts1=p1, pts2=p2)
print('Points saved to points.npz')
