import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

def main():
    # Upload an image
    uploaded = files.upload()

    if len(uploaded) == 0:
        print('No image uploaded.')
        return

    # Load the uploaded image
    image = cv2.imread(list(uploaded.keys())[0], 0)

    if image is None:
        print('Image not found.')
        return

    # Save the uploaded image as 'input.jpg' (overwrite if it already exists)
    cv2.imwrite('input.jpg', image)

    # Display the original image
    cv2_imshow(image)

    # Define transformation parameters
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # Translate 50 pixels right and 30 pixels down
    rotation_angle = 45  # Rotate by 45 degrees
    scaling_factors = (2, 2)  # Scale by a factor of 2 in both x and y directions
    shearing_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shear in x-direction

    # Apply the transformations
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1), (image.shape[1], image.shape[0]))
    scaled_image = cv2.resize(image, None, fx=scaling_factors[0], fy=scaling_factors[1])
    sheared_image = cv2.warpAffine(image, shearing_matrix, (image.shape[1], image.shape[0]))

    # Display the transformed images
    cv2_imshow(translated_image)
    cv2_imshow(rotated_image)
    cv2_imshow(scaled_image)
    cv2_imshow(sheared_image)

if __name__ == "__main__":
    main()
