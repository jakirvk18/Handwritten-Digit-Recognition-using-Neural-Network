### Handwritten Digit Recognition using Neural Network 🧠✍️

This project is a real-time handwritten digit recognition system built with a Convolutional Neural Network (CNN) and OpenCV. It allows users to draw digits on a virtual canvas and get live predictions from a trained model based on the MNIST dataset.

## 🔍 Features

- 🖌️ Interactive drawing canvas using OpenCV
- 🔢 Real-time digit prediction as you draw
- 🧼 Clickable **Clear** button to reset the canvas
- 🧠 Trained CNN model with over **97% accuracy**
- 🖥️ Clean UI with predictions shown in the terminal only

---

## 📁 Folder Structure

```bash
Handwritten-Digit-Recognition/
│
├── model/
│ └── digit_recognition_model.keras # Trained model file
│
├── train_model.py # Script to train and save the CNN model
├── draw_predict.py # Main application for drawing and predicting
|__requirements.py
├── README.md # Project description and instructions
```
## 🛠️ Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/Handwritten-Digit-Recognition.git
cd Handwritten-Digit-Recognition
pip install -r requirements.txt

```
---

### ✅ And include the `requirements.txt` file like this:

```txt
# requirements.txt

tensorflow
opencv-python
numpy
```
## 🧠 Model Training
You can train the CNN model using train_model.py:
```bash
python train_model.py
```
This will:

  . Load the MNIST dataset

  . Train a CNN for 5 epochs

  . Save the model in model/digit_recognition_model.keras
## 🚀 Run the Application
Once the model is trained, run the digit recognition app:
```bash
python draw_predict.py
```
Controls:
- Draw using left mouse button

- Prediction is printed in terminal automatically while drawing

- Click "Clear" button to erase canvas

- Press ESC to exit the application
---
## 🖼️ Sample Demo
✅ Live digit prediction while drawing
✅ Easy-to-use interface built with OpenCV
✅ Model trained on the MNIST dataset

![Screenshot 2025-06-06 194450](https://github.com/user-attachments/assets/1732d263-8dcb-496e-95e5-e4c8d3788575)

---
## 📚 Skills Demonstrated
- Deep Learning with CNNs

- Image preprocessing

- OpenCV GUI handling

- Real-time inference

- Python scripting and modular design

---
## 🤝 Acknowledgements
- MNIST dataset

- TensorFlow and Keras team
---
## 📌 Future Improvements
- Add support for touchscreen/stylus input

- Display prediction confidence

- Export drawn digit as an image
---
## Author
Jakir Hussain
