problem faced

Path Handling Errors
Problem: SyntaxError due to backslashes
Solution: Use raw strings or forward slashes
Example: model_path = r'C:\path\to\model.h5'

Missing Dependencies
Problem: ModuleNotFoundError for PIL, TensorFlow
Solution: pip install -r requirements.txt
Requirements:
pillow
tensorflow
opencv-python

Slow Training and Overfitting
Problem: 15s/epoch on CPU, overfitting after 5 epochs
Solution: Added Dropout & Early Stopping
Code:
model.add(tf.keras.layers.Dropout(0.5))
callbacks = [tf.keras.callbacks.EarlyStopping(patience=2)]

GUI Image Display Issues
Problem: Images disappearing in Tkinter
Solution: Maintain image reference
Code:
photo = ImageTk.PhotoImage(Image.fromarray(img))
self.label.config(image=photo)
self.label.image = photo


Conclusion
I had fun in doing this project even if i encountered some challenges but it made me learn more
