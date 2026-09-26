import cv2


def capture_plant_photo(output_path):
    camera = cv2.VideoCapture(2)

    if not camera.isOpened():
        raise RuntimeError("Could not open Logitech Brio 101.")

    success, frame = camera.read()
    camera.release()

    if not success:
        raise RuntimeError("Could not capture a frame from the webcam.")

    cv2.imwrite(output_path, frame)

    print(f"Photo captured: {output_path}")
    return output_path


if __name__ == "__main__":
    capture_plant_photo("test_images/webcam_test.jpg")
