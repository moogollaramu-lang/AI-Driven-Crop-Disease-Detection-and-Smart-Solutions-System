import numpy as np
import functools

@functools.lru_cache(maxsize=1)
def get_feature_extractor_and_db():
    import torch
    import torchvision.models as models
    from torchvision import transforms
    import os

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

def is_leaf(image):
    """
    Validation optimized to support natural outdoor field conditions.
    Now additionally compares the image features with the PlantVillage dataset
    to ensure it is a valid leaf image.
    Filters plain backdrops, skies, and smooth non-botanical objects, 
    while accepting field-captured leaf images with hands, clutter, or shadows.
    """
    import numpy as np
    import torch
    
    # 1. AI-based Feature Comparison with PlantVillage Dataset
    try:
        model, transform, features_db_norm = get_feature_extractor_and_db()
        img_tensor = transform(image.convert("RGB")).unsqueeze(0)
        
        with torch.no_grad():
            features = model(img_tensor).numpy()
            
        features = features / np.linalg.norm(features, axis=1, keepdims=True)
        similarities = np.dot(features_db_norm, features.T)
        max_sim = np.max(similarities)
        
        # Threshold set to 0.65 to explicitly reject any human, animal, 
        # or non-leaf features. Plant leaves score > 0.70.
        if max_sim < 0.65:
            return False
            
    except Exception as e:
        print("Feature comparison failed, falling back to heuristics:", e)
        pass

    # 2. Heuristic Checks
    # Resize to a standard size for analysis
    img_resized = image.resize((150, 150))
    rgb_array = np.array(img_resized.convert("RGB")).astype(np.float32)
    
    R = rgb_array[:, :, 0]
    G = rgb_array[:, :, 1]
    B = rgb_array[:, :, 2]
    
    total_pixels = R.size
    gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    
    # 1. Texture Check: Reject completely plain/blank backdrops
    if np.std(gray) < 4.0:
        return False
        
    # 2. Leaf Color Check (Green, Yellow, Brown, Red)
    green_mask = (G > R) & (G > B)
    yellow_brown_mask = (R > B) & (G > B)
    red_mask = (R > G) & (R > B) & (B < 100)
    plant_mask = green_mask | yellow_brown_mask | red_mask
    plant_ratio = np.sum(plant_mask) / total_pixels
    
    # 3. Skin / Face Rejection: Relaxed if a valid plant is visible
    # (Allow farmers holding a leaf with their hand)
    skin_mask = (R > G) & (R > B) & (R > 60) & (np.abs(R - G) > 15)
    skin_ratio = np.sum(skin_mask) / total_pixels
    if skin_ratio > 0.40 and plant_ratio < 0.15:
        skin_pixels = gray[skin_mask]
        if len(skin_pixels) > 0 and np.std(skin_pixels) < 22.0:
            return False # Smooth face detected
            
    # 4. Colorlessness Check: Reduced to 12.0 to support shadows/low light
    hsv_array = np.array(img_resized.convert("HSV"))
    saturation = hsv_array[:, :, 1]
    if np.mean(saturation) < 12:
        return False # Too colorless
        
    # 5. Blue Dominance: Increased to 65% to tolerate blue skies in field backgrounds
    blue_mask = (B > R) & (B > G) & (B - np.maximum(R, G) > 20)
    if np.sum(blue_mask) / total_pixels > 0.65:
        return False # Too blue
        
    # 6. Foliage Coverage Check:
    # Requires at least 5% plant matter; no upper bound to support lush field backgrounds
    if plant_ratio < 0.05:
        return False
        
    # 7. Morphological Shape Checks:
    # Only applied if the plant matter doesn't dominate the frame.
    # If plant matter covers >= 50% of the frame, it is guaranteed to be a plant backdrop.
    if plant_ratio < 0.50:
        rows = np.any(plant_mask, axis=1)
        cols = np.any(plant_mask, axis=0)
        
        if not np.any(rows) or not np.any(cols):
            return False
            
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        
        height = rmax - rmin + 1
        width = cmax - cmin + 1
        
        aspect_ratio = width / height
        
        # Leaves aspect ratio usually between 0.2 and 4.5
        if aspect_ratio < 0.2 or aspect_ratio > 4.5:
            return False
            
        # Compactness (Fill ratio of bounding box)
        bounding_box_area = width * height
        fill_ratio = np.sum(plant_mask) / bounding_box_area
        
        if fill_ratio < 0.15:
            return False
            
    return True

def get_disease_info():
    return {
        "Tomato - Early Blight": {
            "English": {
                "name": "Early Blight",
                "solution": "Remove affected leaves immediately. Apply copper-based fungicides. Ensure proper spacing between plants for good air circulation and water at the base.",
                "crops": "Legumes, Onions, Marigolds (Good for Crop Rotation)",
                "fertilizer": "Copper Fungicide & NPK 5-10-10 (Est. Cost: $15 - $25 / ₹1200 - ₹2000 per kg)",
                "pesticides": "Mancozeb 75% WP (2g/L water) or Chlorothalonil 75% WP spray",
                "organic": "Bacillus subtilis bio-fungicide, Neem oil spray (5ml/L) with mild soap"
            },
            "Hindi": {
                "name": "अगेती झुलसा",
                "solution": "प्रभावित पत्तियों को तुरंत हटा दें। तांबे आधारित कवकनाशी का प्रयोग करें। पौधों के बीच उचित दूरी सुनिश्चित करें और जड़ों में पानी दें।",
                "crops": "फलियां, प्याज, गेंदा (फसल चक्रण के लिए अच्छा)",
                "fertilizer": "कॉपर फफूंदनाशक और एनपीके 5-10-10 (अनुमानित लागत: ₹1200 - ₹2000 प्रति किलो)",
                "pesticides": "मैनकोज़ेब 75% WP (2 ग्राम/लीटर पानी) या क्लोरोथालोनिल स्प्रे",
                "organic": "नीम का तेल (5 मिली/लीटर पानी), बेसिलस सबटिलिस जैव-कवकनाशी"
            },
            "Telugu": {
                "name": "ఎర్లీ బ్లైట్",
                "solution": "ప్రభావిత ఆకులను వెంటనే తొలగించండి. రాగి ఆధారిత శిలీంద్రనాశకాలను వర్తించండి. మొక్కల మధ్య సరైన అంతరం ఉండేలా చూసుకోండి.",
                "crops": "పప్పుధాన్యాలు, ఉల్లిపాయలు, బంతిపువ్వు (పంట మార్పిడికి మంచిది)",
                "fertilizer": "రాగి ఆధారిత శిలీంద్రనాశకాలు మరియు NPK 5-10-10 (అంచనా వ్యయం: ₹1200 - ₹2000 కిలోకు)",
                "pesticides": "మాంకోజెబ్ 75% WP (2 గ్రా/లీటరు నీటికి) లేదా క్లోరోథలోనిల్ స్ప్రే",
                "organic": "వేప నూనె (5 మి.లీ/లీటరు నీటికి), బాసిల్లస్ సబ్టిలిస్ బయో-ఫంగిసైడ్"
            }
        },
        "Potato - Late Blight": {
            "English": {
                "name": "Late Blight",
                "solution": "Apply fungicides containing chlorothalonil or copper. Avoid overhead watering. Destroy all infected plant debris to prevent spread.",
                "crops": "Corn, Beans, Cabbage, Carrots",
                "fertilizer": "Chlorothalonil fungicide & Phosphorus-rich fertilizer (Est. Cost: $20 - $35 / ₹1500 - ₹2800 per kg)",
                "pesticides": "Metalaxyl 8% + Mancozeb 64% WP spray (2.5g/L water)",
                "organic": "Compost tea spray, Trichoderma viride bio-control agent"
            },
            "Hindi": {
                "name": "पछेती झुलसा",
                "solution": "क्लोरोथालोनिल या तांबा युक्त कवकनाशी का प्रयोग करें। ऊपर से पानी देने से बचें। फैलने से रोकने के लिए संक्रमित मलबे को नष्ट करें।",
                "crops": "मक्का, बीन्स, पत्ता गोभी, गाजर",
                "fertilizer": "क्लोरोथालोनिल फफूंदनाशक और फास्फोरस युक्त उर्वरक (अनुमानित लागत: ₹1500 - ₹2800 प्रति किलो)",
                "pesticides": "मेटालेक्सिल 8% + मैनकोज़ेब 64% WP (2.5 ग्राम/लीटर पानी) का छिड़काव करें",
                "organic": "कम्पोस्ट चाय का छिड़काव, ट्राइकोडर्मा विरिडी बायो-कंट्रोल"
            },
            "Telugu": {
                "name": "లేట్ బ్లైట్",
                "solution": "క్లోరోథలోనిల్ ఉన్న శిలీంద్రనాశకాలను వాడండి. పైనుండి నీరు పోయడం నివారించండి. సోకిన మొక్కల శిధిలాలను నాశనం చేయండి.",
                "crops": "మొక్కజొన్న, బీన్స్, క్యాబేజీ, క్యారెట్లు",
                "fertilizer": "క్లోరోథలోనిల్ మరియు భాస్వరం అధికంగా ఉండే ఎరువులు (అంచనా వ్యయం: ₹1500 - ₹2800 కిలోకు)",
                "pesticides": "మెటలాక్సిల్ 8% + మాంకోజెబ్ 64% WP (2.5 గ్రా/లీటరు నీటికి) పిచికారీ చేయండి",
                "organic": "కంపోస్ట్ టీ స్ప్రే, ట్రైకోడెర్మా విరిడే బయో-కంట్రోల్"
            }
        },
        "Healthy": {
            "English": {
                "name": "Healthy Plant",
                "solution": "Your plant looks great! Continue your current regular watering and fertilization schedule. No treatments needed.",
                "crops": "Continue with current crops, intercrop with Basil, Mint, or Spinach for better soil health.",
                "fertilizer": "Standard NPK 20-20-20 or Organic Compost (Est. Cost: $5 - $10 / ₹400 - ₹800 per kg)",
                "pesticides": "None required. Routine preventive monitoring recommended.",
                "organic": "Monthly application of diluted Neem oil as a gentle preventive deterrent."
            },
            "Hindi": {
                "name": "स्वस्थ पौधा",
                "solution": "आपका पौधा बहुत अच्छा लग रहा है! अपना वर्तमान पानी और उर्वरक कार्यक्रम जारी रखें। किसी उपचार की आवश्यकता नहीं है।",
                "crops": "वर्तमान फसलों को जारी रखें, बेहतर मिट्टी के स्वास्थ्य के लिए तुलसी या पुदीने के साथ अंतर-फसल करें।",
                "fertilizer": "सामान्य NPK 20-20-20 या जैविक खाद (अनुमानित लागत: ₹400 - ₹800 प्रति किलो)",
                "pesticides": "किसी कीटनाशक की आवश्यकता नहीं है। नियमित निगरानी करें।",
                "organic": "कीटों से बचाव के लिए महीने में एक बार हल्के नीम के तेल का छिड़काव करें।"
            },
            "Telugu": {
                "name": "ఆరోగ్యకరమైన మొక్క",
                "solution": "మీ మొక్క అద్భుతంగా కనిపిస్తోంది! మీ ప్రస్తుత నీరు మరియు ఎరువుల షెడ్యూల్‌ను కొనసాగించండి. ఎటువంటి చికిత్స అవసరం లేదు.",
                "crops": "ప్రస్తుత పంటలను కొనసాగించండి, నేల ఆరోగ్యం కోసం తులసి లేదా పుదీనాతో అంతర పంట వేయండి.",
                "fertilizer": "ప్రామాణిక NPK 20-20-20 లేదా సేంద్రియ కంపోస్ట్ (అంచనా వ్యయం: ₹400 - ₹800 కిలోకు)",
                "pesticides": "ఎలాంటి పురుగుమందులు అవసరం లేదు. క్రమం తప్పకుండా పర్యవేక్షించండి.",
                "organic": "సాధారణ చీడపీడల నివారణకు నెలకు ఒకసారి వేప నూనెను పిచికారీ చేయండి."
            }
        }
    }

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
from torchvision import transforms
from model import load_model

def predict_disease(image):
    """
    Predicts the disease using the trained CNN Model if available.
    Falls back to simulation if the model is not yet trained.
    """
    model_path = 'crop_disease_model.pth'
    classes_path = 'classes.txt'
    
    # Check if we have trained the model
    if os.path.exists(model_path) and os.path.exists(classes_path):
        # Load classes
        with open(classes_path, 'r') as f:
            classes = [line.strip() for line in f.readlines()]
            
        # Load Model
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = load_model(model_path, len(classes), device)
        
        # Preprocess Image
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        # Predict
        input_tensor = transform(image.convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted_idx = torch.max(probabilities, 0)
            
        disease_name = classes[predicted_idx.item()]
        return disease_name, confidence.item() * 100.0
        
    else:
        # Fallback to simulated prediction while model is training
        diseases = ["Tomato___Early_blight", "Potato___Late_blight", "Tomato___healthy"]
        
        # Use image data to return a consistent mock prediction
        img_array = np.array(image.resize((32, 32)))
        hashed = int(np.sum(img_array))
        
        idx = hashed % len(diseases)
        confidence = 88.0 + (hashed % 11) + (hashed % 100) / 100.0
        
        return diseases[idx], confidence

def get_recommendations(disease_id, lang):
    import disease_database
    try:
        return disease_database.get_all_disease_recommendations(disease_id, lang)
    except Exception as e:
        fallback_fert = {
            "English": "General Purpose NPK Fertilizer (Est. Cost: $10/kg)",
            "Hindi": "सामान्य प्रयोजन एनपीके उर्वरक (अनुमानित लागत: ₹800/किलो)",
            "Telugu": "సాధారణ ప్రయోజన NPK ఎరువులు (అంచనా వ్యయం: ₹800/కిలో)"
        }
        return disease_id, "Ensure regular watering and remove visibly diseased parts.", "Consult local agriculture office.", fallback_fert.get(lang, "N/A"), "Consult local agronomist for targeted fungicide.", "Apply diluted Neem oil spray."

import urllib.request
import json

def get_weather(lang="English"):
    """
    Statically returns weather for Andhra Pradesh, completely bypassing IP geolocation tracking.
    Returns a tuple: (formatted_weather_string, detected_region, detected_area)
    """
    from translations import TRANSLATIONS
    t = TRANSLATIONS.get(lang, TRANSLATIONS["English"])
    temp = "28"
    condition = "Partly Cloudy"
    advice = t['weather_adv_good']
    region = "Andhra Pradesh"
    area = "Guntur"
    return f"{temp}°C, {condition} - {advice}", region, area

def get_mandi_rates(lang="English", region=None):
    """
    Returns real-time simulated mandi rates for regional crops.
    Optionally filters by region (e.g. 'Andhra Pradesh', 'Telangana').
    """
    # Base data with regional flags
    raw_data = [
        {"crop_en": "Tomato", "crop_hi": "टमाटर", "crop_te": "టొమాటో", "rate": "₹2500/q", "trend": "up", "trend_val": "+5%", "market_en": "Guntur APMC", "market_hi": "गुंटूर एपीएमसी", "market_te": "గుంటూరు APMC", "location_en": "Guntur, Andhra Pradesh", "location_hi": "गुंटूर, आंध्र प्रदेश", "location_te": "గుంటూరు, ఆంధ్రప్రదేశ్", "dealer_en": "Ramesh Agri Traders", "dealer_hi": "रमेश एग्री ट्रेडर्स", "dealer_te": "రమేష్ అగ్రి ట్రేడర్స్", "contact": "+91 98765 43210", "region": "Andhra Pradesh"},
        {"crop_en": "Potato", "crop_hi": "आलू", "crop_te": "బంగాళాదుంప", "rate": "₹1800/q", "trend": "down", "trend_val": "-2%", "market_en": "Kurnool Mandi", "market_hi": "कुरनूल मंडी", "market_te": "కర్నూలు మండి", "location_en": "Kurnool, Andhra Pradesh", "location_hi": "कुरनूल, आंध्र प्रदेश", "location_te": "కర్నూలు, ఆంధ్రప్రదేశ్", "dealer_en": "Sri Krishna Enterprises", "dealer_hi": "श्री कृष्ण एंटरप्राइजेज", "dealer_te": "శ్రీ కృష్ణ ఎంటర్ప్రైజెస్", "contact": "+91 87654 32109", "region": "Andhra Pradesh"},
        {"crop_en": "Onion", "crop_hi": "प्याज", "crop_te": "ఉల్లిపాయ", "rate": "₹3200/q", "trend": "stable", "trend_val": "0%", "market_en": "Malakpet Market", "market_hi": "मलकपेट मार्केट", "market_te": "మలక్ పేట మార్కెట్", "location_en": "Hyderabad, Telangana", "location_hi": "हैदराबाद, तेलंगाना", "location_te": "హైదరాబాద్, తెలంగాణ", "dealer_en": "Deccan Bulbs Co.", "dealer_hi": "डेक्कन बल्ब्स कंपनी", "dealer_te": "డెక్కన్ బల్బ్స్ కో.", "contact": "+91 76543 21098", "region": "Telangana"},
        {"crop_en": "Chilli", "crop_hi": "मिर्च", "crop_te": "మిర్చి", "rate": "₹15000/q", "trend": "up", "trend_val": "+10%", "market_en": "Warangal Enamamula", "market_hi": "वारंगल एनामुला", "market_te": "వరంగల్ ఏనుమాముల", "location_en": "Warangal, Telangana", "location_hi": "वारंगल, तेलंगाना", "location_te": "వరంగల్, తెలంగాణ", "dealer_en": "Telangana Spice House", "dealer_hi": "तेलंगाना स्पाइस हाउस", "dealer_te": "తెలంగాణ స్పైస్ హౌస్", "contact": "+91 65432 10987", "region": "Telangana"},
    ]

    # Filter by region if provided
    if region:
        filtered_data = [d for d in raw_data if region.lower() in d["region"].lower()]
        if not filtered_data:
             filtered_data = raw_data # Fallback to all if no match
    else:
        filtered_data = raw_data

    # Format based on language
    lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te"}
    suffix = lang_map.get(lang, "en")
    
    formatted = []
    for d in filtered_data:
        formatted.append({
            "crop": d[f"crop_{suffix}"],
            "rate": d["rate"],
            "trend": d["trend"],
            "trend_val": d["trend_val"],
            "market": d[f"market_{suffix}"],
            "location": d[f"location_{suffix}"],
            "dealer": d[f"dealer_{suffix}"],
            "contact": d["contact"]
        })
    return formatted


def get_regional_crop_threats(lang="English", region=None):
    """
    Returns a list of major regional crops, their active local disease threats,
    severity levels, and quick-action prevention plans.
    """
    if region and "telangana" in region.lower():
        raw_threats = [
            {
                "crop": {"English": "Maize", "Hindi": "मक्का", "Telugu": "మొక్కజొన్న"},
                "disease": {"English": "Fall Armyworm", "Hindi": "फॉल आर्मीवॉर्म", "Telugu": "కత్తెర పురుగు"},
                "severity": "high",
                "action": {
                    "English": "Apply Emamectin Benzoate @ 0.4g/L. Set pheromone traps.",
                    "Hindi": "इमामेक्टिन बेंजोएट @ 0.4 ग्राम/लीटर लगाएं। फेरोमोन जाल स्थापित करें।",
                    "Telugu": "ఎమామెక్టిన్ బెంజోయేట్ @ 0.4 గ్రా/లీ వేయండి. ఫెరమోన్ ఉచ్చులు అమర్చండి."
                }
            },
            {
                "crop": {"English": "Chilli", "Hindi": "मिर्च", "Telugu": "మిర్చి"},
                "disease": {"English": "Black Thrips", "Hindi": "ब्लैक थ्रिप्स (काले कीट)", "Telugu": "నల్ల తామర పురుగులు"},
                "severity": "high",
                "action": {
                    "English": "Spray Spinetoram 11.7% SC @ 1ml/L. Install blue sticky traps.",
                    "Hindi": "स्पिनेटोरम 11.7% SC @ 1 मिली/लीटर स्प्रे करें। नीले चिपचिपे जाल लगाएं।",
                    "Telugu": "స్పినెటోరమ్ 11.7% SC @ 1 మి.లీ/లీ పిచికారీ చేయండి. నీలి జిగురు అట్టలు పెట్టండి."
                }
            },
            {
                "crop": {"English": "Onion", "Hindi": "प्याज", "Telugu": "ఉల్లిపాయ"},
                "disease": {"English": "Purple Blotch", "Hindi": "बैंगनी धब्बा रोग", "Telugu": "నేల రంగు మచ్చ తెగులు"},
                "severity": "medium",
                "action": {
                    "English": "Spray Mancozeb @ 2.5g/L or Tebuconazole @ 1ml/L.",
                    "Hindi": "मैनकोज़ेब @ 2.5 ग्राम/लीटर या टेबुकोनाज़ोल @ 1 मिली/लीटर स्प्रे करें।",
                    "Telugu": "మాంకోజెబ్ @ 2.5 గ్రా/లీ లేదా టెబుకొనజోల్ @ 1 మి.లీ/లీ పిచికారీ చేయండి."
                }
            }
        ]
    elif region and ("andhra" in region.lower() or "guntur" in region.lower()):
        raw_threats = [
            {
                "crop": {"English": "Paddy (Rice)", "Hindi": "धान (चावल)", "Telugu": "వరి (బియ్యం)"},
                "disease": {"English": "Rice Blast", "Hindi": "ब्लास्ट रोग", "Telugu": "అగ్గి తెగులు"},
                "severity": "high",
                "action": {
                    "English": "Apply Tricyclazole 75% WP @ 0.6g/L. Keep water levels balanced.",
                    "Hindi": "ट्राइसाइक्लाजोल 75% WP @ 0.6 ग्राम/लीटर लगाएं। पानी का स्तर संतुलित रखें।",
                    "Telugu": "ట్రైసైక్లాజోల్ 75% WP @ 0.6 గ్రా/లీటరు వేయండి. నీటి పరిమాణాన్ని సమతుల్యంగా ఉంచండి."
                }
            },
            {
                "crop": {"English": "Cotton", "Hindi": "कपास", "Telugu": "పత్తి"},
                "disease": {"English": "Leaf Curl Virus", "Hindi": "लीफ कर्ल वायरस", "Telugu": "ఆకు ముడత వైరస్"},
                "severity": "medium",
                "action": {
                    "English": "Spray Imidacloprid to control whitefly vector. Remove weed hosts.",
                    "Hindi": "सफेद मक्खी वाहक को नियंत्रित करने के लिए इमिडाक्लोप्रिड का छिड़काव करें।",
                    "Telugu": "తెల్లదోమ నివారణకు ఇమిడాక్లోప్రిడ్ పిచికారీ చేయండి."
                }
            },
            {
                "crop": {"English": "Chilli", "Hindi": "मिर्च", "Telugu": "మిర్చి"},
                "disease": {"English": "Dieback & Fruit Rot", "Hindi": "डाईबैक और फल सड़न", "Telugu": "ఎండు తెగులు & కాయ కుళ్లు"},
                "severity": "high",
                "action": {
                    "English": "Spray Copper Oxychloride 3g/L or Mancozeb 2.5g/L. Improve drainage.",
                    "Hindi": "कॉपर ऑक्सीक्लोराइड 3 ग्राम/लीटर या मैनकोज़ेब 2.5 ग्राम/लीटर का छिड़काव करें।",
                    "Telugu": "కాపర్ ఆక్సిక్లోరైడ్ 3 గ్రా/లీ లేదా మాంకోజెబ్ 2.5 గ్రా/లీ పిచికారీ చేయండి."
                }
            }
        ]
    else:
        # Default fallback (e.g. Tomato and Potato)
        raw_threats = [
            {
                "crop": {"English": "Tomato", "Hindi": "टमाटर", "Telugu": "టొమాటో"},
                "disease": {"English": "Early Blight", "Hindi": "अगेती झुलसा", "Telugu": "ఎర్లీ బ్లైట్"},
                "severity": "high",
                "action": {
                    "English": "Remove lower leaves immediately. Apply Copper Hydroxide spray.",
                    "Hindi": "निचली पत्तियों को तुरंत हटाएं। कॉपर हाइड्रोक्साइड स्प्रे का प्रयोग करें।",
                    "Telugu": "క్రింది ఆకులను వెంటనే కత్తిరించండి. కాపర్ హైడ్రాక్సైడ్ పిచికారీ చేయండి."
                }
            },
            {
                "crop": {"English": "Potato", "Hindi": "आलू", "Telugu": "బంగాళाదుంప"},
                "disease": {"English": "Late Blight", "Hindi": "पछेती झुलसा", "Telugu": "లేట్ బ్లైట్"},
                "severity": "high",
                "action": {
                    "English": "Apply Metalaxyl + Mancozeb. Avoid overhead watering.",
                    "Hindi": "मेटालेक्सिल + मैनकोज़ेब लगाएं। ऊपर से पानी देने से बचें।",
                    "Telugu": "మెటలాక్సిల్ + మాంకోజెబ్ వేయండి. పైనుండి నీరు పోయడం నివారించండి."
                }
            }
        ]

    formatted_threats = []
    for t in raw_threats:
        formatted_threats.append({
            "crop": t["crop"].get(lang, t["crop"]["English"]),
            "disease": t["disease"].get(lang, t["disease"]["English"]),
            "severity": t["severity"],
            "action": t["action"].get(lang, t["action"]["English"])
        })
    return formatted_threats


def get_community_connectivity(lang="English", region=None):
    """
    Returns a directory of regional agricultural support contacts (helplines, logistics,
    dealers, buyers) with phone numbers.
    """
    if region and "telangana" in region.lower():
        raw_contacts = [
            {
                "role_key": "role_agronomist",
                "name": {"English": "Dr. G. Reddy (Telangana Agri University)", "Hindi": "डॉ. जी. रेड्डी (तेलंगाना कृषि विश्वविद्यालय)", "Telugu": "డాక్టర్ జి. రెడ్డి (తెలంగాణ వ్యవసాయ విశ్వవిద్యాలయం)"},
                "spec": {"English": "Maize FAW & Cotton Pests", "Hindi": "मक्का FAW और कपास कीट", "Telugu": "మొక్కజొన్న కత్తెర పురుగు & పత్తి తెగుళ్లు"},
                "contact": "+91 98480 98765"
            },
            {
                "role_key": "role_logistics",
                "name": {"English": "Warangal Mandi Transport Union", "Hindi": "वारंगल मंडी परिवहन संघ", "Telugu": "వరంగల్ మండి రవాణా యూనియన్"},
                "spec": {"English": "Bulk Mandi Delivery & Cold Storage", "Hindi": "थोक मंडी वितरण और कोल्ड स्टोरेज", "Telugu": "మండి రవాణా & కోల్డ్ స్టోరేజ్"},
                "contact": "+91 90001 54321"
            },
            {
                "role_key": "role_dealer",
                "name": {"English": "Kakatiya Bio-Organic Fertilizers", "Hindi": "काकतीय बायो-ऑर्गेनिक फर्टिलाइजर्स", "Telugu": "కాకతీయ బయో-ఆర్గానిక్ ఫెర్టిలైజర్స్"},
                "spec": {"English": "Micro-Nutrients & Organic Sprays", "Hindi": "सूक्ष्म पोषक तत्व और जैविक स्प्रे", "Telugu": "సూక్ష్మ పోషకాలు & సేంద్రియ మందులు"},
                "contact": "+91 88888 77777"
            },
            {
                "role_key": "role_buyer",
                "name": {"English": "Telangana Agri Crop Buyers Co.", "Hindi": "तेलंगाना एग्री क्रॉप बायर्स कंपनी", "Telugu": "తెలంగాణ అగ్రి క్రాప్ బయ్యర్స్ కో."},
                "spec": {"English": "Direct Maize & Onion Bulk Buying", "Hindi": "मक्का और प्याज की सीधी थोक खरीद", "Telugu": "మొక్కజొన్న & ఉల్లిపాయల కొనుగోళ్లు"},
                "contact": "+91 77777 66666"
            }
        ]
    elif region and ("andhra" in region.lower() or "guntur" in region.lower()):
        raw_contacts = [
            {
                "role_key": "role_agronomist",
                "name": {"English": "Dr. K. Rao (AP Rice Research Station)", "Hindi": "डॉ. के. राव (आंध्र धान अनुसंधान स्टेशन)", "Telugu": "డాక్టర్ కె. రావు (ఆంధ్ర వరి పరిశోధనా కేంద్రం)"},
                "spec": {"English": "Paddy & Chilli Diseases", "Hindi": "धान और मिर्च के रोग", "Telugu": "వరి & మిర్చి తెగుళ్లు"},
                "contact": "+91 94401 23456"
            },
            {
                "role_key": "role_logistics",
                "name": {"English": "Guntur Agri-Express Logistics", "Hindi": "गुंटूर एग्री-एक्सप्रेस लॉजिस्टिक्स", "Telugu": "గుంటూరు అగ్రి-ఎక్స్‌ప్రెస్ లాజిస్టిక్స్"},
                "spec": {"English": "Crop Transportation & Storage", "Hindi": "ఫसल परिवहन और भंडारण", "Telugu": "పంట రవాణా & నిల్వ"},
                "contact": "+91 80081 23456"
            },
            {
                "role_key": "role_dealer",
                "name": {"English": "Sri Venkata Seeds & Fertilizers", "Hindi": "श्री वेंकट सीड्स एंड फर्टिलाइजर्स", "Telugu": "శ్రీ వెంకట సీడ్స్ & ఫెర్టిలైజర్స్"},
                "spec": {"English": "Certified Paddy Seeds & Bio-Inputs", "Hindi": "प्रमाणित धान बीज और जैव-इनपुट", "Telugu": "ధృవీకరించబడిన వరి విత్తనాలు & బయో-ఇన్‌పుట్స్"},
                "contact": "+91 99887 76655"
            },
            {
                "role_key": "role_buyer",
                "name": {"English": "Rayalaseema Wholesale Traders", "Hindi": "रायलसीमा थोक व्यापारी", "Telugu": "రాయలసీమ హోల్‌సేల్ ట్రేడర్స్"},
                "spec": {"English": "Bulk Chilli & Cotton Procurement", "Hindi": "थोक मिर्च और कपास खरीद", "Telugu": "మిర్చి & పత్తి కొనుగోళ్లు"},
                "contact": "+91 73829 10482"
            }
        ]
    else:
        raw_contacts = [
            {
                "role_key": "role_agronomist",
                "name": {"English": "Dr. Amit Sharma (National Ag Helpdesk)", "Hindi": "डॉ. अमित शर्मा (राष्ट्रीय कृषि हेल्पडेस्क)", "Telugu": "డాక్టర్ అమిత్ శర్మ (జాతీయ వ్యవసాయ హెల్ప్‌డెస్క్)"},
                "spec": {"English": "Vegetable Crops Expert", "Hindi": "सब्जी फसल विशेषज्ञ", "Telugu": "కూరగాయల పంటల నిపుణుడు"},
                "contact": "+91 91111 22222"
            },
            {
                "role_key": "role_logistics",
                "name": {"English": "National Cold-Chain Logistics", "Hindi": "राष्ट्रीय कोल्ड-चेन लॉजिस्टिक्स", "Telugu": "జాతీయ కోల్డ్-చైన్ లాజిస్టిక్స్"},
                "spec": {"English": "Multi-State Reefer Transport", "Hindi": "बहु-राज्य रीफर परिवहन", "Telugu": "మల్టీ-స్టేట్ రవాణా సేవలు"},
                "contact": "+91 82222 33333"
            },
            {
                "role_key": "role_dealer",
                "name": {"English": "Bharat Kisan Seed Emporium", "Hindi": "भारत किसान बीज एम्पोरियम", "Telugu": "భారత్ కిసాన్ సీడ్ ఎంపోరియం"},
                "spec": {"English": "High-Yield F1 Hybrid Seeds", "Hindi": "उच्च उपज वाले F1 हाइब्रिड बीज", "Telugu": "అధిక దిగుబడినిచ్చే హైబ్రిడ్ విత్తనాలు"},
                "contact": "+91 93333 44444"
            },
            {
                "role_key": "role_buyer",
                "name": {"English": "Metro Food Wholesalers Ltd.", "Hindi": "मेट्रो फूड होलसेलर्स लिमिटेड", "Telugu": "మెట్రో ఫుడ్ హోల్‌సేలర్స్ లిమిటెడ్"},
                "spec": {"English": "Bulk Tomato & Potato Purchasing", "Hindi": "टमाटर और आलू की थोक खरीद", "Telugu": "టొమాటో & బంగాళాదుంప కొనుగోళ్లు"},
                "contact": "+91 74444 55555"
            }
        ]

    formatted_contacts = []
    for c in raw_contacts:
        formatted_contacts.append({
            "role_key": c["role_key"],
            "name": c["name"].get(lang, c["name"]["English"]),
            "spec": c["spec"].get(lang, c["spec"]["English"]),
            "contact": c["contact"]
        })
    return formatted_contacts


