import cv2
import numpy as np

def main():
    # Input image file path
    image_path = "input2.jpg"  # Provide the path to your image file

    # Load the image
    image = cv2.imread(image_path, 0)

    if image is None:
        print('Image not found.')
        return

    # Display the original image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Define transformation parameters
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # Translate 50 pixels right and 30 pixels down
    rotation_angle = 45  # Rotate by 45 degrees
    scaling_factors = (2, 2)  # Scale by a factor of 2 in both x and y directions
    shearing_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shear in the x-direction

    # Apply the transformations
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1), (image.shape[1], image.shape[0]))
    scaled_image = cv2.resize(image, None, fx=scaling_factors[0], fy=scaling_factors[1])
    sheared_image = cv2.warpAffine(image, shearing_matrix, (image.shape[1], image.shape[0]))

    # Display the transformed images
    cv2.imshow('Translated Image', translated_image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.imshow('Scaled Image', scaled_image)
    cv2.imshow('Sheared Image', sheared_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
