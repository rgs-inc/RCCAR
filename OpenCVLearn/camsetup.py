import cv2
import datetime

cap = cv2.VideoCapture(0)   # Default camera usually 0, or -1

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(3, 3000)     # Set width
cap.set(4, 3000)     # Set height

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width; ' + str(cap.get(3)) + ' ' + "Height: " + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        frame = cv2.putText(frame, datet, (0, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()