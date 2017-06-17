import sys

import cv2
import numpy as np

from matplotlib import pyplot as plt


class Video:
    def __init__(self, path):
        self.path = path
        self.capture = cv2.VideoCapture(self.path)
        # Eats first frame
        self.h, self.w = self.get_size(self.get_frame())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.capture.release()

    def get_frame(self):
        ret, frame = self.capture.read()
        r = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return r

    def get_size(self, frame):
        h, w = frame.shape
        return (h, w)

    def show(self, frame):
        plt.imshow(frame)
        plt.show()


def averengify(path, skip, grab):
    with Video(path) as v:
        # Create matrix for result
        mat = np.ndarray(shape=(v.h, v.w))

        # Skip n frames
        for n in range(skip):
            v.get_frame()

        # Sum m frames
        for m in range(grab):
            mat = mat + v.get_frame()

        return (mat / grab).astype(int)
        


if __name__ == '__main__':
    name, path, skip, grab = sys.argv
    print(f'Video file:\t{path}\n' \
          f'frames to skip:\t{skip}\n' \
          f'frames to grab:\t{grab}')

    frame = averengify(path, int(skip), int(grab))

    # Save frame
    cv2.imwrite('sum.jpeg', frame)
