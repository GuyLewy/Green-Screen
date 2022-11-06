import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


backgroundImage = mpimg.imread("max-mckinnon-c9OCWLka764-unsplash.jpg")
forgroundImage = mpimg.imread("greenscreen.jpg")
error = 20

finalImage = forgroundImage.copy()


def ReplaceGreenWithImage():
    if (backgroundImage.shape != forgroundImage.shape):
        Wstart = int((backgroundImage.shape[0]-forgroundImage.shape[0])/2)
        Hstart = int((backgroundImage.shape[1]-forgroundImage.shape[1])/2)

    else:
        Wstart = 0
        Hstart = 0

    for i in range(len(forgroundImage)):
        for k in range(len(forgroundImage[i])):
            if (forgroundImage[i, k, 0] >= 78-error & forgroundImage[i, k, 0] <= 78+error & forgroundImage[i, k, 1] >= 255-error & forgroundImage[i, k, 2] <= 0+error):
                finalImage[i, k, :] = backgroundImage[i +
                                                      Wstart, k + Hstart, :]

            else:
                finalImage[i, k, :] = forgroundImage[i, k, :]
        print(i)

    plt.imshow(finalImage)
    plt.savefig("final-image.jpg")
    plt.show()


ReplaceGreenWithImage()
