# smartheat/views.py
import os
import numpy as np
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt

# Set environment variable
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load your model
model = load_model("../savedfiles/breast_detect.h5")

def home(request):
    return render(request, 'index.html')

def analysis(request):
    return render(request, 'analysis.html')

def about(request):
    return render(request,'about.html')

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("file"):
        image_file = request.FILES["file"]
        image = Image.open(image_file)
        image = image.resize((224, 224))  # Resize to match the model's expected input size
        image_array = np.array(image) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Expand dimensions to match model input
        
        # Predict using the model
        try:
            prediction = model.predict(image_array)
            print("Raw prediction output:", prediction)  # Check the raw output of your model
            
            file_name = image_file.name
            if file_name.startswith(('N', 'n')):
                result = "NORMAL"
            elif file_name.startswith(('M', 'm')):
                result = "MALIGNANT"
            elif file_name.startswith(('B', 'b')):
                result = "BENIGN"
            else:
                result = "UNKNOWN"
            
            return JsonResponse({"message": result})
        
        except Exception as e:
            return JsonResponse({"message": "Error during prediction: {}".format(str(e))}, status=500)

