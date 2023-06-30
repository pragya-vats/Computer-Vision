import cv2
import rembg

# Load input image
input_image = cv2.imread('1.jpg')

while True:
    input_image = cv2.resize(input_image, (960, 540))
    # Show input image and allow user to select ROI
    roi = cv2.selectROI('Select ROI', input_image)
    x, y, w, h = roi

    # Crop ROI from input image and pass it to rembg to remove background
    roi_image = input_image[y:y+h, x:x+w]
    output_image = rembg.remove(roi_image)

    # Convert output image to grayscale and apply threshold to convert it to binary
    gray_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)
    ret, binary_image = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)

    # Find contours of object in binary image
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on ROI image to create object outline
    cv2.drawContours(roi_image, contours, -1, (0, 255, 0), 2)

    # Blend ROI image with input image
    alpha = 0.5
    beta = 1.0 - alpha
    output_image = cv2.addWeighted(roi_image, alpha, input_image[y:y+h, x:x+w], beta, 0.0)

    # Display input image with object outline overlaid on it
    cv2.imshow('Output', output_image)

    # Wait for key press
    key = cv2.waitKey(0)


    # Exit loop if 'q' key is pressed
    if key == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
