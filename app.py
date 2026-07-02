import streamlit as st
import numpy as np
from PIL import Image
from translations import TRANSLATIONS
from utils import is_leaf, predict_disease, get_recommendations, get_weather
import disease_database
import time
import base64
import os
import textwrap

# Set Streamlit Page Configuration
st.set_page_config(page_title="AI Driven Crop Disease Detection and Smart Solutions System", page_icon="🌱", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit Branding
st.markdown("""
<style>
#MainMenu {{ visibility: hidden !important; }}
[data-testid="stMainMenu"] {{ display: none !important; }}
footer {{ visibility: hidden !important; }}
[data-testid="stToolbar"] {{ display: none !important; }}
.stDeployButton {{ display: none !important; }}
[data-testid="stHeader"] {{ display: none !important; }}
header {{ display: none !important; }}
.stAppHeader {{ display: none !important; }}
div[class*="stAppHeader"] {{ display: none !important; }}
[data-testid="stSidebar"] {{ display: none !important; }}
[data-testid="collapsedControl"] {{ display: none !important; }}

/* Hide Streamlit Community Cloud Manage App Badge & red watermark */
.viewerBadge {{ display: none !important; }}
.stViewerBadge {{ display: none !important; }}
#viewer-badge {{ display: none !important; }}
[data-testid="viewerBadge"] {{ display: none !important; }}
[data-testid="stViewerBadge"] {{ display: none !important; }}
a[href*="streamlit.io"] {{ display: none !important; }}
a[href*="streamlit.app"] {{ display: none !important; }}
div[class*="viewerBadge"] {{ display: none !important; }}
div[class*="stViewerBadge"] {{ display: none !important; }}
a[class*="viewerBadge"] {{ display: none !important; }}
a[class*="stViewerBadge"] {{ display: none !important; }}
iframe[title="Manage app"] {{ display: none !important; }}
iframe[src*="viewerBadge"] {{ display: none !important; }}

/* Hide Streamlit logos, icons, top decorations and loading widgets */
img[src*="streamlit"] {{ display: none !important; }}
svg[class*="streamlit"] {{ display: none !important; }}
.stLogo {{ display: none !important; }}
[data-testid="stLogo"] {{ display: none !important; }}
div[data-testid="stDecoration"] {{ display: none !important; }}
div[data-testid="stStatusWidget"] {{ display: none !important; }}

/* Premium Styled Specimen Image Preview */
[data-testid="stImage"] img {{
    max-width: 240px !important;
    max-height: 240px !important;
    object-fit: cover !important;
    border-radius: 16px !important;
    border: 2px solid #3c5a45 !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08) !important;
    margin: 12px auto !important;
    display: block !important;
    transition: transform 0.3s ease !important;
}}
[data-testid="stImage"] img:hover {{
    transform: scale(1.02);
}}
[data-testid="stImage"] {{
    text-align: center !important;
}}
</style>
""", unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def get_image_base64(image):
    import io
    buffered = io.BytesIO()
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def get_background_url():
    for ext in ["jpg", "jpeg", "png"]:
        bg_path = f"background.{ext}"
        if os.path.exists(bg_path):
            bg_base64 = get_base64_of_bin_file(bg_path)
            mime_ext = "jpeg" if ext in ["jpg", "jpeg"] else "png"
            return f"data:image/{mime_ext};base64,{bg_base64}"
    return "https://images.unsplash.com/photo-1592982537447-6f2a6a0a3023?q=80&w=2000&auto=format&fit=crop"

bg_url = get_background_url()

# Custom CSS for Botanica UI
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

    [data-testid="stAppViewContainer"] {{
        background-image: url('{bg_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    [data-testid="stHeader"] {{ display: none !important; }}
    header {{ display: none !important; }}
    [data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}
    
    body, .stApp, p, span, div {{ font-family: 'Inter', sans-serif; color: #4a4a4a; }}
    h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', serif; color: #2c3e2e; }}
    
    .botanica-logo-area {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }}
    .botanica-logo-icon {{
        background: white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        border: 1px solid #e0e0e0;
    }}
    .botanica-title {{
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        letter-spacing: 0.2rem;
        color: #2c3e2e;
        margin: 0;
        text-transform: uppercase;
        font-weight: 600;
    }}
    
    /* Botanica Cards */
    .b-card {{
        background: rgba(244, 241, 235, 0.95);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.8);
    }}
    
    /* Main Right Card */
    .b-main-card {{
        background: rgba(244, 241, 235, 0.95);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        min-height: 600px;
        border: 1px solid rgba(255,255,255,0.8);
    }}
    
    /* Pills */
    .pill-red {{ background: #fff0f0; color: #d32f2f; border: 1px solid #ffcccc; padding: 4px 12px; border-radius: 20px; font-size: 0.70rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem; display: inline-block; }}
    .pill-green {{ background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; padding: 4px 12px; border-radius: 20px; font-size: 0.70rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem; display: inline-block; }}
    .pill-dark {{ background: #3c5a45; color: #ffffff; padding: 4px 12px; border-radius: 20px; font-size: 0.70rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem; display: inline-block; margin-right: 10px; }}
    .pill-light {{ background: #e8ede9; color: #3c5a45; border: 1px solid #d1ded3; padding: 4px 12px; border-radius: 20px; font-size: 0.70rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem; display: inline-block; }}
    
    /* Result title */
    .result-title {{ font-family: 'Playfair Display', serif; font-size: 2.6rem; color: #2c3e2e; line-height: 1.2; margin-top: 15px; margin-bottom: 25px; }}
    
    /* Weather / Mini cards */
    .mini-card {{ background: rgba(244, 241, 235, 0.95); border-radius: 20px; padding: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.8); }}
    .mini-card h4 {{ font-family: 'Inter', sans-serif; font-size: 0.65rem; color: #888; text-transform: uppercase; margin-bottom: 5px; letter-spacing: 0.1rem; font-weight: 700; }}
    .mini-card p {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #2c3e2e; margin: 0; }}
    
    /* Solution block */
    .solution-block {{ background: #eef2ed; border-radius: 12px; padding: 25px; border: 1px solid #d1ded3; margin-top: 20px; margin-bottom: 20px; }}
    .solution-block h4 {{ font-family: 'Inter', sans-serif; font-size: 0.7rem; color: #3c5a45; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.05rem; font-weight: 700; }}
    .solution-block p {{ color: #4a4a4a; font-size: 0.95rem; line-height: 1.6; margin: 0; }}
    
    /* Preventive measures block */
    .preventive-block {{ background: #ffffff; border-radius: 12px; padding: 25px; border: 1px solid #e0e0e0; margin-bottom: 20px; }}
    .preventive-block h4 {{ font-family: 'Inter', sans-serif; font-size: 0.7rem; color: #888; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 0.05rem; font-weight: 700; }}
    .preventive-block li {{ color: #4a4a4a; font-size: 0.95rem; line-height: 1.8; margin-bottom: 8px; }}
    
    /* Primary Button */
    button[kind="primary"] {{
        background: #3c5a45 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 12px 24px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(60, 90, 69, 0.3) !important;
    }}
    button[kind="primary"] * {{
        color: white !important;
    }}
    button[kind="primary"]:hover {{
        background: #2c4233 !important;
        transform: translateY(-2px);
    }}
    
    /* Secondary Pill Button */
    button[kind="secondary"] {{
        background: #e8ede9 !important;
        color: #3c5a45 !important;
        border-radius: 20px !important;
        padding: 4px 14px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        border: 1px solid #d1ded3 !important;
        width: auto !important;
        float: right !important;
        transition: all 0.3s ease !important;
    }}
    button[kind="secondary"]:hover {{
        background: #d1ded3 !important;
    }}
    
    /* File uploader custom style */
    [data-testid="stFileUploader"] {{
        background: white;
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #e0e0e0;
    }}
    
    /* Hide specific streamlit elements */
    #MainMenu {{ visibility: hidden !important; }}
    [data-testid="stMainMenu"] {{ display: none !important; }}
    footer {{ visibility: hidden !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    .stDeployButton {{ display: none !important; }}
    
    /* Hide Streamlit Community Cloud Manage App Badge and Hosted with Streamlit Badge in bottom right */
    .viewerBadge {{ display: none !important; }}
    .stViewerBadge {{ display: none !important; }}
    #viewer-badge {{ display: none !important; }}
    [data-testid="viewerBadge"] {{ display: none !important; }}
    [data-testid="stViewerBadge"] {{ display: none !important; }}
    a[href*="streamlit.io"] {{ display: none !important; }}
    a[href*="streamlit.app"] {{ display: none !important; }}
    div[class*="viewerBadge"] {{ display: none !important; }}
    div[class*="stViewerBadge"] {{ display: none !important; }}
    a[class*="viewerBadge"] {{ display: none !important; }}
    a[class*="stViewerBadge"] {{ display: none !important; }}
    iframe[title="Manage app"] {{ display: none !important; }}
    iframe[src*="viewerBadge"] {{ display: none !important; }}
    
    /* Hide Streamlit logos, icons, top decorations and loading widgets */
    img[src*="streamlit"] {{ display: none !important; }}
    svg[class*="streamlit"] {{ display: none !important; }}
    .stLogo {{ display: none !important; }}
    [data-testid="stLogo"] {{ display: none !important; }}
    div[data-testid="stDecoration"] {{ display: none !important; }}
    div[data-testid="stStatusWidget"] {{ display: none !important; }}
    
    /* Responsive max width */
    .block-container {{ max-width: 1200px; padding-top: 2rem !important; padding-bottom: 4rem !important; }}
    
    /* Action Buttons row at bottom */
    .action-btn {{
        background: white; 
        border: 1px solid #d1ded3; 
        padding: 8px 16px; 
        border-radius: 20px; 
        color: #3c5a45; 
        font-weight: 600; 
        font-size: 0.75rem; 
        display: inline-block;
        margin-right: 10px;
    }}
    
    /* Style Streamlit native bordered containers to be solid white cards */
    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"] > div,
    div[data-testid="stVerticalBlockBorderWrapper"] > div > div,
    div[data-testid="stVerticalBlock"] > div[style*="border"],
    div[data-testid="stVerticalBlock"] > div[style*="border"] > div,
    div[data-testid="stVerticalBlock"] > div[style*="border"] > div > div {{
        background-color: #ffffff !important;
        background: #ffffff !important;
        border-radius: 20px !important;
        padding: 25px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
        border: 1px solid rgba(255,255,255,0.8) !important;
    }}
</style>
""", unsafe_allow_html=True)

# Fetch Weather Info (Dynamically based on language)
if 'loc_detected' not in st.session_state:
    st.session_state.loc_detected = True

lang = st.session_state.get('lang', 'English')
if 'weather_lang' not in st.session_state or st.session_state.weather_lang != lang:
    st.session_state.weather, st.session_state.detected_region, st.session_state.detected_area = get_weather(lang)
    st.session_state.weather_lang = lang

weather_str = st.session_state.weather
temp_str = "--°C"
cond_str = "Unknown"
if "°C" in weather_str:
    temp_str = weather_str.split("°C")[0] + "°C"
    try:
        cond_str = weather_str.split("°C, ")[1].split(" - ")[0]
    except:
        pass

# Initialize History
if 'history' not in st.session_state:
    st.session_state.history = []

# Top Bar Language Selection (Float Right visually)
col_lang_left, col_lang_right = st.columns([8, 1])
with col_lang_right:
    lang = st.selectbox("Language", ["English", "Hindi", "Telugu"], key="lang", label_visibility="collapsed")
    t = TRANSLATIONS[lang]

# Centered Logo and Title
st.markdown("""
<div class='botanica-logo-area'>
    <div class='botanica-logo-icon'>🌱</div>
    <h1 class='botanica-title'>AI Driven Crop Disease Detection and Smart Solutions System</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)

col_left, col_space, col_right = st.columns([1.2, 0.1, 2.5])
    
with col_left:
    # Upload
    upload_container = st.container(border=True)
    with upload_container:
        st.markdown(f"""
<div style='display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 15px;'>
<h3 style='font-family: Playfair Display, serif; font-size: 1.4rem; color: #2c3e2e; margin: 0;'>{t['up_img']}</h3>
<span style='font-size: 0.65rem; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.05rem;'>{t['reset']}</span>
</div>
""", unsafe_allow_html=True)
        
        input_type = st.radio("Choose Input Method", ["Upload File", "Camera"], horizontal=True, label_visibility="collapsed")
        
        if input_type != "Upload File":
            st.markdown(f"""
            <div style='background: #f0fdf4; border-radius: 12px; padding: 15px; border: 1px solid #bbf7d0; margin-bottom: 15px;'>
                <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 8px;'>
                    <span class='pulse-green' style='width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block;'></span>
                    <strong style='font-size: 0.85rem; color: #166534; font-family: Inter, sans-serif;'>📷 MOBILE CAMERA ASSISTANT</strong>
                </div>
                <p style='font-size: 0.8rem; color: #15803d; line-height: 1.4; font-family: Inter, sans-serif; margin: 0;'>
                    Please allow browser camera permissions when prompted. If the camera doesn't start:
                    <br>• Tap the <strong>lock icon 🔒</strong> in your browser's address bar.
                    <br>• Set <strong>Camera</strong> permission to <strong>"Allow"</strong> and refresh.
                </p>
            </div>
            <style>
            .pulse-green {{
                animation: pulse-green 2s infinite;
            }}
            @keyframes pulse-green {{
                0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
                70% {{ transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }}
                100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
            }}
            </style>
            """, unsafe_allow_html=True)

        image = None
        if input_type == "Upload File":
            uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, use_container_width=True, caption="Main Specimen")
        else:
            try:
                import streamlit.components.v1 as components
                import os
                parent_dir = os.path.dirname(os.path.abspath(__file__))
                component_dir = os.path.join(parent_dir, "back_camera")
                local_back_camera_input = components.declare_component("local_back_camera_input", path=component_dir)
                
                # Check if we already have a captured image in session state
                if "rear_captured_image" in st.session_state and st.session_state.rear_captured_image is not None:
                    image = st.session_state.rear_captured_image
                    st.image(image, use_container_width=True, caption="Main Specimen (Camera)")
                    
                    if st.button("🔄 Retake Photo", key="retake_rear"):
                        st.session_state.rear_captured_image = None
                        st.session_state.last_file = None
                        if "current_analysis" in st.session_state:
                            del st.session_state.current_analysis
                        st.rerun()
                else:
                    rear_camera_file = local_back_camera_input(height=350, width=450, facingMode="environment", key="rear_camera_widget")
                    if rear_camera_file:
                        if isinstance(rear_camera_file, str) and (rear_camera_file.startswith("data:image") or "," in rear_camera_file):
                            import base64
                            import io
                            base64_data = rear_camera_file.split(",")[1] if "," in rear_camera_file else rear_camera_file
                            img_bytes = base64.b64decode(base64_data)
                            image = Image.open(io.BytesIO(img_bytes))
                        elif isinstance(rear_camera_file, bytes):
                            import io
                            image = Image.open(io.BytesIO(rear_camera_file))
                        else:
                            image = Image.open(rear_camera_file)
                        
                        st.session_state.rear_captured_image = image
                        st.rerun()
            except Exception as e:
                st.error(f"Error loading camera component: {e}")
    


    with col_right:
        nav_selection = st.pills("Navigation", ["ANALYZE", "ENCYCLOPEDIA", "SCHEMES", "HISTORY"], default="ANALYZE", label_visibility="collapsed")
        
        if nav_selection == "ANALYZE" and image is None:
            st.markdown(f"""
<div class='b-main-card'>
<div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; min-height: 400px; color: #888;'>
<div style='font-size: 3rem; margin-bottom: 20px; opacity: 0.4;'>🍃</div>
<h2 style='color: #666; font-family: Playfair Display;'>{t['awaiting']}</h2>
<p style='font-size: 0.9rem;'>{t['awaiting_sub']}</p>
</div>
</div>
""", unsafe_allow_html=True)
        elif nav_selection == "ANALYZE":
            if input_type == "Upload File":
                file_identifier = uploaded_file.name
            else:
                if "rear_captured_image" in st.session_state and st.session_state.rear_captured_image is not None:
                    img_obj = st.session_state.rear_captured_image
                    file_identifier = f"camera_{hash(img_obj.tobytes())}"
                else:
                    file_identifier = "awaiting_camera_capture"
            
            if "current_analysis" not in st.session_state or st.session_state.get("last_file") != file_identifier:
                with st.spinner("Processing Specimen Data..."):
                    time.sleep(1.0) # Slight delay for visual effect on first load
                    disease_en, confidence = predict_disease(image)
                    if not is_leaf(image) or confidence < 45.0:
                        st.session_state.current_analysis = {"valid": False}
                    else:
                        st.session_state.current_analysis = {
                            "valid": True,
                            "disease_en": disease_en,
                            "confidence": confidence
                        }
                        
                        # Add to history exactly once per new image
                        st.session_state.history.append({
                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                            "disease_en": disease_en,
                            "confidence": f"{confidence:.2f}%"
                        })
                st.session_state.last_file = file_identifier
                
            # Render from session state
            analysis = st.session_state.current_analysis
            
            if not analysis["valid"]:
                st.markdown(f"""
<div class='b-main-card'>
<span class='pill-red'>{t['invalid']}</span>
<h1 class='result-title'>{t['invalid_title']}</h1>
<div class='solution-block'>
<h4>{t['system_warning']}</h4>
<p>{t['invalid_desc']}</p>
</div>
</div>
""", unsafe_allow_html=True)
            else:
                disease_en = analysis["disease_en"]
                confidence = analysis["confidence"]
                
                # Dynamically translate based on current selected lang
                disease_translated, solution, new_crops, fertilizer, pesticides, organic = get_recommendations(disease_en, lang)
                
                is_healthy = "healthy" in disease_en.lower()
                status_pill = f"<span class='pill-green'>{t['healthy_pill']}</span>" if is_healthy else f"<span class='pill-red'>{t['infected_pill']}</span>"
                crop_name = disease_translated.split('-')[0].strip() if '-' in disease_translated else t['crop']
                
                # Generate preventive measures bullet points
                sentences = [s.strip() + "." for s in solution.split(".") if len(s.strip()) > 5]
                bullets = "".join([f"<li>{s}</li>" for s in sentences])
                
                st.markdown(f"""
<div class='b-main-card'>
<div style='margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;'>
{status_pill}
<span class='action-btn' style='margin: 0;'>{t['download']}</span>
</div>

<div style='display: flex; gap: 20px; align-items: center; margin-bottom: 25px; flex-wrap: wrap;'>
    <img src='data:image/jpeg;base64,{get_image_base64(image)}' style='width: 120px; height: 120px; object-fit: cover; border-radius: 12px; border: 2px solid #3c5a45; box-shadow: 0 4px 10px rgba(0,0,0,0.1);' />
    <div>
        <div style='margin-bottom: 8px;'>
            <span class='pill-dark'>{t['crop']}: {crop_name.upper()}</span>
            <span style='font-size: 0.65rem; color: #888; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem; margin-left: 10px;'>{t['ai_id']} ({confidence:.1f}%)</span>
        </div>
        <h1 class='result-title' style='margin: 0; font-size: 2.2rem;'>{disease_translated}</h1>
    </div>
</div>

<!-- Internal Fake Tabs -->
<div style='display: flex; gap: 20px; border-bottom: 1px solid #e0e0e0; padding-bottom: 15px; margin-bottom: 30px; margin-top: 30px;'>
<span style='background: #3c5a45; color: white; padding: 6px 16px; border-radius: 20px; font-weight: 600; font-size: 0.8rem;'>{t['diagnosis']}</span>
</div>

<div class='solution-block'>
<h4>{t['rec_solution']}</h4>
<p>{solution}</p>
</div>

<div class='preventive-block'>
<h4>{t['prev_measures']}</h4>
<ul style='padding-left: 20px;'>
{bullets}
<li><strong>{t['rec_fert']}</strong> <span style='color: #3c5a45; font-weight: 500;'>{fertilizer}</span></li>
<li><strong>{t['comp_crops']}</strong> <span style='color: #3c5a45; font-weight: 500;'>{new_crops}</span></li>
<li><strong>{t.get('rec_pest', 'Target Pesticide/Fungicide:')}</strong> <span style='color: #b91c1c; font-weight: 500;'>{pesticides}</span></li>
<li><strong>{t.get('rec_org', 'Organic/Biological Protocol:')}</strong> <span style='color: #15803d; font-weight: 500;'>{organic}</span></li>
</ul>
</div>

<div style='margin-top: 35px;'>
<span class='action-btn'>{t['rate']}</span>
<span class='action-btn'>{t['fix']}</span>
</div>
</div>
""", unsafe_allow_html=True)

        elif nav_selection == "ENCYCLOPEDIA":
            enc_tab = st.pills("Encyclopedia Tabs", [t['enc_t1'], t['enc_t2'], t['enc_t3']], default=t['enc_t1'], label_visibility="collapsed")
            
            # Custom helper to strip HTML tags and convert them to clean Markdown styling
            def clean_html_to_markdown(text):
                if not isinstance(text, str):
                    return text
                text = text.replace("<strong>", "**").replace("</strong>", "**")
                text = text.replace("<em>", "*").replace("</em>", "*")
                text = text.replace("<b>", "**").replace("</b>", "**")
                text = text.replace("<i>", "*").replace("</i>", "*")
                return text

            # We style this using Streamlit containers to look like a solid card!
            with st.container(border=True):
                st.markdown(f"<h2 class='result-title' style='margin-top: 0;'>{t['enc_title']}</h2>", unsafe_allow_html=True)
                
                if enc_tab == t['enc_t1']:
                    crop_select_labels = {
                        "English": "Select Crop to Explore",
                        "Hindi": "अन्वेषण के लिए फसल चुनें",
                        "Telugu": "అన్వేషించడానికి పంటను ఎంచుకోండి"
                    }
                    
                    available_crops = list(disease_database.CROP_DATA.keys())
                    crop_options = {}
                    for key in available_crops:
                        crop_name = disease_database.CROP_DATA[key].get(lang, disease_database.CROP_DATA[key]["English"])
                        crop_options[crop_name] = key
                    
                    sorted_crop_names = sorted(list(crop_options.keys()))
                    
                    selected_crop_name = st.selectbox(
                        crop_select_labels.get(lang, "Select Crop to Explore"),
                        options=sorted_crop_names,
                        key="encyclopedia_crop_select"
                    )
                    
                    selected_crop_key = crop_options[selected_crop_name]
                    diseases = disease_database.get_crop_diseases_encyclopedia(selected_crop_key, lang)
                    
                    # Localized disease selection labels
                    disease_select_labels = {
                        "English": "Select Disease / Condition",
                        "Hindi": "रोग / स्थिति चुनें",
                        "Telugu": "వ్యాధి / పరిస్థితిని ఎంచుకోండి"
                    }
                    
                    disease_titles = [d["title"] for d in diseases]
                    selected_disease_title = st.selectbox(
                        disease_select_labels.get(lang, "Select Disease / Condition"),
                        options=disease_titles,
                        key="encyclopedia_disease_select"
                    )
                    
                    selected_disease = next(d for d in diseases if d["title"] == selected_disease_title)
                    
                    # Renders a neat sub-container for the selected disease
                    with st.container(border=True):
                        c1, c2 = st.columns([3, 1])
                        with c1:
                            st.markdown(f"### {selected_disease['title']}")
                        with c2:
                            if selected_disease["is_healthy"]:
                                st.success(t['healthy_pill'])
                            else:
                                st.error(t['infected_pill'])
                        
                        # Clean up/prepare lists and elements
                        sol_text = selected_disease['solution']
                        sentences = [s.strip() + "." for s in sol_text.split(".") if len(s.strip()) > 5]
                        bullets = "".join([f"<li>{s}</li>" for s in sentences])
                        
                        target_pest_label = t.get('rec_pest', 'Target Pesticide/Fungicide:')
                        organic_label = t.get('rec_org', 'Organic/Biological Protocol:')
                        
                        pest_html = f"<li><strong>{target_pest_label}</strong> <span style='color: #b91c1c; font-weight: 500;'>{selected_disease['pesticides']}</span></li>" if selected_disease["pesticides"] != "N/A" else ""
                        org_html = f"<li><strong>{organic_label}</strong> <span style='color: #15803d; font-weight: 500;'>{selected_disease['organic']}</span></li>" if selected_disease["organic"] != "N/A" else ""
                        
                        # Render disease recommendations as premium visual HTML components
                        disease_card_html = f"""
<div class='solution-block' style='margin-top: 15px;'>
    <h4>{t['rec_solution']}</h4>
    <p>{sol_text}</p>
</div>

<div class='preventive-block' style='margin-top: 15px; margin-bottom: 5px;'>
    <h4>{t['prev_measures']}</h4>
    <ul style='padding-left: 20px; margin-bottom: 0;'>
        {bullets}
        <li><strong>{t['rec_fert']}</strong> <span style='color: #3c5a45; font-weight: 500;'>{selected_disease['fertilizer']}</span></li>
        <li><strong>{t['comp_crops']}</strong> <span style='color: #3c5a45; font-weight: 500;'>{selected_disease['crops']}</span></li>
        {pest_html}
        {org_html}
    </ul>
</div>
                        """
                        st.markdown(disease_card_html, unsafe_allow_html=True)
                            
                elif enc_tab == t['enc_t2']:
                    st.markdown(f"## {t['enc_t2']}")
                    
                    # pH Management Card
                    st.markdown(f"""
<div class='preventive-block' style='margin-top: 15px;'>
    <h4>🌱 {t['enc_s1_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_s1_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_s1_b1']}</li>
        <li>{t['enc_s1_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Organic Matter Card
                    st.markdown(f"""
<div class='preventive-block' style='margin-top: 15px;'>
    <h4>🍂 {t['enc_s2_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_s2_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_s2_b1']}</li>
        <li>{t['enc_s2_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Cover Crops Card
                    st.markdown(f"""
<div class='preventive-block' style='margin-top: 15px;'>
    <h4>🍀 {t['enc_s3_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_s3_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_s3_b1']}</li>
        <li>{t['enc_s3_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Soil Testing Card
                    st.markdown(f"""
<div class='preventive-block' style='margin-top: 15px; margin-bottom: 10px;'>
    <h4>🔬 {t['enc_s4_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_s4_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_s4_b1']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                else:
                    st.markdown(f"## {t['enc_t3']}")
                    
                    # Drip Irrigation Card
                    st.markdown(f"""
<div class='solution-block' style='margin-top: 15px;'>
    <h4>💧 {t['enc_w1_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_w1_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_w1_b1']}</li>
        <li>{t['enc_w1_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Mulching Card
                    st.markdown(f"""
<div class='solution-block' style='margin-top: 15px;'>
    <h4>🌾 {t['enc_w2_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_w2_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_w2_b1']}</li>
        <li>{t['enc_w2_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Rainwater Harvesting Card
                    st.markdown(f"""
<div class='solution-block' style='margin-top: 15px;'>
    <h4>🌧️ {t['enc_w3_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_w3_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_w3_b1']}</li>
        <li>{t['enc_w3_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)
                    
                    # Smart Scheduling Card
                    st.markdown(f"""
<div class='solution-block' style='margin-top: 15px; margin-bottom: 10px;'>
    <h4>📅 {t['enc_w4_title']}</h4>
    <p style='font-size: 0.95rem; margin-bottom: 10px;'>{t['enc_w4_desc']}</p>
    <ul style='padding-left: 20px; margin-bottom: 0; font-size: 0.9rem;'>
        <li>{t['enc_w4_b1']}</li>
        <li>{t['enc_w4_b2']}</li>
    </ul>
</div>
                    """, unsafe_allow_html=True)

        
        elif nav_selection == "SCHEMES":
            st.markdown(f"<h2 class='result-title' style='margin-bottom: 15px;'>{t['sch_title']}</h2>", unsafe_allow_html=True)
            
            # Category toggle
            sch_cat = st.pills("Category", [t['sch_central'], t['sch_state']], default=t['sch_central'], label_visibility="collapsed")
            
            # Prepare scheme options based on category
            scheme_data = []
            if sch_cat == t['sch_central']:
                for i in range(1, 10):
                    if f"sch_s{i}_title" in t:
                        scheme_data.append({
                            "title": t[f"sch_s{i}_title"],
                            "desc": t[f"sch_s{i}_desc"],
                            "ben": t[f"sch_s{i}_ben"],
                            "link": t[f"sch_s{i}_link"]
                        })
            else:
                # Detect state to show relevant schemes
                detected_state = st.session_state.get('detected_region', 'Andhra Pradesh')
                
                # State indicator
                st.markdown(f"""
                <div style='display: flex; align-items: center; gap: 10px; margin: 10px 0 20px 0; background: #f0fdf4; padding: 10px 18px; border-radius: 50px; border: 1px solid #bbf7d0;'>
                    <span style='width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block;'></span>
                    <span style='font-size: 0.75rem; color: #166534; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05rem;'>Region: {detected_state} (2026 Schemes)</span>
                </div>
                """, unsafe_allow_html=True)
                
                prefix = "ap" if "Andhra" in detected_state else "ts"
                for i in range(1, 5):
                    if f"sch_{prefix}{i}_title" in t:
                         scheme_data.append({
                            "title": t[f"sch_{prefix}{i}_title"],
                            "desc": t[f"sch_{prefix}{i}_desc"],
                            "ben": t[f"sch_{prefix}{i}_ben"],
                            "link": t[f"sch_{prefix}{i}_link"]
                        })
                
            if scheme_data:
                titles = [s['title'] for s in scheme_data]
                selected_title = st.selectbox("Select a Scheme", titles, label_visibility="collapsed")
                selected_scheme = next(s for s in scheme_data if s['title'] == selected_title)
                
                st.markdown(f"""
    <div class='b-main-card' style='margin-top: 20px;'>
        <h3 style='margin: 0 0 15px 0; font-size: 1.8rem; color: #2c3e2e; font-family: Playfair Display, serif;'>{selected_scheme['title']}</h3>
        <p style='font-size: 1.1rem; line-height: 1.6; color: #4a4a4a; margin-bottom: 20px; font-family: Inter, sans-serif;'>{selected_scheme['desc']}</p>
        <div style='background: #f0fdf4; padding: 20px; border-radius: 12px; border: 1px solid #dcfce7;'>
            <h4 style='margin: 0 0 10px 0; color: #166534; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.05rem;'>✅ Key Benefits</h4>
            <p style='font-size: 1rem; color: #166534; margin: 0; line-height: 1.5;'>{selected_scheme['ben']}</p>
        </div>
        <div style='margin-top: 35px; text-align: center;'>
            <a href='{selected_scheme['link']}' target='_blank' style='display: inline-block; background: #3c5a45; color: white; padding: 14px 40px; border-radius: 50px; text-decoration: none; font-family: Inter, sans-serif; font-weight: 700; font-size: 0.9rem; box-shadow: 0 4px 15px rgba(60, 90, 69, 0.2); letter-spacing: 0.05rem;'>
                🚀 {t['sch_apply']}
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        elif nav_selection == "HISTORY":
            if len(st.session_state.history) == 0:
                history_html = f"<div style='background: #e8ede9; padding: 20px; border-radius: 16px; color: #3c5a45; font-family: Inter, sans-serif; text-align: center; font-weight: 500;'>{t['hist_empty']}</div>"
            else:
                history_html = ""
                for item in reversed(st.session_state.history):
                    disease_en = item.get('disease_en', item.get('disease', 'Healthy'))
                    conf = item.get('confidence', '0.00%')
                    timestamp = item.get('timestamp', '')
                    disease_translated, _, _, fertilizer, _, _ = get_recommendations(disease_en, lang)
                    history_html += f"""
    <div class='preventive-block' style='display: flex; justify-content: space-between; align-items: center; padding: 20px; border-radius: 16px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.02);'>
    <div>
    <h3 style='margin: 0 0 8px 0; font-size: 1.3rem; font-family: Playfair Display, serif; color: #2c3e2e;'>{disease_translated}</h3>
    <span class='pill-light' style='margin-right: 10px;'>{t['hist_conf']} {conf}</span>
    <span style='font-size: 0.85rem; color: #666; font-family: Inter, sans-serif;'>{t['hist_fert']} <strong style='color: #3c5a45;'>{fertilizer}</strong></span>
    </div>
    <div style='color: #aaa; font-size: 0.8rem; font-family: Inter, sans-serif;'>{timestamp}</div>
    </div>
    """
                st.markdown(f"""
    <div class='b-main-card'>
    <h2 class='result-title'>{t['hist_title']}</h2>
    {history_html}
    </div>
    """, unsafe_allow_html=True)
