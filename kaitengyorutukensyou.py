import numpy as np
import cv2
import math

dist_coeffs = np.array([
2.83872654e-01, -1.80751258e+00,
-1.74164544e-03, -1.21750242e-03, 3.50791161e+00
])

mtx1 = [1.21527670e+03, 0.00000000e+00, 5.44046492e+02]
mtx2 = [0.00000000e+00, 1.21987486e+03, 7.19751979e+02]
mtx3 = [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]

mtx = np.array([mtx1,mtx2,mtx3])

mp1 = (-83.75,-47.78,0)
mp2 = (83.75,-47.78,0)
mp3 = (0,145.06,0)
mp4 = (0,0,0)


markerPoints = np.array([mp1,mp2,mp3,mp4])

#初期位置
#522.jpg
mpp1 = (418.0,814.0)
mpp2 = (693.0,809.0)
mpp3 = (552.0,573.0)
mpp4 = (554.0,732.0)

markerPointsonPC = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec, tvec = cv2.solvePnP(
markerPoints, markerPointsonPC, mtx, dist_coeffs
)

R = cv2.Rodrigues(rvec)[0]

proj_matrix = np.hstack((R, tvec))
euler_angle_begin = cv2.decomposeProjectionMatrix(proj_matrix)[6]
print("XRbegin,YRbegin,ZRbegin")
print(str(euler_angle_begin[0]),
str(euler_angle_begin[1]),
str(euler_angle_begin[2]))
