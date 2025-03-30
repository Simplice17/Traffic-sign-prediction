import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf

class TrafficSignClassifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Sign Classifier")
        self.root.geometry("800x600")
        
        # Load model (change path to your model)
        self.model = tf.keras.models.load_model('C:\\Users\\Tikela Daouda\\Desktop\\Traffic\\Simplice\\traffic_model.h5')
        self.class_names = [str(i) for i in range(43)]  # Replace with actual names

        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Image display
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)
        
        # Upload button
        upload_btn = tk.Button(
            self.root,
            text="Select Image",
            command=self.load_image,
            font=('Arial', 14),
            bg='#4CAF50',
            fg='white'
        )
        upload_btn.pack(pady=10)
        
        # Prediction label
        self.prediction_label = tk.Label(
            self.root,
            text="Prediction will appear here",
            font=('Arial', 16)
        )
        self.prediction_label.pack(pady=20)
        
        # Confidence label
        self.confidence_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 14)
        )
        self.confidence_label.pack()
    
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        
        if file_path:
            try:
                # Process image
                img = cv2.imread(file_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, (300, 300))  # Display size
                
                # Show image
                photo = ImageTk.PhotoImage(image=Image.fromarray(img))
                self.image_label.config(image=photo)
                self.image_label.image = photo
                
                # Get prediction
                self.predict(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not process image: {e}")
    
    def predict(self, image_path):
        # Preprocess (match your training)
        img = cv2.imread(image_path)
        img = cv2.resize(img, (30, 30))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Predict
        predictions = self.model.predict(img)
        predicted_class = np.argmax(predictions)
        confidence = np.max(predictions) * 100
        
        # Update UI
        self.prediction_label.config(
            text=f"Prediction: {self.class_names[predicted_class]}"
        )
        self.confidence_label.config(
            text=f"Confidence: {confidence:.2f}%",
            fg='green' if confidence > 80 else 'orange'
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSignClassifier(root)
    root.mainloop()