import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
from zipfile import ZipFile
import urllib.request

# Hyperparameters
BATCH_SIZE = 32
EPOCHS = 3
LEARNING_RATE = 0.001
DATASET_URL = 'https://github.com/spMohanty/PlantVillage-Dataset/archive/refs/heads/master.zip'
ZIP_FILE = 'plantvillage.zip'
DATA_DIR = 'PlantVillage-Dataset-master/raw/color' # The path inside the zip file
MODEL_SAVE_PATH = 'crop_disease_model.pth'

def download_and_extract():
    if not os.path.exists(ZIP_FILE) and not os.path.exists(DATA_DIR):
        print("Downloading PlantVillage dataset... (This may take a while depending on your internet speed)")
        urllib.request.urlretrieve(DATASET_URL, ZIP_FILE)
        print("Download complete.")
        
    if not os.path.exists(DATA_DIR) and os.path.exists(ZIP_FILE):
        print("Extracting dataset...")
        with ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall()
        print("Extraction complete.")

def main():
    # Setup Device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 1. Prepare Dataset
    download_and_extract()
    
    if not os.path.exists(DATA_DIR):
        print(f"Error: Could not find dataset directory at {DATA_DIR}")
        return

    print("Loading images and applying Data Augmentation...")
    # Data transformations with Augmentation to improve accuracy
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Load dataset
    full_dataset = datasets.ImageFolder(root=DATA_DIR, transform=transform)
    num_classes = len(full_dataset.classes)
    print(f"Found {len(full_dataset)} images belonging to {num_classes} classes.")
    
    # Save classes to a file so we can use them in app.py later
    with open('classes.txt', 'w') as f:
        for c in full_dataset.classes:
            f.write(c + '\n')

    # Split dataset
    train_size = int(0.8 * len(full_dataset))
    val_size = len(full_dataset) - train_size
    train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=4, pin_memory=True)

    # 2. Define Model
    print("Initializing ResNet18 model...")
    # We load the model from our model.py (reusing the same architecture)
    from model import CropDiseaseCNN
    model = CropDiseaseCNN(num_classes).to(device)

    # 3. Define Loss and Optimizer
    criterion = nn.CrossEntropyLoss()
    # Fine-tune the entire model instead of just the fully connected layer for better accuracy
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE / 10) # Lower LR for fine-tuning
    
    # Optional learning rate scheduler for better convergence
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.1)

    # 4. Training Loop
    print("Starting training...")
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            if i % 10 == 0:
                print(f"Epoch [{epoch+1}/{EPOCHS}], Step [{i}/{len(train_loader)}], Loss: {loss.item():.4f}, Accuracy: {100 * correct / total:.2f}%")

        print(f"Epoch [{epoch+1}/{EPOCHS}] completed. Average Loss: {running_loss/len(train_loader):.4f}")
        scheduler.step()

    # 5. Save the model
    print("Saving trained model...")
    torch.save(model.state_dict(), MODEL_SAVE_PATH)
    print(f"Model successfully saved to {MODEL_SAVE_PATH}")
    print("Training process finished! You can now update app.py to load this model.")

if __name__ == '__main__':
    main()
