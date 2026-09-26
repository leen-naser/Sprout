import cv2


def capture_plant_photo(output_path, camera_index=0):
    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        raise RuntimeError(f"Could not open camera {camera_index}.")

    success, frame = camera.read()
    camera.release()

    if not success:
        raise RuntimeError("Could not capture a frame from the webcam.")

    cv2.imwrite(output_path, frame)

    print(f"Photo captured: {output_path}")
    return output_path


if __name__ == "__main__":
    capture_plant_photo("test_images/webcam_test.jpg", camera_index=2)