import cv2
import base64

cam = cv2.VideoCapture(0)

if not cam.isOpened():
  print("Camera cannot be opened")
  exit()

def convert(frame):
  name = 'output.png'
  output = cv2.imwrite(name, frame)

  if not output:
    print("Could not save image!")
  else:
    with open("output.png", "rb") as img:
      s = base64.b64encode(img.read())
    with open('encode.bin', "wb") as f:
      f.write(s)

    print(s)
    
fred = True
while fred:
  fred = False
  ret, frame = cam.read()

  if not ret:
    print("can't receive frame (stream ended?). Exiting...")
    break

  frame = cv2.flip(frame, 1)
  cv2.imshow("Camera Feed", frame)

  convert(frame)

  if cv2.waitKey(5) == 27:
    break

cam.release()
cv2.destroyAllWindows()