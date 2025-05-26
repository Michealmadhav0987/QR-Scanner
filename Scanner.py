import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    for barcode in decode(frame):
        data = barcode.data.decode('utf-8')
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("Detected:", data)

    cv2.imshow('QR/Barcode Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()