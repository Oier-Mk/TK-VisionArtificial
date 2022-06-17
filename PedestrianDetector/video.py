# importing libraries
import cv2
import traceback
from counter import getNDetections

def detectionInVideo(path, modeloYolo):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(path)

    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")

    # Read until video is completed
    while(cap.isOpened()):
            
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            
            actualFrame = modeloYolo(frame)

            for index, i in enumerate(actualFrame.xyxy[0]):
                tensor = actualFrame.xyxy[0][index]
                p1 = (int(tensor[0]),int(tensor[1]))
                p2 = (int(tensor[2]),int(tensor[3]))
                print(p1, p2)
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

            # Display the resulting frame
            cv2.imshow('Frame', frame)
            print("fame")
            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break
    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

def detectVideo(path, model):
    #https://docs.ultralytics.com/tutorials/pytorch-hub/
    print("Conteo comenzado")

    try:

        video = cv2.VideoCapture(path)
        
        detections = 0
        lastDetections = 0

        while True:
            ok, frame = video.read()
            if not ok:
                break 

            actualFrame = model(frame)
            actualDetections = getNDetections(actualFrame)
            print(actualDetections)
            if lastDetections < actualDetections:
                detections += abs(actualDetections - lastDetections)
                print("incremento " + str(abs(actualDetections - lastDetections)) + ", total " + str(detections))
            
            lastDetections = actualDetections
        
        print(detections)
        
    except Exception:
        #print(f"La imagen {path.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
        print(traceback.format_exc())

    print("Conteo completado")

