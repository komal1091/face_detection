# import cv2

# from mtcnn import MTCNN

# detector = MTCNN()

# img = cv2.imread("c:\\Users\\Admin\\Desktop\\test2.jpg")

# output = detector.detect_faces(img)
# print(output)
# print(len(output),"&&&&&&&&&&&&&&&&")

# for i in range (0,len(output)):
#     x,y,width,height = output[i]["box"]
#     cv2.rectangle(img,pt1=(x,y),pt2=(x+width,y+height),color=(0,0,255),thickness=2)

#     # x,y,width,height = output[1]["box"]
#     # cv2.rectangle(img,pt1=(x,y),pt2=(x+width,y+height),color=(0,0,255),thickness=2)

    
# cv2.imshow("window",img)
# cv2.waitKey(0)




import cv2
import os
from mtcnn import MTCNN

# Initialize the MTCNN detector
detector = MTCNN()

# Function to detect faces in an image
def detect_faces(image_path):
    # Read the image
    img = cv2.imread(image_path)
    # Detect faces
    output = detector.detect_faces(img)
    # Draw bounding boxes around detected faces
    for face in output:
        x, y, width, height = face["box"]
        cv2.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(0, 0, 255), thickness=2)
    # Display the image with bounding boxes
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Directory containing images
root_folder = "c:\\Users\\Admin\\Desktop\\images"

# Function to traverse through directories and process images
def process_images_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Check if the file is an image (you can add more extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Get the full path of the image
                image_path = os.path.join(root, file)
                # Detect faces in the image
                detect_faces(image_path)

# Call the function to process images in the root folder and its subfolders
process_images_in_folder(root_folder)



# import cv2
# import os
# from mtcnn import MTCNN

# # Initialize the MTCNN detector
# detector = MTCNN()

# # Function to detect faces in an image with a confidence threshold
# def detect_faces(image_path, confidence_threshold=0.5):
#     # Read the image
#     img = cv2.imread(image_path)
#     # Detect faces
#     output = detector.detect_faces(img)
#     # Draw bounding boxes around detected faces with confidence above the threshold
#     for face in output:
#         if face['confidence'] >= confidence_threshold:
#             x, y, width, height = face["box"]
#             cv2.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(0, 0, 255), thickness=2)
#     # Display the image with bounding boxes
#     cv2.imshow("window", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Directory containing images
# root_folder = "c:\\Users\\Admin\\Desktop\\images"

# # Function to traverse through directories and process images
# def process_images_in_folder(folder):
#     for root, dirs, files in os.walk(folder):
#         for file in files:
#             # Check if the file is an image (you can add more extensions if needed)
#             if file.lower().endswith(('.png', '.jpg', '.jpeg')):
#                 # Get the full path of the image
#                 image_path = os.path.join(root, file)
#                 # Detect faces in the image
#                 detect_faces(image_path)

# # Call the function to process images in the root folder and its subfolders
# process_images_in_folder(root_folder)





import cv2
import os
from mtcnn import MTCNN

# Initialize the MTCNN detector
detector = MTCNN()

# Function to detect faces in an image with confidence levels as percentages
def detect_faces(image_path, confidence_threshold=0.5):
    # Read the image
    img = cv2.imread(image_path)
    # Detect faces
    output = detector.detect_faces(img)
    # Draw bounding boxes around detected faces with confidence above the threshold
    for face in output:
        confidence = face['confidence'] * 100  # Convert confidence to percentage
        if confidence >= confidence_threshold:
            x, y, width, height = face["box"]
            cv2.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(0, 0, 255), thickness=2)
            # Display confidence level as percentage
            cv2.putText(img, f'{confidence:.2f}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    # Display the image with bounding boxes
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Directory containing images
root_folder = "c:\\Users\\Admin\\Desktop\\images"

# Function to traverse through directories and process images
def process_images_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Check if the file is an image (you can add more extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Get the full path of the image
                image_path = os.path.join(root, file)
                # Detect faces in the image
                detect_faces(image_path)

# Call the function to process images in the root folder and its subfolders
process_images_in_folder(root_folder)
