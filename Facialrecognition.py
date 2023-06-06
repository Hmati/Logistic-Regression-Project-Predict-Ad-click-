import cv2 

cap= cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        break

    cv2.imshow("hellen",img)

    if cv2.waitKey(1) & 0xff == ord("q"):

        cv2.destroyAllWindows()
        break 

cap.release()        

    




