import numpy as np
import cv2
import math


mtx1 = [1.21527670e+03, 0.00000000e+00, 5.44046492e+02]
mtx2 = [0.00000000e+00, 1.21987486e+03, 7.19751979e+02]
mtx3 = [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]

mtx = np.array([mtx1,mtx2,mtx3])


mp1 = (-83.75, -48.35, 0)
mp2 = (83.75, -48.35, 0)
mp3 = (0, 96.71, 0)
mp4 = (0, 0, 0)


markerPoints = np.array([mp1,mp2,mp3,mp4])

dist_coeffs = np.array([
 2.83872654e-01, -1.80751258e+00, -1.74164544e-03,
 -1.21750242e-03, 3.50791161e+00])


def distortionAdjust(x, y):
    src = np.array([x,y])
    p = cv2.undistortPoints(src, mtx, dist_coeffs)[0][0]
    center = p
    return center
#left-------------------------------------------------------------
#533.jpg
mpp1 = (513.0, 749.0)
mpp2 = (666.0, 749.0)
mpp3 = (587.0, 749.0)
mpp4 = (590.0, 749.0)

markerPointsonPC533 = np.array([mpp1, mpp2,mpp3,mpp4])
center533 = np.array([mpp4])[0]
ret, vec_rotation533, translation533 = cv2.solvePnP(
markerPoints, markerPointsonPC533, mtx, dist_coeffs
)
center533 = distortionAdjust(*center533)
points533 = np.append(center533, -1.21527670e+03).reshape(3,1)

#rotation-------------------------------------------------------
rotation533 = cv2.Rodrigues(vec_rotation533)[0]
print("rotation533")
print(rotation533)
inv_rotation533 = cv2.invert(rotation533)[1]
a = np.array([-1,1,1]).reshape(3,1)
hoko533 = np.matrix(inv_rotation533) * np.matrix(a)
hoko533 = np.array([hoko533])
print(hoko533)
print(points533)
vec533 = hoko533 * points533
print("vec533")
print(vec533)
print("translation533")
print(translation533)


print("533のZ=0時,t,X,Y")
t = -translation533[2][0] / vec533[0][2][0]
X = vec533[0][0][0] * t + translation533[0][0]
Y = vec533[0][1][0] * t + translation533[1][0]
print(t,X,Y)

#Right-------------------------------------------------------------

#534.jpg
mpp1 = (511.0, 764.0)
mpp2 = (658.0, 764.0)
mpp3 = (595.0, 764.0)
mpp4 = (587.0, 764.0)

markerPointsonPC534 = np.array([mpp1, mpp2,mpp3,mpp4])
center534 = np.array([mpp4])[0]

ret, vec_rotation534, translation534 = cv2.solvePnP(
markerPoints, markerPointsonPC534, mtx, dist_coeffs
)
center534 = distortionAdjust(*center534)

points534 = np.append(center534, -1.21527670e+03).reshape(3,1)


#rotation-------------------------------------------------------
rotation534 = cv2.Rodrigues(vec_rotation534)[0]
print("rotation534")
print(rotation534)
inv_rotation534 = cv2.invert(rotation534)[1]
a = np.array([-1,1,1]).reshape(3,1)
hoko534 = np.matrix(inv_rotation534) * np.matrix(a)
hoko534 = np.array([hoko534]).reshape(3,1)
vec534 = hoko534 * points534
print("vec534")
print(vec534)
print("translation534")
print(translation534)

print("534のZ=0時,t,X,Y")
t = -translation534[2][0] / vec534[2][0]
X = vec534[0][0] * t + translation534[0][0]
Y = vec534[1][0] * t + translation534[1][0]
print(t,X,Y)
