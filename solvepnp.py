import numpy as np
import cv2


dist_coeffs = np.array([
 2.83872654e-01, -1.80751258e+00, -1.74164544e-03,
 -1.21750242e-03, 3.50791161e+00
 ])

mtx1 = [1.21527670e+03, 0.00000000e+00, 5.44046492e+02]
mtx2 = [0.00000000e+00, 1.21987486e+03, 7.19751979e+02]
mtx3 = [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]

mtx = np.array([mtx1,mtx2,mtx3])


mp1 = (-83.75,-48.35,0)
mp2 = (83.75,-48.35,0)
mp3 = (0,96.71,0)
mp4 = (0,0,0)

markerPoints = np.array([mp1,mp2,mp3,mp4])

#Xdirection----------------------------------------------------------------

#533.jpg
mpp1 = (403.0,741.0)
mpp2 = (677.0,748.0)
mpp3 = (545.0,506.0)
mpp4 = (542.0,666.0)


markerPointsonPC533 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec, tvec533 = cv2.solvePnP(
markerPoints, markerPointsonPC533, mtx, dist_coeffs
)

#534.jpg
mpp1 = (572.0,744.0)
mpp2 = (850.0,742.0)
mpp3 = (709.0,504.0)
mpp4 = (709.0,663.0)


markerPointsonPC534 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec534, tvec534 = cv2.solvePnP(
markerPoints, markerPointsonPC534, mtx, dist_coeffs
)

print(tvec533)
print(tvec534)

#Ydirection----------------------------------------------------------------

#537.jpg
mpp1 = (417.0,845.0)
mpp2 = (692.0,845.0)
mpp3 = (553.0,608.0)
mpp4 = (555.0,766.0)


markerPointsonPC537 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec537, tvec537 = cv2.solvePnP(
markerPoints, markerPointsonPC537, mtx, dist_coeffs
)


#538.jpg
mpp1 = (402.0,668.0)
mpp2 = (677.0,668.0)
mpp3 = (540.0,428.0)
mpp4 = (540.0,590.0)

markerPointsonPC538 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec538, tvec538 = cv2.solvePnP(
markerPoints, markerPointsonPC538, mtx, dist_coeffs
)

print(tvec537)
print(tvec538)

#Zdirection----------------------------------------------------------------

#563.jpg
mpp1 = (421.0,813.0)
mpp2 = (686.0,813.0)
mpp3 = (554.0,582.0)
mpp4 = (553.0,736.0)


markerPointsonPC563 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec563, tvec563 = cv2.solvePnP(
markerPoints, markerPointsonPC563, mtx, dist_coeffs
)


#565.jpg
mpp1 = (414.0,817.0)
mpp2 = (688.0,822.0)
mpp3 = (554.0,583.0)
mpp4 = (552.0,741.0)

markerPointsonPC565 = np.array([mpp1, mpp2,mpp3,mpp4])

ret, rvec565, tvec565 = cv2.solvePnP(
markerPoints, markerPointsonPC565, mtx, dist_coeffs
)

print(tvec563)
print(tvec565)
