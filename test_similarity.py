import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
import torchvision.models as models
from torchvision import transforms
import numpy as np
from PIL import Image

def test_similarity():
    # Load features
    features_db = np.load('plantvillage_features.npy')
    
    # Setup ResNet18 feature extractor
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    # Remove the final classification layer to get 512-dim features
    model.fc = torch.nn.Identity()
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # Create a dummy image (e.g. random noise) to see if it works
    img = Image.new('RGB', (224, 224), color = 'red')
    img_tensor = transform(img).unsqueeze(0)
    
    with torch.no_grad():
        features = model(img_tensor).numpy()
        
    # Calculate cosine similarities
    features = features / np.linalg.norm(features, axis=1, keepdims=True)
    features_db_norm = features_db / np.linalg.norm(features_db, axis=1, keepdims=True)
    
    similarities = np.dot(features_db_norm, features.T)
    max_sim = np.max(similarities)
    print("Max similarity for red image:", max_sim)

if __name__ == '__main__':
    test_similarity()
