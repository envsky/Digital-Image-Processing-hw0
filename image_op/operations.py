import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        
        # add your code here
        ilrow = len(image_left)
        ilcol = column
        ircol = len(image_right[0])

        merged_image = np.zeros((ilrow, ircol), dtype=np.float64)

        for i in range(0, ilrow):
            for j in range(0, ilcol):
                merged_image[i][j] = image_left[i][j]

        for i in range(0, ilrow):
            for j in range(ilcol, ircol):
                merged_image[i][j] = image_right[i][j]


        # Please do not change the structure
        return merged_image  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        row = len(input_image)
        col = len(input_image[0])

        scaled_image = np.zeros((row, col), dtype=np.float64)

        for i in range(0, row):
            for j in range(0, column):
                scaled_image[i][j] = input_image[i][j] * alpha

        for i in range(0, row):
            for j in range(column, col):
                scaled_image[i][j] = input_image[i][j] * beta

        # Please do not change the structure
        return scaled_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here
        row = len(input_image)
        col = len(input_image[0])

        ml = 0
        mr = 0
        count = 0

        centralized_image = np.zeros((row, col), dtype=np.float64)

        for i in range(0, row):
            for j in range(0, column):
                ml += input_image[i][j]
                count += 1

        ml = ml / count
        count = 0

        for i in range(0, row):
            for j in range(column, col):
                mr += input_image[i][j]
                count += 1

        mr = mr / count

        offsetl = 128 - ml
        offsetr = 128 - mr

        pixel = 0

        for i in range(0, row):
            for j in range(0, column):
                pixel = input_image[i][j] + offsetl
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255

                centralized_image[i][j] = pixel

        for i in range(0, row):
            for j in range(column, col):
                pixel = input_image[i][j] + offsetr
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255

                centralized_image[i][j] = pixel

        return centralized_image   # Currently the input image is returned, please replace this with the centralized image
