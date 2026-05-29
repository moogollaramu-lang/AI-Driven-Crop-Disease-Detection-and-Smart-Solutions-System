import torch
import torch.nn as nn
import torchvision.models as models

class CropDiseaseCNN(nn.Module):
    """
    Convolutional Neural Network (CNN) architecture for Crop Disease Detection.
    Uses Transfer Learning with a pre-trained ResNet18 model.
    """
    def __init__(self, num_classes):
        super(CropDiseaseCNN, self).__init__()
        # Load a pre-trained ResNet18 as the base CNN feature extractor
        self.base_model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        
        # Get the number of features in the last fully connected layer
        num_ftrs = self.base_model.fc.in_features
        
        # Replace the final layer for our specific number of crop disease classes
        self.base_model.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(num_ftrs, num_classes)
        )

    def forward(self, x):
        return self.base_model(x)

def load_model(model_path, num_classes, device='cpu'):
    """
    Function to load the trained CNN model.
    """
    model = CropDiseaseCNN(num_classes)
    # Uncomment the line below when you have a trained model weights file (.pth)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model

def preprocess_image(image):
    """
    Prepares the image to be fed into the CNN model.
    """
    from torchvision import transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)
