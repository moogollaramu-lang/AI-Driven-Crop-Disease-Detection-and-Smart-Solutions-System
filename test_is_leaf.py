import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
import torchvision.models as models
from torchvision import transforms
import numpy as np
from PIL import Image

def get_feature_extractor_and_db():
    features_db = np.load('plantvillage_features.npy')
    features_db_norm = features_db / np.linalg.norm(features_db, axis=1, keepdims=True)
    
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    model.fc = torch.nn.Identity()
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    return model, transform, features_db_norm

def test_random_images():
    model, transform, features_db_norm = get_feature_extractor_and_db()
    
    # test pure noise
    noise = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
    noise_img = Image.fromarray(noise)
    
    # test pure white
    white_img = Image.new('RGB', (224, 224), 'white')
    
    # test a fake "leaf" (just green)
    green_img = Image.new('RGB', (224, 224), 'green')
    
    for name, img in [('Noise', noise_img), ('White', white_img), ('Green', green_img)]:
        img_tensor = transform(img.convert("RGB")).unsqueeze(0)
        with torch.no_grad():
            features = model(img_tensor).numpy()
        features = features / np.linalg.norm(features, axis=1, keepdims=True)
        similarities = np.dot(features_db_norm, features.T)
        print(f"Max similarity for {name}: {np.max(similarities)}")

if __name__ == '__main__':
    test_random_images()
