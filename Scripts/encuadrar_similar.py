# -*- coding: utf-8 -*-
"""Encuadrar_similar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/149ys78gqh-Dno8KGCQmHTCwtC97hr_DQ

# Image Alignment
**Satya Mallick, LearnOpenCV.com**
"""

def similarBox(template,input):
  # Imports
  import cv2
  import numpy as np

  """## Step 1: Read Tempalate and Scanned Image"""

  # Read reference image
  refFilename = template
  print("Reading reference image : ", refFilename)
  im1 = cv2.imread(refFilename)
  #im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)


  # Read image to be aligned
  imFilename = input
  print("Reading image to align : ", imFilename)
  im2 = cv2.imread(imFilename)
  #im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)


  """## Step 2: Find keypoints in both Images

  Think of keypoints as corner points that are stable under image transformations
  """

  # Convert images to grayscale
  im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    

  # Detect ORB features and compute descriptors.
  MAX_NUM_FEATURES = 1000
  orb = cv2.ORB_create(MAX_NUM_FEATURES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1_gray, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2_gray, None)

  # Display 
  im1_display = cv2.drawKeypoints(im1, keypoints1, outImage=np.array([]), color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  im2_display = cv2.drawKeypoints(im2, keypoints2, outImage=np.array([]), color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  """## Step 3 : Match keypoints in the two image"""

  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
    
  # Sort matches by score
  matches.sort(key=lambda x: x.distance, reverse=False)

  # Remove not so good matches
  numGoodMatches = int(len(matches) * 0.05)
  matches = matches[:numGoodMatches]

  # Draw top matches
  im_matches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)

  plt.figure(figsize=[40,10])
  plt.imshow(im_matches); plt.axis('off'); plt.title("Original Form");

  """## Step 4:  Find Homography"""

  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
    
  # Find homography
  h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

  """## Step 5: Warp image"""

  # Use homography to warp image
  height, width, channels = im1.shape
  im2_reg = cv2.warpPerspective(im2, h, (width, height))

  imageFileName = input.split("/")[-1]
  path = input.split("/")
  path.pop(-1)
  nombre = ("boxed_"+imageFileName)
  path = '/'.join(path)
  path = os.path.join(path,nombre)
  cv.imwrite(path,opening)
  print("Imagen encuadrada")
  return path


plantilla = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/template_matricula.jpeg"
imagen = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/matricula.jpeg"
similarBox(plantilla, imagen)
