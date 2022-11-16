import cv2
import time
import shutil
import requests
from deepface import DeepFace




while True:
    url = f"http://192.168.1.5/capture?_cb={time.time()}"

    response = requests.get(url, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    frame = cv2.imread("img.png")
    cv2.imshow('Frame', frame)
    # read image
    img = cv2.imread('img.jpg')

    # storing the result
    result = DeepFace.analyze(img, actions=['emotion'])

    # print result
    print(result)
    url = f"http://192.168.1.5/{result['dominant_emotion']}"
    requests.get(url)

    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
