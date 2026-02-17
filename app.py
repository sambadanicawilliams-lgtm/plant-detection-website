from flask import Flask render_template,
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
model = tf .keras.models.load_model("model/plant_models.h5")
@app.route("/",  methods=["GET","POST"])
def index():
  prediction = None
  if request . method == "POST":
    file = request.files["image"]
    img = Image .open (files) .resize ((224 , 224))
    img = np.array (img) /255.0
    img = img .reshape (1, 224, 224, 3)
    prediction = model.predict (img)
  return render _ template("index.html" , prediction = prediction)
  if__ name__== "__main__":
  app.run(debug=True)

