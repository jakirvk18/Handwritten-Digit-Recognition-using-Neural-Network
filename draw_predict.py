import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model/digit_recognition_model.keras")

canvas_size = 400
canvas = np.zeros((canvas_size, canvas_size), dtype=np.uint8)
drawing = False
has_drawing = False

# Clear button position and size

button_x, button_y = canvas_size - 60, canvas_size - 35
button_w, button_h = 50, 25

def draw(event, x, y, flags, param):
    global drawing, has_drawing, canvas
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if click is inside Clear button
        if button_x <= x <= button_x + button_w and button_y <= y <= button_y + button_h:
            canvas[:] = 0
            has_drawing = False
            print("Canvas cleared")
        else:
            drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(canvas, (x, y), 10, (255), -1)
        has_drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

def draw_clear_button(img):
    cv2.rectangle(img, (button_x, button_y), (button_x + button_w, button_y + button_h), (255), -1)
    
    cv2.putText(img, "Clear", (button_x + 10, button_y + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0), 1, cv2.LINE_AA)

win_name = "Draw a digit"
cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, draw)

last_prediction = None

while True:
    display_canvas = canvas.copy()

    draw_clear_button(display_canvas)

    if has_drawing:
        img = cv2.resize(canvas, (28, 28))
        img = img.astype('float32') / 255.0
        img = img.reshape(1, 28, 28)

        prediction = model.predict(img, verbose=0)
        predicted_digit = np.argmax(prediction)

        if predicted_digit != last_prediction:
            print(f"Predicted Digit: {predicted_digit}")
            last_prediction = predicted_digit

    cv2.imshow(win_name, display_canvas)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
