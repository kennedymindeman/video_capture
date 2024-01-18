# import the opencv library 
import cv2
import numpy

def main():
    # define a video capture object
    vid = cv2.VideoCapture(1)

    while True:

        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        edge_image = edge_detection(frame)

        # Display the resulting frame
        cv2.imshow('frame', numpy.fliplr(edge_image))

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def edge_detection(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    # what does gaussian blur do?
    # https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
    blur = cv2.GaussianBlur(gray, (1, 1), 0)

    # Run the edge detector on grayscale
    edges = cv2.Canny(blur, 50, 150, apertureSize=3)

    return edges


if __name__ == "__main__":
    main()
