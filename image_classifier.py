import torch
import torch.nn as nn

from torchvision import models
from torchvision import transforms
from PIL import Image


# Load class names
classes = torch.load("models/class_names.pth")

# Load model
model = models.mobilenet_v2()

model.classifier[1] = nn.Linear(
    model.last_channel,
    len(classes)
)

model.load_state_dict(
    torch.load(
        "models/disease_model.pth",
        map_location="cpu"
    )
)

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


def predict_disease(image_path):

    image = Image.open(image_path).convert("RGB")
    image = transform(image)
    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(output, dim=1)

        confidence, prediction = torch.max(probabilities, dim=1)

    pred = classes[prediction.item()]

    mapping = {
        "Tomato___Early_blight": "Tomato - Early Blight",
        "Tomato___Late_blight": "Tomato - Late Blight",
        "Potato___Early_blight": "Potato - Early Blight",
        "Potato___Late_blight": "Potato - Late Blight",
        "Bacterial leaf blight": "Rice - Bacterial Leaf Blight",
        "Brown spot": "Rice - Brown Spot",
        "Leaf smut": "Rice - Leaf Smut"
    }

    disease_name = mapping.get(pred, pred)

    confidence = confidence.item() * 100

    return disease_name, confidence