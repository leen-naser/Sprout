import cv2

camera = cv2.VideoCapture(2)

if not camera.isOpened():
    print("Could not open webcam.")
else:
    print("Webcam opened successfully!")

    success, frame = camera.read()

    if success:
        cv2.imwrite("test_images/webcam_test.jpg", frame)
        print("Photo captured successfully!")
    else:
        print("Webcam opened, but could not capture a frame.")

camera.release()
