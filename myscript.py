%%writefile my_streamlit_app.py
# Paste your Streamlit code here


import cv2
import numpy as np
import streamlit as st

def main():
    st.title("Image Transformations App")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
        st.image(image, caption="Original Image", use_column_width=True)

        transformation_option = st.selectbox("Select Transformation", ["Translate", "Rotate", "Scale", "Shear"])

        if transformation_option == "Translate":
            translate_x = st.slider("Translate X", -100, 100, 0)
            translate_y = st.slider("Translate Y", -100, 100, 0)
            translation_matrix = np.float32([[1, 0, translate_x], [0, 1, translate_y]])
            transformed_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
        elif transformation_option == "Rotate":
            rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
            rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1)
            transformed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
        elif transformation_option == "Scale":
            scaling_factor = st.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1)
            transformed_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)
        elif transformation_option == "Shear":
            shear_x = st.slider("Shear X", -1.0, 1.0, 0.0, 0.01)
            shear_y = st.slider("Shear Y", -1.0, 1.0, 0.0, 0.01)
            shearing_matrix = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
            transformed_image = cv2.warpAffine(image, shearing_matrix, (image.shape[1], image.shape[0]))

        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

if __name__ == "__main__":
    main()
