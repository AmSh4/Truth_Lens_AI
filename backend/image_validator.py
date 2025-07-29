from torchvision import transforms
from PIL import Image
import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3), nn.ReLU(), nn.MaxPool2d(2)
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 6 * 6, 2)
        )

    def forward(self, x):
        return self.fc(self.conv(x))

model = SimpleCNN()
model.load_state_dict(torch.load("models/cnn_image_classifier.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor()
])

def validate_image(img: Image.Image):
    input_tensor = transform(img).unsqueeze(0)
    output = model(input_tensor)
    pred = torch.argmax(output).item()
    return "Genuine Image" if pred == 1 else "Fake Image"
