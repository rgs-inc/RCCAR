import cv2

cap = cv2.VideoCapture(0)   # Default camera usually 0, or -1

# To save video:

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (1280,720))

# Capture video can also be used with 'home.avi' or existing video

# To capture continuous frame:

while cap.isOpened():           #While video frame is open
    ret, frame = cap.read()

    if ret:
        out.write(frame)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # TO convert color
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Grey Frame', gray)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()