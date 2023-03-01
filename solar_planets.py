import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (80, 50),
    cv2.FONT_HERSHEY_TRIPLEX,
    1.2,
    (0, 255, 255)   
)

cv2.putText(
    img,
    "Mercury",
    (110, 190),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (192, 192, 192)
)

cv2.putText(
    img,
    "Venus",
    (205, 260),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (135, 206, 235)

)

cv2.putText(
    img,
    "Earth",
    (300, 265),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.55,
    #(144, 238, 144),
    (180, 213, 48)
)

cv2.putText(
    img,
    "Mars",
    (395, 255),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.55,
    (68, 74, 230)
)

cv2.putText(
    img,
    "Jupiter",
    (530, 55),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.8,
    (0, 125, 255)
)

cv2.putText(
    img,
    "Saturn",
    (750, 120),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.65,
    (208, 185, 254)
)

cv2.putText(
    img,
    "Uranus",
    (940, 140),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Neptune",
    (1080, 145),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (255, 105, 40)
)

cv2.imwrite("S.jpg", img)

cv2.imshow("S.jpg", img)

cv2.waitKey(0)