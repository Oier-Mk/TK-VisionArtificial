# Imports
import cv2
from cv2 import idft
import numpy as np
import matplotlib.pyplot as plt

def detectAndCrop(referencePath, idPath):

  """## Step 1: Read Tempalate and Scanned Image"""

  # Read reference image
  reference = cv2.imread(referencePath)
  reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)

  # Read image to be aligned
  id = cv2.imread(idPath, cv2.IMREAD_COLOR)
  id = cv2.cvtColor(id, cv2.COLOR_BGR2RGB)

  """## Step 2: Find keypoints in both Images Think of keypoints as corner points that are stable under image transformations """

  # Convert images to grayscale
  reference = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
  id = cv2.cvtColor(id, cv2.COLOR_BGR2GRAY)

  # Detect ORB features and compute descriptors.
  MAX_NUM_FEATURES = 1000
  orb = cv2.ORB_create(MAX_NUM_FEATURES)
  keypoints1, descriptors1 = orb.detectAndCompute(reference, None)
  keypoints2, descriptors2 = orb.detectAndCompute(id, None)

  """## Step 3 : Match keypoints in the two image"""

  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
    
  # Sort matches by score
  matches = sorted(matches, key=lambda x: x.distance)

  # Remove not so good matches
  numGoodMatches = int(len(matches) * 0.05)
  matches = matches[:numGoodMatches]

  """## Step 4:  Find Homography """

  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
    
  # Find homography
  homography, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

  """## Step 5: Warp image"""

  # Use homography to warp image
  height, width = reference.shape
  id = cv2.warpPerspective(id, homography, (width, height))

  id = cv2.cvtColor(id, cv2.COLOR_RGB2BGR)
  reference = cv2.cvtColor(reference, cv2.COLOR_RGB2BGR)

  # Display results 
  plt.figure(figsize=[20,10]); 
  plt.subplot(121); plt.imshow(reference); plt.axis('off'); plt.title("Original Form")
  plt.subplot(122); plt.imshow(id); plt.axis('off'); plt.title("Scanned Form")

  plt.show()

referencePath = "/Users/mentxaka/TK-VisionArtificial/IdCrop/images/Template.png"
idPath = "/Users/mentxaka/TK-VisionArtificial/IdCrop/images/6.png"
idPath = "/Users/mentxaka/TK-VisionArtificial/IdCrop/images/7.png"
detectAndCrop(referencePath,idPath)