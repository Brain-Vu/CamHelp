import cv2
cam = cv2.VideoCapture(0)

if not cam.isOpened():
  print("Camera cannot be opened")
  exit()

while True:
  ret, frame = cam.read()

  if not ret:
    print("can't receive frame (stream ended?). Exiting...")
    break

  frame = cv2.flip(frame, 1)
  cv2.imshow("Camera Feed", frame)

  if cv2.waitKey(5) == 27:
    break

cam.release()
cv2.destroyAllWindows()