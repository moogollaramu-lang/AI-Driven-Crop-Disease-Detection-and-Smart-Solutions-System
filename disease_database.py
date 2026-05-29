# Dynamic Agricultural Disease Database
# Contains comprehensive localized recommendations for all 38 classes of the PlantVillage dataset

CROP_DATA = {
    "apple": {
        "English": "Apple",
        "Hindi": "सेब",
        "Telugu": "ఆపిల్"
    },
    "blueberry": {
        "English": "Blueberry",
        "Hindi": "ब्लूबेरी",
        "Telugu": "బ్లూబెర్రీ"
    },
    "cherry_(including_sour)": {
        "English": "Cherry (Sour)",
        "Hindi": "चेरी (खट्टी)",
        "Telugu": "చెర్రీ (పులుపు)"
    },
    "corn_(maize)": {
        "English": "Corn (Maize)",
        "Hindi": "मक्का",
        "Telugu": "మొక్కజొన్న"
    },
    "grape": {
        "English": "Grape",
        "Hindi": "अंगूर",
        "Telugu": "ద్రాక్ష"
    },
    "orange": {
        "English": "Orange (Citrus)",
        "Hindi": "संतरा (साइट्रस)",
        "Telugu": "నారింజ (సిట్రస్)"
    },
    "peach": {
        "English": "Peach",
        "Hindi": "आड़ू",
        "Telugu": "పీచుపండు"
    },
    "pepper,_bell": {
        "English": "Bell Pepper",
        "Hindi": "शिमला मिर्च",
        "Telugu": "బెల్ పెప్పర్ (మిరప)"
    },
    "potato": {
        "English": "Potato",
        "Hindi": "आलू",
        "Telugu": "బంగాళాదుంప"
    },
    "raspberry": {
        "English": "Raspberry",
        "Hindi": "रसभरी",
        "Telugu": "రాస్ప్బెర్రీ"
    },
    "soybean": {
        "English": "Soybean",
        "Hindi": "सोयाबीन",
        "Telugu": "సోయాబీన్"
    },
    "squash": {
        "English": "Squash",
        "Hindi": "कद्दू / स्क्वैश",
        "Telugu": "గుమ్మడికాయ (స్క్వాష్)"
    },
    "strawberry": {
        "English": "Strawberry",
        "Hindi": "स्ट्रॉबेरी",
        "Telugu": "స్ట్రాబెర్రీ"
    },
    "tomato": {
        "English": "Tomato",
        "Hindi": "टमाटर",
        "Telugu": "టొమాటో"
    }
}

DISEASE_PROFILES = {
    "apple_scab": {
        "English": {
            "name": "Apple Scab",
            "solution": "Fungal infection caused by Venturia inaequalis. Leads to olive-green to black spots on leaves and fruit. Prune trees to increase air circulation and remove fallen leaves to eliminate overwintering spores.",
            "crops": "Pears, Plums, Garlic, Chives (Good companion crops or rotational options)",
            "fertilizer": "NPK 10-10-10 & Calcium sprays (Est. Cost: $18 - $28 / ₹1400 - ₹2200 per kg)",
            "pesticides": "Captan 50% WP (2.5g/L water) or Myclobutanil spray",
            "organic": "Sulfur-based organic fungicide, compost tea sprays"
        },
        "Hindi": {
            "name": "सेब का स्कैब",
            "solution": "वेंचुरिया इनेक्वलिस के कारण होने वाला कवक संक्रमण। पत्तियों और फलों पर जैतून-हरे से काले धब्बे बनते हैं। हवा के संचलन को बढ़ाने के लिए पेड़ों की छंटाई करें और गिरी हुई पत्तियों को नष्ट करें।",
            "crops": "नाशपाती, आलूबुखारा, लहसुन, चाइव्स",
            "fertilizer": "एनपीके 10-10-10 और कैल्शियम स्प्रे (अनुमानित लागत: ₹1400 - ₹2200 प्रति किलो)",
            "pesticides": "कैप्टन 50% WP (2.5 ग्राम/लीटर पानी) या मायक्लोबुटानिल स्प्रे",
            "organic": "सल्फर आधारित जैविक कवकनाशी, कम्पोस्ट चाय स्प्रे"
        },
        "Telugu": {
            "name": "ఆపిల్ స్కాబ్",
            "solution": "వెంచురియా ఇనేక్వాలిస్ వల్ల కలిగే శిలీంధ్ర వ్యాధి. ఆకులు మరియు పండ్లపై ముదురు ఆకుపచ్చ నుండి నల్లటి మచ్చలు ఏర్పడతాయి. గాలి ప్రసరణ పెంచడానికి కొమ్మలను కత్తిరించండి.",
            "crops": "బేరి పండ్లు, ప్లమ్స్, వెల్లుల్లి, ఉల్లిపాయలు",
            "fertilizer": "NPK 10-10-10 మరియు కాల్షియం స్ప్రేలు (అంచనా వ్యయం: ₹1400 - ₹2200 కిలోకు)",
            "pesticides": "క్యాప్టాన్ 50% WP (2.5 గ్రా/లీటరు నీటికి) లేదా మైక్లోబుటానిల్ స్ప్రే",
            "organic": "సల్ఫర్ ఆధారిత సేంద్రీయ శిలీంద్రనాశకాలు, కంపోస్ట్ టీ"
        }
    },
    "black_rot": {
        "English": {
            "name": "Black Rot",
            "solution": "Caused by the fungus Botryosphaeria obtusa (in Apples) or Guignardia bidwellii (in Grapes). Produces dark, rotting spots on fruit and leaves. Remove all mummified fruit from trees and apply targeted fungicides.",
            "crops": "Mustard, Radish, Clover (Good for soil suppression)",
            "fertilizer": "Copper-based fungicide & Balanced NPK 19-19-19 (Est. Cost: $20 - $30 / ₹1500 - ₹2400 per kg)",
            "pesticides": "Mancozeb 75% WP or Tebuconazole 250 EC spray",
            "organic": "Neem oil spray (0.5%), copper sulfate organic sprays"
        },
        "Hindi": {
            "name": "ब्लैक रॉट (काला सड़न)",
            "solution": "कवक जनित रोग। फलों और पत्तियों पर काले, सड़ने वाले धब्बे पैदा करता है। पेड़ों से सभी सूखे और सड़े हुए फलों को हटा दें और लक्षित कवकनाशी का प्रयोग करें।",
            "crops": "सरसों, मूली, तिपतिया घास",
            "fertilizer": "तांबा आधारित कवकनाशी और संतुलित एनपीके 19-19-19 (अनुमानित लागत: ₹1500 - ₹2400 प्रति किलो)",
            "pesticides": "मैनकोज़ेब 75% WP या टेबुकोनाज़ोल 250 EC स्प्रे",
            "organic": "नीम का तेल स्प्रे (0.5%), कॉपर सल्फेट जैविक स्प्रे"
        },
        "Telugu": {
            "name": "బ్లాక్ రాట్ (నల్ల కుళ్లు)",
            "solution": "శిలీంధ్రం వల్ల వచ్చే వ్యాధి. పండ్లు మరియు ఆకులపై నల్లటి, కుళ్ళిపోయే మచ్చలు ఏర్పడతాయి. కుళ్ళిన పండ్లను వెంటనే చెట్ల నుండి తీసివేసి నాశనం చేయాలి.",
            "crops": "ఆవాలు, ముల్లంగి, క్లోవర్",
            "fertilizer": "రాగి ఆధారిత శిలీంద్రనాశకాలు & సమతుల్య NPK 19-19-19 (అంచనా వ్యయం: ₹1500 - ₹2400 కిలోకు)",
            "pesticides": "మాంకోజెబ్ 75% WP లేదా టెబుకొనజోల్ 250 EC పిచికారీ",
            "organic": "వేప నూనె స్ప్రే (0.5%), కాపర్ సల్ఫేట్ సేంద్రీయ స్ప్రేలు"
        }
    },
    "cedar_apple_rust": {
        "English": {
            "name": "Cedar Apple Rust",
            "solution": "A complex fungal disease requiring both apple trees and Junipers to complete its cycle. Produces striking bright orange-yellow spots on leaves. Remove nearby wild junipers if possible.",
            "crops": "Marigolds, Basil, Alfalfa",
            "fertilizer": "NPK 12-12-17 & Myclobutanil fungicide (Est. Cost: $22 - $35 / ₹1700 - ₹2700 per kg)",
            "pesticides": "Propiconazole 25% EC (1ml/L water) or Myclobutanil spray",
            "organic": "Diluted baking soda sprays, organic copper fungicides"
        },
        "Hindi": {
            "name": "सीडर एप्पल रस्ट",
            "solution": "एक जटिल कवक रोग जिसके चक्र को पूरा करने के लिए सेब और जुनिपर दोनों पेड़ों की आवश्यकता होती है। पत्तियों पर चमकीले नारंगी-पीले धब्बे पैदा करता है।",
            "crops": "गेंदा, तुलसी, अल्फाल्फा",
            "fertilizer": "एनपीके 12-12-17 और मायक्लोबुटानिल फफूंदनाशक (अनुमानित लागत: ₹1700 - ₹2700 प्रति किलो)",
            "pesticides": "प्रोपिकोनाज़ोल 25% EC (1 मिली/लीटर पानी) या मायक्लोबुटानिल स्प्रे",
            "organic": "पतला बेकिंग सोडा स्प्रे, जैविक कॉपर कवकनाशी"
        },
        "Telugu": {
            "name": "సీడర్ ఆపిల్ రస్ట్",
            "solution": "ఆపిల్ మరియు జునిపర్ చెట్లు రెండూ అవసరమయ్యే సంక్లిష్ట శిలీంధ్ర వ్యాధి. ఆకులపై ప్రకాశవంతమైన నారింజ-పసుపు రంగు మచ్చలు ఏర్పడతాయి.",
            "crops": "బంతిపువ్వులు, తులసి, అల్ఫాల్ఫా",
            "fertilizer": "NPK 12-12-17 మరియు మైక్లోబుటానిల్ శిలీంద్రనాశకం (అంచనా వ్యయం: ₹1700 - ₹2700 కిలోకు)",
            "pesticides": "ప్రోపికోనజోల్ 25% EC (1 మి.లీ/లీటరు నీటికి) లేదా మైక్లోబుటానిల్ స్ప్రే",
            "organic": "బేకింగ్ సోడా స్ప్రేలు, సేంద్రీయ కాపర్ శిలీంద్రనాశకాలు"
        }
    },
    "powdery_mildew": {
        "English": {
            "name": "Powdery Mildew",
            "solution": "Appears as white, powdery flour-like coating on leaves. Caused by Podosphaera or Erysiphe species. Prune to improve airflow, avoid overhead irrigation, and ensure sunlight access.",
            "crops": "Garlic, Chives, Beans (Good companions)",
            "fertilizer": "Potassium bicarbonate & NPK 15-15-15 (Est. Cost: $12 - $22 / ₹900 - ₹1700 per kg)",
            "pesticides": "Hexaconazole 5% EC (2ml/L) or Dinocap 48% EC spray",
            "organic": "Neem oil, milk-water spray (1:9 ratio), baking soda organic mix"
        },
        "Hindi": {
            "name": "पाउडर जैसी फफूंदी (चूर्णिल आसिता)",
            "solution": "पत्तियों पर सफेद, पाउडर जैसे आटे की परत के रूप में दिखाई देता है। हवा के प्रवाह को बेहतर बनाने के लिए छंटाई करें, ऊपर से सिंचाई से बचें।",
            "crops": "लहसुन, चाइव्स, बीन्स",
            "fertilizer": "पोटेशियम बाइकार्बोनेट और एनपीके 15-15-15 (अनुमानित लागत: ₹900 - ₹1700 प्रति किलो)",
            "pesticides": "हेक्साकोनाज़ोल 5% EC (2 मिली/लीटर) या डिनोकैप स्प्रे",
            "organic": "नीम का तेल, दूध-पानी का स्प्रे (1:9 अनुपात), बेकिंग सोडा जैविक मिश्रण"
        },
        "Telugu": {
            "name": "పౌడరీ మిల్డ్యూ (బూడిద తెగులు)",
            "solution": "ఆకులపై తెల్లటి బూడిద పూతలా కనిపిస్తుంది. గాలి ప్రసరణను మెరుగుపరచడానికి కొమ్మలను కత్తిరించండి, మొక్కల పైనుండి నీరు పోయడం నివారించండి.",
            "crops": "వెల్లుల్లి, ఉల్లిపాయలు, బీన్స్",
            "fertilizer": "పొటాషియం బైకార్బోనేట్ & NPK 15-15-15 (అంచనా వ్యయం: ₹900 - ₹1700 కిలోకు)",
            "pesticides": "హెక్సాకొనజోల్ 5% EC (2 మి.లీ/లీటరు నీటికి) లేదా డైనోకాప్ పిచికారీ",
            "organic": "వేప నూనె, పాలు-నీటి స్ప్రే (1:9 నిష్పత్తి), బేకింగ్ సోడా మిశ్రమం"
        }
    },
    "leaf_spot": {
        "English": {
            "name": "Cercospora / Septoria Leaf Spot",
            "solution": "Fungal pathogen causing small circular spots with light-colored centers on foliage. Spread by water splashes. Keep foliage dry, use drip irrigation, and remove heavily affected lower leaves.",
            "crops": "Carrots, Peas, Mustard (Good cover crops)",
            "fertilizer": "NPK 10-20-20 & Micronutrient Zinc / Boron (Est. Cost: $14 - $24 / ₹1100 - ₹1900 per kg)",
            "pesticides": "Propiconazole 25% EC or Carbendazim 50% WP spray (1g/L)",
            "organic": "Copper soap spray, Trichoderma viride biological bio-agent"
        },
        "Hindi": {
            "name": "लीफ स्पॉट (पत्ती धब्बा रोग)",
            "solution": "कवक जनित रोग जो पत्तियों पर हल्के रंग के केंद्रों के साथ छोटे गोल धब्बे पैदा करता है। पत्तों को सूखा रखें, ड्रिप सिंचाई का उपयोग करें।",
            "crops": "गाजर, मटर, सरसों",
            "fertilizer": "एनपीके 10-20-20 और सूक्ष्म पोषक तत्व जिंक / बोरॉन (अनुमानित लागत: ₹1100 - ₹1900 प्रति किलो)",
            "pesticides": "प्रोपिकोनाज़ोल 25% EC या कार्बेन्डाजिम 50% WP स्प्रे",
            "organic": "कॉपर साबुन स्प्रे, ट्राइकोडर्मा विरिडी जैविक एजेंट"
        },
        "Telugu": {
            "name": "ఆకు మచ్చ తెగులు (సెప్టోరియా/సెర్కోస్పోరా)",
            "solution": "శిలీంధ్రాల వల్ల ఆకులపై చిన్న వృత్తాకార మచ్చలు ఏర్పడతాయి. ఆకులు తడవకుండా చూసుకోండి, డ్రిప్ ఇరిగేషన్ పద్ధతిని వాడండి.",
            "crops": "క్యారెట్లు, బఠానీలు, ఆవాలు",
            "fertilizer": "NPK 10-20-20 & మైక్రోన్యూట్రియెంట్ జింక్ / బోరాన్ (అంచనా వ్యయం: ₹1100 - ₹1900 కిలోకు)",
            "pesticides": "ప్రోపికోనజోల్ 25% EC లేదా కార్బెండజిమ్ 50% WP స్ప్రే (1 గ్రా/లీటరు)",
            "organic": "కాపర్ సోప్ స్ప్రే, ట్రైకోడెర్మా విరిడే బయో-ఏజెంట్"
        }
    },
    "rust": {
        "English": {
            "name": "Rust Infection",
            "solution": "Puccinia fungal infection. Appears as rust-colored, powdery pustules on the undersides of leaves. Water early in the day so plants dry quickly, and apply sulfur fungicides.",
            "crops": "Marigolds, Mint, Lavender (Natural aromatic repellents)",
            "fertilizer": "Sulfur-rich fertilizer & NPK 10-15-20 (Est. Cost: $16 - $28 / ₹1300 - ₹2100 per kg)",
            "pesticides": "Teubconazole 250 EC (1.5ml/L water) or Mancozeb spray",
            "organic": "Sulfur dust organic applications, garlic extract sprays"
        },
        "Hindi": {
            "name": "रस्ट (गेरुआ रोग)",
            "solution": "पुकिया कवक संक्रमण। पत्तियों के निचले हिस्से पर जंग के रंग के, पाउडर जैसे दाने दिखाई देते हैं। दिन की शुरुआत में पानी दें ताकि पौधे जल्दी सूख सकें।",
            "crops": "गेंदा, पुदीना, लैवेंडर",
            "fertilizer": "सल्फर युक्त उर्वरक और एनपीके 10-15-20 (अनुमानित लागत: ₹1300 - ₹2100 प्रति किलो)",
            "pesticides": "टेबुकोनाज़ोल 250 EC (1.5 मिली/लीटर पानी) या मैनकोज़ेब स्प्रे",
            "organic": "सल्फर धूल अनुप्रयोग, लहसुन का अर्क स्प्रे"
        },
        "Telugu": {
            "name": "రస్ట్ తెగులు (తుప్పు తెగులు)",
            "solution": "శిలీంధ్రాల వల్ల ఆకుల అడుగుభాగంలో తుప్పు రంగు పొడి మచ్చలు ఏర్పడతాయి. ఉదయాన్నే నీరు పెట్టండి, తద్వారా మొక్కలు త్వరగా ఆరిపోతాయి.",
            "crops": "బంతిపువ్వులు, పుదీనా, లావెండర్",
            "fertilizer": "సల్ఫర్ అధికంగా ఉండే ఎరువులు & NPK 10-15-20 (అంచనా వ్యయం: ₹1300 - ₹2100 కిలోకు)",
            "pesticides": "టెబుకొనజోల్ 250 EC (1.5 మి.లీ/లీటరు నీటికి) లేదా మాంకోజెబ్ స్ప్రే",
            "organic": "సల్ఫర్ సేంద్రీయ ప్రయోగాలు, వెల్లుల్లి సారం స్ప్రే"
        }
    },
    "blight": {
        "English": {
            "name": "Northern / General Leaf Blight",
            "solution": "Caused by Exserohilum or Helminthosporium. Results in large cigar-shaped grayish-green lesions on foliage. Crop rotation, tillage, and using resistant cultivars are key.",
            "crops": "Legumes, Oats, Mustard (Great for rotation breaks)",
            "fertilizer": "High Potassium fertilizer & NPK 10-10-20 (Est. Cost: $18 - $30 / ₹1400 - ₹2300 per kg)",
            "pesticides": "Azoxystrobin 23% SC or Mancozeb 75% WP spray",
            "organic": "Compost-based bio-fertilizer tea, Pseudomonas fluorescens spray"
        },
        "Hindi": {
            "name": "उत्तरी / सामान्य लीफ ब्लाइट",
            "solution": "पत्तों पर बड़े सिगार के आकार के धूसर-हरे घाव बनते हैं। फसल चक्रण, जुताई और प्रतिरोधी किस्मों का उपयोग मुख्य उपाय हैं।",
            "crops": "फलियां, जई, सरसों",
            "fertilizer": "उच्च पोटेशियम उर्वरक और एनपीके 10-10-20 (अनुमानित लागत: ₹1400 - ₹2300 प्रति किलो)",
            "pesticides": "एज़ोक्सीस्ट्रोबिन 23% SC या मैनकोज़ेब 75% WP स्प्रे",
            "organic": "कम्पोस्ट आधारित जैव-उर्वरक चाय, स्यूडोमोनास फ्लोरेसेंस स्प्रे"
        },
        "Telugu": {
            "name": "లీఫ్ బ్లైట్ (మచ్చ తెగులు)",
            "solution": "ఆకులపై పెద్ద బూడిద-ఆకుపచ్చ మచ్చలు ఏర్పడతాయి. పంట మార్పిడి, లోతైన దుక్కి మరియు నిరోధక రకాలను ఎంచుకోవడం ప్రధాన నివారణ చర్యలు.",
            "crops": "పప్పుధాన్యాలు, ఓట్స్, ఆవాలు",
            "fertilizer": "పొటాషియం అధికంగా ఉండే ఎరువులు & NPK 10-10-20 (అంచనా వ్యయం: ₹1400 - ₹2300 కిలోకు)",
            "pesticides": "అజోక్సిస్ట్రోబిన్ 23% SC లేదా మాంకోజెబ్ 75% WP పిచికారీ",
            "organic": "సేంద్రీయ కంపోస్ట్ బయో-టీ, సుడోమోనాస్ ఫ్లోరోసెన్స్ స్ప్రే"
        }
    },
    "esca": {
        "English": {
            "name": "Esca (Black Measles)",
            "solution": "A complex wood-rot disease in grapes caused by Phaeomoniella and Phaeoacremonium. Leads to tiger-stripe leaf discoloration. Disinfect pruning tools between cuts.",
            "crops": "Cover crops like Clover or Rye grass to improve soil balance",
            "fertilizer": "NPK 15-5-30 & Trace Iron / Magnesium minerals (Est. Cost: $25 - $40 / ₹1900 - ₹3000 per kg)",
            "pesticides": "Sodium arsenite (Restricted) or specialized systemic fungicides like Carbendazim",
            "organic": "Trichoderma-based pruning wound paste dressings"
        },
        "Hindi": {
            "name": "एस्का (ब्लैक मीजल्स)",
            "solution": "अंगूर में लकड़ी सड़ने का रोग। पत्तियों पर बाघ की धारियों जैसे रंग उड़ जाते हैं। कटाई के उपकरणों को अच्छी तरह कीटाणुरहित करें।",
            "crops": "तिपतिया घास या राई घास",
            "fertilizer": "एनपीके 15-5-30 और लौह / मैग्नीशियम खनिज (अनुमानित लागत: ₹1900 - ₹3000 प्रति किलो)",
            "pesticides": "कार्बेन्डाजिम जैसे प्रणालीगत कवकनाशी स्प्रे",
            "organic": "ट्राइकोडर्मा आधारित प्रूनिंग घाव पेस्ट"
        },
        "Telugu": {
            "name": "ఎస్కా (నల్ల పొక్కు తెగులు)",
            "solution": "ద్రాక్ష కొమ్మల కుళ్ళిపోయే సంక్లిష్ట వ్యాధి. ఆకులపై పులి చారల వంటి మచ్చలు ఏర్పడతాయి. కొమ్మలు కత్తిరించే పరికరాలను క్రిమిరహితం చేయండి.",
            "crops": "క్లోవర్ లేదా రై గడ్డి (నేల సమతుల్యత కోసం)",
            "fertilizer": "NPK 15-5-30 & ఐరన్ / మెగ్నీషియం ఖనిజాలు (అంచనా వ్యయం: ₹1900 - ₹3000 కిలోకు)",
            "pesticides": "కార్బెండజిమ్ వంటి ద్రవ శిలీంద్రనాశకాలు",
            "organic": "ట్రైకోడెర్మా ఆధారిత కత్తిరింపు పేస్ట్లు"
        }
    },
    "citrus_greening": {
        "English": {
            "name": "Huanglongbing (Citrus Greening)",
            "solution": "Devastating bacterial disease spread by the Asian citrus psyllid. Leaves show mottled yellowing. Control psyllids immediately and remove heavily infected trees as there is no cure.",
            "crops": "Guava (Acts as natural psyllid repellent when intercropped)",
            "fertilizer": "Nutritional sprays (Zinc, Manganese, Iron) & Balanced Foliar NPK (Est. Cost: $30 - $50 / ₹2200 - ₹3800 per kg)",
            "pesticides": "Imidacloprid 17.8% SL or Thiamethoxam 25% WG to control insect vectors",
            "organic": "Horticultural mineral oils, Neem soap vector sprays"
        },
        "Hindi": {
            "name": "हुआंगलोंगबिंग (साइट्रस ग्रीनिंग)",
            "solution": "एशियाई साइट्रस साइलिड द्वारा फैलाया जाने वाला जीवाणु रोग। पत्तियां चित्तीदार पीली हो जाती हैं। कोई इलाज नहीं होने के कारण संक्रमित पेड़ों को हटा दें।",
            "crops": "अमरूद (साइलिड कीटों के लिए प्राकृतिक निवारक)",
            "fertilizer": "पोषक तत्व स्प्रे (जिंक, मैंगनीज, लोहा) और पर्णीय एनपीके (अनुमानित लागत: ₹2200 - ₹3800 प्रति किलो)",
            "pesticides": "इमिडाक्लोप्रिड 17.8% SL या थायमेथोक्सम कीटों को नियंत्रित करने के लिए",
            "organic": "बागवानी खनिज तेल, नीम साबुन स्प्रे"
        },
        "Telugu": {
            "name": "సిట్రస్ గ్రీనింగ్ (ఆకు పచ్చ తెగులు)",
            "solution": "ఆసియా సిట్రస్ సిల్లిడ్ అనే రెక్కల పురుగు ద్వారా వ్యాపించే బ్యాక్టీరియా వ్యాధి. ఆకులు పసుపు రంగులోకి మారుతాయి. చికిత్స లేనందున సోకిన చెట్లను తొలగించాలి.",
            "crops": "జామ (సహజ నివారణిగా పనిచేస్తుంది)",
            "fertilizer": "పోషక స్ప్రేలు (జింక్, మాంగనీస్, ఐరన్) & ఫోలియర్ NPK (అంచనా వ్యయం: ₹2200 - ₹3800 కిలోకు)",
            "pesticides": "ఇమిడాక్లోప్రిడ్ 17.8% SL లేదా థయామెథోక్సామ్ పురుగుల నివారణకు",
            "organic": "సేంద్రీయ నూనెలు, వేప సబ్బు ద్రావణ పిచికారీ"
        }
    },
    "bacterial_spot": {
        "English": {
            "name": "Bacterial Spot",
            "solution": "Caused by Xanthomonas bacteria. Creates water-soaked lesions that turn dark brown on leaves and fruit. Avoid overhead watering and handle plants only when completely dry.",
            "crops": "Carrots, Garlic, Beans (Rotational crops)",
            "fertilizer": "Copper-based nutritional fertilizer spray & balanced NPK (Est. Cost: $15 - $25 / ₹1200 - ₹2000 per kg)",
            "pesticides": "Streptomycin Sulfate + Tetracycline Hydrochloride (Antibiotic sprays like Plantomycin)",
            "organic": "Copper hydroxide organic spray, Pseudomonas vector control"
        },
        "Hindi": {
            "name": "जीवाणु जनित धब्बा रोग (बैक्टीरियल स्पॉट)",
            "solution": "जैंथोमोनास बैक्टीरिया के कारण होता है। पानी से भीगे हुए घाव बनाता है जो गहरे भूरे हो जाते हैं। ऊपर से पानी देने से बचें।",
            "crops": "गाजर, लहसुन, बीन्स",
            "fertilizer": "कॉपर आधारित पोषक तत्व उर्वरक स्प्रे (अनुमानित लागत: ₹1200 - ₹2000 प्रति किलो)",
            "pesticides": "स्ट्रेप्टोमाइसिन सल्फेट + टेट्रासाइक्लिन हाइड्रोक्लोराइड (एंटीबायोटिक स्प्रे)",
            "organic": "कॉपर हाइड्रोक्साइड जैविक स्प्रे, स्यूडोमोनास बायो-नियंत्रण"
        },
        "Telugu": {
            "name": "బ్యాక్టీరియల్ స్పాట్ (బ్యాక్టీరియా ఆకు మచ్చ తెగులు)",
            "solution": "జాంతోమోనాస్ బ్యాక్టీరియా వల్ల వస్తుంది. ఆకులు మరియు పండ్లపై ముదురు గోధుమ రంగు మచ్చలు ఏర్పడతాయి. మొక్కలపై నీరు చల్లడం నివారించండి.",
            "crops": "క్యారెట్లు, వెల్లుల్లి, బీన్స్",
            "fertilizer": "రాగి ఆధారిత పోషక ఎరువుల స్ప్రే (అంచనా వ్యయం: ₹1200 - ₹2000 కిలోకు)",
            "pesticides": "స్ట్రెప్టోమైసిన్ సల్ఫేట్ + టెట్రాసైక్లిన్ హైడ్రోక్లోరైడ్ (యాంటీబయోటిక్ స్ప్రే)",
            "organic": "కాపర్ హైడ్రాక్సైడ్ సేంద్రీయ స్ప్రే, సుడోమోనాస్ నియంత్రణ"
        }
    },
    "early_blight": {
        "English": {
            "name": "Early Blight",
            "solution": "Fungal infection causing circular brown spots with concentric 'target' rings on older leaves. Prune lower leaves to prevent splash infection from soil spores.",
            "crops": "Legumes, Onions, Marigolds",
            "fertilizer": "Copper Fungicide & NPK 5-10-10 (Est. Cost: $15 - $25 / ₹1200 - ₹2000 per kg)",
            "pesticides": "Mancozeb 75% WP (2g/L water) or Chlorothalonil 75% WP spray",
            "organic": "Bacillus subtilis bio-fungicide, Neem oil spray (5ml/L) with mild soap"
        },
        "Hindi": {
            "name": "अगेती झुलसा (अर्ली ब्लाइट)",
            "solution": "कवक संक्रमण जिसके कारण पुरानी पत्तियों पर संकेंद्रित 'लक्षित' वलयों के साथ गोलाकार भूरे रंग के धब्बे बन जाते हैं। हवा के संचार के लिए निचली पत्तियों की छंटाई करें।",
            "crops": "फलियां, प्याज, गेंदा",
            "fertilizer": "कॉपर फफूंदनाशक और एनपीके 5-10-10 (अनुमानित लागत: ₹1200 - ₹2000 प्रति किलो)",
            "pesticides": "मैनकोज़ेब 75% WP (2 ग्राम/लीटर पानी) या क्लोरोथालोनिल स्प्रे",
            "organic": "बेसिलस सबटिलिस जैव-कवकनाशी, नीम का तेल स्प्रे"
        },
        "Telugu": {
            "name": "ఎర్లీ బ్లైట్",
            "solution": "ఆకులపై వలయాకారంలో గోధుమ రంగు మచ్చలు ఏర్పడే శిలీంధ్ర వ్యాధి. నేల నుండి వ్యాపించకుండా క్రింది ఆకులను కత్తిరించండి.",
            "crops": "పప్పుధాన్యాలు, ఉల్లిపాయలు, బంతిపువ్వు",
            "fertilizer": "రాగి ఆధారిత శిలీంద్రనాశకాలు మరియు NPK 5-10-10 (అంచనా వ్యయం: ₹1200 - ₹2000 కిలోకు)",
            "pesticides": "మాంకోజెబ్ 75% WP (2 గ్రా/లీటరు నీటికి) లేదా క్లోరోథలోనిల్ స్ప్రే",
            "organic": "బాసిల్లస్ సబ్టిలిస్ బయో-ఫంగిసైడ్, వేప నూనె స్ప్రే"
        }
    },
    "late_blight": {
        "English": {
            "name": "Late Blight",
            "solution": "Water-mold disease leading to large water-soaked spots that rot foliage rapidly. Thrives in cool, humid weather. Prune for ventilation and apply protective fungicides.",
            "crops": "Corn, Beans, Cabbage, Carrots",
            "fertilizer": "Chlorothalonil fungicide & Phosphorus-rich fertilizer (Est. Cost: $20 - $35 / ₹1500 - ₹2800 per kg)",
            "pesticides": "Metalaxyl 8% + Mancozeb 64% WP spray (2.5g/L water)",
            "organic": "Compost tea spray, Trichoderma viride bio-control agent"
        },
        "Hindi": {
            "name": "पछेती झुलसा (लेट ब्लाइट)",
            "solution": "जल-फफूंदी रोग जिसके कारण बड़े पानी से भीगे धब्बे बनते हैं जो पत्तियों को तेजी से सड़ा देते हैं। ठंडे, आर्द्र मौसम में फैलता है।",
            "crops": "मक्का, बीन्स, पत्ता गोभी, गाजर",
            "fertilizer": "क्लोरोथालोनिल फफूंदनाशक और फास्फोरस युक्त उर्वरक (अनुमानित लागत: ₹1500 - ₹2800 प्रति किलो)",
            "pesticides": "मेटालेक्सिल 8% + मैनकोज़ेब 64% WP (2.5 ग्राम/लीटर पानी) का छिड़काव करें",
            "organic": "कम्पोस्ट चाय का छिड़काव, ट्राइकोडर्मा विरिडी बायो-कंट्रोल"
        },
        "Telugu": {
            "name": "లేట్ బ్లైట్",
            "solution": "ఆకులను వేగంగా కుళ్ళిపోయేలా చేసే శిలీంధ్ర తెగులు. చల్లటి, తేమతో కూడిన వాతావరణంలో ఇది వేగంగా వ్యాపిస్తుంది. గాలి తగిలేలా కత్తిరించండి.",
            "crops": "మొక్కజొన్న, బీన్స్, క్యాబేజీ, క్యారెట్లు",
            "fertilizer": "క్లోరోథలోనిల్ మరియు భాస్వరం అధికంగా ఉండే ఎరువులు (అంచనా వ్యయం: ₹1500 - ₹2800 కిలోకు)",
            "pesticides": "మెటలాక్సిల్ 8% + మాంకోజెబ్ 64% WP (2.5 గ్రా/లీటరు నీటికి) పిచికారీ చేయండి",
            "organic": "కంపోస్ట్ టీ స్ప్రే, ట్రైకోడెర్మా విరిడే బయో-కంట్రోల్"
        }
    },
    "leaf_scorch": {
        "English": {
            "name": "Leaf Scorch",
            "solution": "Fungal infection (Diplocarpon earlianum in strawberries) or environmental stress. Causes leaves to dry, curl, and turn dark red/purple. Ensure regular irrigation and apply protective organic copper.",
            "crops": "Garlic, Oats, Rye (Good soil balance)",
            "fertilizer": "NPK 15-30-15 & organic mulch for water retention (Est. Cost: $14 - $24 / ₹1100 - ₹1800 per kg)",
            "pesticides": "Mancozeb 75% WP or Carbendazim sprays",
            "organic": "Neem seed kernel extract (NSKE 5%), organic copper hydroxide"
        },
        "Hindi": {
            "name": "लीफ झुलसन (लीफ स्कॉर्च)",
            "solution": "कवक संक्रमण या पर्यावरणीय तनाव। पत्तियां सूखती हैं, मुड़ती हैं और गहरे लाल/बैंगनी रंग की हो जाती हैं। नियमित सिंचाई सुनिश्चित करें।",
            "crops": "लहसुन, जई, राई",
            "fertilizer": "एनपीके 15-30-15 और पानी बनाए रखने के लिए जैविक गीली घास (अनुमानित लागत: ₹1100 - ₹1800 प्रति किलो)",
            "pesticides": "मैनकोज़ेब 75% WP या कार्बेन्डाजिम स्प्रे",
            "organic": "नीम बीज गिरी का अर्क (NSKE 5%), जैविक कॉपर हाइड्रोक्साइड"
        },
        "Telugu": {
            "name": "ఆకు ముడత తెగులు (ఆకు మాడు తెగులు)",
            "solution": "శిలీంధ్రం లేదా పర్యావరణ ఒత్తిడి వల్ల ఆకులు ఎండిపోయి, ముడుచుకుని ముదురు ఎరుపు/ఊదా రంగులోకి మారుతాయి. క్రమం తప్పకుండా నీరు పెట్టండి.",
            "crops": "వెల్లుల్లి, ఓట్స్, రై గడ్డి",
            "fertilizer": "NPK 15-30-15 & తేమను నిలుపుకోవడానికి సేంద్రీయ మల్చింగ్ (అంచనా వ్యయం: ₹1100 - ₹1800 కిలోకు)",
            "pesticides": "మాంకోజెబ్ 75% WP లేదా కార్బెండజిమ్ పిచికారీ",
            "organic": "వేప గింజల కషాయం (NSKE 5%), సేంద్రీయ కాపర్ హైడ్రాక్సైడ్"
        }
    },
    "leaf_mold": {
        "English": {
            "name": "Leaf Mold",
            "solution": "Caused by Passalora fulva. Leads to olive-green mold on the leaf undersides. Thrives in highly humid greenhouses. Reduce relative humidity and increase plant spacing.",
            "crops": "Lettuce, Radish, Basil",
            "fertilizer": "Calcium nitrate & Potassium-rich NPK (Est. Cost: $16 - $26 / ₹1200 - ₹2000 per kg)",
            "pesticides": "Chlorothalonil 75% WP or Azoxystrobin SC spray",
            "organic": "Baking soda and organic mild soap sprays, Trichoderma bio-agent"
        },
        "Hindi": {
            "name": "लीफ मोल्ड (पत्ती फफूंद)",
            "solution": "पत्तियों के निचले हिस्से पर जैतून-हरे रंग की फफूंद बन जाती है। अत्यधिक आर्द्र ग्रीनहाउस में फलता-फूलता है। आर्द्रता कम करें।",
            "crops": "सलाद, मूली, तुलसी",
            "fertilizer": "कैल्शियम नाइट्रेट और पोटेशियम युक्त एनपीके (अनुमानित लागत: ₹1200 - ₹2000 प्रति किलो)",
            "pesticides": "क्लोरोथालोनिल 75% WP या एज़ोक्सीस्ट्रोबिन स्प्रे",
            "organic": "बेकिंग सोडा और जैविक साबुन स्प्रे, ट्राइकोडर्मा"
        },
        "Telugu": {
            "name": "ఆకు బూజు తెగులు (లీఫ్ మోల్డ్)",
            "solution": "ఆకుల అడుగుభాగంలో ముదురు ఆకుపచ్చ బూజు ఏర్పడుతుంది. తేమ ఎక్కువగా ఉండే గ్రీన్ హౌస్ లలో ఇది వేగంగా పెరుగుతుంది. తేమను తగ్గించండి.",
            "crops": "సలాడ్ ఆకులు, ముల్లంగి, తులసి",
            "fertilizer": "కాల్షియం నైట్రేట్ & పొటాషియం అధికంగా ఉండే NPK (అంచనా వ్యయం: ₹1200 - ₹2000 కిలోకు)",
            "pesticides": "క్లోరోథలోనిల్ 75% WP లేదా అజోక్సిస్ట్రోబిన్ పిచికారీ",
            "organic": "బేకింగ్ సోడా మరియు ఆర్గానిక్ సోప్ వాటర్ స్ప్రే, ట్రైకోడెర్మా"
        }
    },
    "spider_mites": {
        "English": {
            "name": "Spider Mites (Two-Spotted)",
            "solution": "Tiny insect pests that suck sap, creating fine white webbing under leaves and yellow speckling. Sprinkling plants with overhead water can wash mites away. Introduce predatory mites.",
            "crops": "Onions, Garlic, Coriander (Natural repelling crops)",
            "fertilizer": "Trace minerals foliar & Seaweed liquid fertilizer (Est. Cost: $15 - $28 / ₹1200 - ₹2100 per kg)",
            "pesticides": "Abamectin 1.9% EC (0.5ml/L water) or Spiromesifen spray",
            "organic": "Neem oil (1%), rosemary oil organic spray, insecticidal soaps"
        },
        "Hindi": {
            "name": "मकड़ी के कण (स्पाइडर माइट्स)",
            "solution": "छोटे कीट जो रस चूसते हैं, जिससे पत्तियों के नीचे महीन जाला बन जाता है। पौधों पर तेज धार से पानी छिड़कने से माइट्स धुल जाते हैं।",
            "crops": "प्याज, लहसुन, धनिया",
            "fertilizer": "ट्रेस खनिज पर्णीय और समुद्री शैवाल तरल उर्वरक (अनुमानित लागत: ₹1200 - ₹2100 प्रति किलो)",
            "pesticides": "एबामेक्टिन 1.9% EC (0.5 मिली/लीटर पानी) या स्पाइरोमेसिफेन स्प्रे",
            "organic": "नीम का तेल (1%), दौनी का तेल स्प्रे, कीटनाशक साबुन"
        },
        "Telugu": {
            "name": "ఎర్ర నల్లి తెగులు (స్పైడర్ మైట్స్)",
            "solution": "ఆకుల రసం పీల్చే చిన్న పురుగులు. ఆకుల అడుగుభాగంలో సన్నని తెల్లటి జాలీలను ఏర్పరుస్తాయి. ఫోర్స్ గా నీరు చల్లితే ఇవి కొట్టుకుపోతాయి.",
            "crops": "ఉల్లిపాయలు, వెల్లుల్లి, కొత్తిమీర",
            "fertilizer": "ఖనిజ లవణాలు & సముద్రపు నాచు ద్రవ ఎరువులు (అంచనా వ్యయం: ₹1200 - ₹2100 కిలోకు)",
            "pesticides": "అబామెక్టిన్ 1.9% EC (0.5 మి.లీ/లీటరు నీటికి) లేదా స్పైరోమెసిఫెన్ స్ప్రే",
            "organic": "వేప నూనె (1%), రోజ్మేరీ ఆయిల్ స్ప్రే, సబ్బు ద్రావణం"
        }
    },
    "target_spot": {
        "English": {
            "name": "Target Spot",
            "solution": "Caused by Corynespora cassiicola. Appears as concentric zoned spots, resembling targets, on leaves. Ensure plants are properly spaced to lower leaf moisture.",
            "crops": "Legumes, Sweet corn, Radish",
            "fertilizer": "NPK 10-10-10 & Copper sulfate protective spray (Est. Cost: $18 - $28 / ₹1300 - ₹2200 per kg)",
            "pesticides": "Chlorothalonil 75% WP or Pyraclostrobin 20% WG spray",
            "organic": "Bordeaux organic mixture spray, Bacillus bio-control agent"
        },
        "Hindi": {
            "name": "टारगेट स्पॉट (लक्ष्य धब्बा)",
            "solution": "पत्तियों पर संकेंद्रित गोलाकार धब्बे दिखाई देते हैं। पत्ती की नमी को कम करने के लिए पौधों के बीच पर्याप्त दूरी सुनिश्चित करें।",
            "crops": "फलियां, मक्का, मूली",
            "fertilizer": "एनपीके 10-10-10 और कॉपर सल्फेट सुरक्षात्मक स्प्रे (अनुमानित लागत: ₹1300 - ₹2200 प्रति किलो)",
            "pesticides": "क्लोरोथालोनिल 75% WP या पाइराक्लोस्ट्रोबिन स्प्रे",
            "organic": "बोर्डो कार्बनिक मिश्रण स्प्रे, बेसिलस बायो-कंट्रोल"
        },
        "Telugu": {
            "name": "టార్గెట్ స్పాట్ (వలయ మచ్చ తెగులు)",
            "solution": "ఆకులపై వలయాకార మచ్చలు ఏర్పడతాయి. ఆకులపై తేమను తగ్గించడానికి మొక్కల మధ్య సరైన అంతరం ఉండేలా నాటాలి.",
            "crops": "పప్పుధాన్యాలు, మొక్కజొన్న, ముల్లంగి",
            "fertilizer": "NPK 10-10-10 & కాపర్ సల్ఫేట్ స్ప్రే (అంచనా వ్యయం: ₹1300 - ₹2200 కిలోకు)",
            "pesticides": "క్లోరోథలోనిల్ 75% WP లేదా పైరాక్లోస్ట్రోబిన్ పిచికారీ",
            "organic": "బోర్డో సేంద్రీయ మిశ్రమం పిచికారీ, బాసిల్లస్ బయో-నియంత్రణ"
        }
    },
    "yellow_leaf_curl_virus": {
        "English": {
            "name": "Yellow Leaf Curl Virus",
            "solution": "Severe viral disease transmitted by Whiteflies. Leaves curl upward, shrink, and turn bright yellow. Use silver reflective mulches and yellow sticky insect traps to control whiteflies.",
            "crops": "Eggplant, Hot peppers (Crops not favored by whiteflies)",
            "fertilizer": "Systemic micronutrients foliar & NPK 10-20-30 (Est. Cost: $25 - $40 / ₹1800 - ₹3000 per kg)",
            "pesticides": "Acetamiprid 20% SP or Diafenthiuron 50% WP to eliminate vector whiteflies",
            "organic": "Neem oil vector sprays, yellow sticky insect traps, insect nets"
        },
        "Hindi": {
            "name": "पीला पत्ता मरोड़ विषाणु (येलो लीफ कर्ल)",
            "solution": "सफेद मक्खियों द्वारा फैलने वाला गंभीर वायरल रोग। पत्तियां ऊपर की ओर मुड़ती हैं और पीली हो जाती हैं। सफेद मक्खियों के लिए पीले चिपचिपे जाल लगाएं।",
            "crops": "बैंगन, तीखी मिर्च",
            "fertilizer": "प्रणालीगत सूक्ष्म पोषक तत्व पर्णीय और एनपीके 10-20-30 (अनुमानित लागत: ₹1800 - ₹3000 प्रति किलो)",
            "pesticides": "सफेद मक्खियों को खत्म करने के लिए एसिटामिप्रिड 20% SP स्प्रे",
            "organic": "नीम का तेल वेक्टर स्प्रे, पीले चिपचिपे कीट जाल"
        },
        "Telugu": {
            "name": "ఆకు ముడత వైరస్ (ఎల్లో లీఫ్ కర్ల్ వైరస్)",
            "solution": "తెల్లదోమ ద్వారా వ్యాపించే తీవ్రమైన వైరస్ వ్యాధి. ఆకులు పైకి ముడుచుకుని పసుపు రంగులోకి మారుతాయి. పసుపు జిగురు బోర్డులను వాడండి.",
            "crops": "వంకాయ, మిరపకాయలు",
            "fertilizer": "ఫోలియర్ మైక్రోన్యూట్రియెంట్లు & NPK 10-20-30 (అంచనా వ్యయం: ₹1800 - ₹3000 కిలోకు)",
            "pesticides": "తెల్లదోమల నివారణకు ఎసిటామిప్రిడ్ 20% SP లేదా డయాఫెంథియురాన్ 50% WP పిచికారీ",
            "organic": "వేప నూనె స్ప్రే, పసుపు జిగురు కార్డ్స్, దోమల నెట్లు"
        }
    },
    "mosaic_virus": {
        "English": {
            "name": "Mosaic Virus",
            "solution": "Highly contagious plant virus causing green-yellow mottling, blistering, and dwarf growth. Spread by aphids or contaminated hands/tools. Remove infected plants immediately; wash hands.",
            "crops": "Marigolds, Garlic, French Beans",
            "fertilizer": "NPK 19-19-19 & Potassium silicate to boost cell walls (Est. Cost: $20 - $35 / ₹1500 - ₹2700 per kg)",
            "pesticides": "No direct cure. Apply Dimethoate 30% EC to control aphids/insect vectors.",
            "organic": "Spray skim milk (proteins block virus entry), clean tools with soap"
        },
        "Hindi": {
            "name": "मोज़ेक विषाणु (मोज़ेक वायरस)",
            "solution": "अत्यधिक संक्रामक वायरस जो हरी-पीली चित्तीदार पत्तियां और बौनापन पैदा करता है। संक्रमित पौधों को तुरंत नष्ट करें; हाथों को साबुन से धोएं।",
            "crops": "गेंदा, लहसुन, फ्रेंच बीन्स",
            "fertilizer": "एनपीके 19-19-19 और सेल की दीवारों को मजबूत करने के लिए पोटेशियम सिलिकेट (अनुमानित लागत: ₹1500 - ₹2700 प्रति किलो)",
            "pesticides": "सीधा कोई इलाज नहीं। एफिड्स को नियंत्रित करने के लिए डाइमेथोएट स्प्रे करें।",
            "organic": "स्किम्ड मिल्क स्प्रे (प्रोटीन वायरस प्रवेश को रोकता है), उपकरण कीटाणुरहित करें"
        },
        "Telugu": {
            "name": "మొజాయిక్ వైరస్",
            "solution": "ఆకులపై పసుపు-ఆకుపచ్చ చారలు ఏర్పడే అతి వేగంగా వ్యాపించే వైరస్. సోకిన మొక్కలను వెంటనే పీకేసి నాశనం చేయాలి. పరికరాలను శుభ్రం చేయాలి.",
            "crops": "బంతిపువ్వులు, వెల్లుల్లి, ఫ్రెంచ్ బీన్స్",
            "fertilizer": "NPK 19-19-19 & కణ గోడలను బలోపేతం చేయడానికి పొటాషియం సిలికేట్ (అంచనా వ్యయం: ₹1500 - ₹2700 కిలోకు)",
            "pesticides": "నేరుగా నివారణ లేదు. దోమలను అరికట్టడానికి డైమెథోయేట్ 30% EC పిచికారీ చేయాలి.",
            "organic": "పాల పొడి నీటి మిశ్రమం పిచికారీ, సబ్బుతో పరికరాలను కడగాలి"
        }
    },
    "healthy": {
        "English": {
            "name": "Healthy Foliage",
            "solution": "Foliage looks vigorous and free of lesions. Keep up consistent irrigation, ensuring proper soil aeration, organic mulching, and balanced seasonal crop rotation.",
            "crops": "Intercrop with Basil, Mint, Parsley, or Spinach for soil nutrient synergy",
            "fertilizer": "Balanced organic vermicompost or NPK 20-20-20 (Est. Cost: $5 - $10 / ₹400 - ₹800 per kg)",
            "pesticides": "None required. Keep observing for early vector signals.",
            "organic": "Diluted Neem oil (0.2%) as an active monthly preventive spray"
        },
        "Hindi": {
            "name": "स्वस्थ पत्तियां",
            "solution": "पत्तियां जोरदार और धब्बों से मुक्त दिखती हैं। उचित मृदा वातन, जैविक मल्चिंग और संतुलित मौसमी फसल चक्र सुनिश्चित करें।",
            "crops": "मिट्टी के स्वास्थ्य के लिए तुलसी, पुदीना, धनिया या पालक के साथ अंतर-फसल",
            "fertilizer": "संतुलित जैविक केंचुआ खाद या एनपीके 20-20-20 (अनुमानित लागत: ₹400 - ₹800 प्रति किलो)",
            "pesticides": "कोई आवश्यक नहीं। कीटों के लिए नियमित निगरानी रखें।",
            "organic": "बचाव के लिए महीने में एक बार हल्के नीम के तेल (0.2%) का छिड़काव"
        },
        "Telugu": {
            "name": "ఆరోగ్యకరమైన ఆకులు",
            "solution": "ఆకులు దృఢంగా మరియు ఎటువంటి తెగుళ్లు లేకుండా ఉన్నాయి. స్థిరమైన నీటి పారుదల మరియు సేంద్రీయ మల్చింగ్ కొనసాగించండి.",
            "crops": "నేల పోషకాల సమతుల్యత కోసం తులసి, పుదీనా లేదా పాలకూరతో అంతర పంట వేయండి.",
            "fertilizer": "సమతుల్య సేంద్రీయ వర్మికంపోస్ట్ లేదా NPK 20-20-20 (అంచనా వ్యయం: ₹400 - ₹800 కిలోకు)",
            "pesticides": "ఏమీ అవసరం లేదు. కేవలం క్రమం తప్పకుండా పరిశీలిస్తూ ఉండండి.",
            "organic": "నివారణ చర్యగా నెలకు ఒకసారి వేప నూనె (0.2%) పిచికారీ చేయండి"
        }
    }
}

def parse_class_name(disease_id):
    """
    Parses a raw class name from classes.txt (e.g. 'Apple___Apple_scab' or 'Tomato___healthy')
    Returns: (crop_key, disease_type)
    """
    disease_id = disease_id.strip()
    if "___" in disease_id:
        parts = disease_id.split("___")
        crop_part = parts[0].lower()
        disease_part = parts[1].lower()
    else:
        # Fallback parsing
        crop_part = "tomato"
        disease_part = disease_id.lower()

    # Determine disease type
    if "healthy" in disease_part:
        disease_type = "healthy"
    elif "early_blight" in disease_part:
        disease_type = "early_blight"
    elif "late_blight" in disease_part:
        disease_type = "late_blight"
    elif "scab" in disease_part:
        disease_type = "apple_scab"
    elif "black_rot" in disease_part:
        disease_type = "black_rot"
    elif "rust" in disease_part:
        if "cedar" in disease_part:
            disease_type = "cedar_apple_rust"
        else:
            disease_type = "rust"
    elif "powdery_mildew" in disease_part:
        disease_type = "powdery_mildew"
    elif "leaf_spot" in disease_part:
        disease_type = "leaf_spot"
    elif "blight" in disease_part:
        disease_type = "blight"
    elif "esca" in disease_part:
        disease_type = "esca"
    elif "greening" in disease_part or "haunglongbing" in disease_part:
        disease_type = "citrus_greening"
    elif "bacterial_spot" in disease_part:
        disease_type = "bacterial_spot"
    elif "scorch" in disease_part:
        disease_type = "leaf_scorch"
    elif "mold" in disease_part:
        disease_type = "leaf_mold"
    elif "spider_mites" in disease_part:
        disease_type = "spider_mites"
    elif "target_spot" in disease_part:
        disease_type = "target_spot"
    elif "yellow_leaf" in disease_part:
        disease_type = "yellow_leaf_curl_virus"
    elif "mosaic" in disease_part:
        disease_type = "mosaic_virus"
    else:
        disease_type = "healthy" # Fallback

    return crop_part, disease_type

def get_all_disease_recommendations(disease_id, lang):
    """
    Generates dynamic localized recommendations for any class name
    """
    crop_part, disease_type = parse_class_name(disease_id)
    
    # Retrieve Crop and Disease Details
    crop_info = CROP_DATA.get(crop_part, {"English": crop_part.capitalize(), "Hindi": crop_part, "Telugu": crop_part})
    disease_info = DISEASE_PROFILES.get(disease_type, DISEASE_PROFILES["healthy"])
    
    crop_translated = crop_info.get(lang, crop_info["English"])
    data = disease_info.get(lang, disease_info["English"])
    
    # Build a custom translated disease title
    # e.g., Tomato - Early Blight -> टमाटर - अगेती झुलसा
    if disease_type == "healthy":
        disease_title = f"{crop_translated} - {data['name']}"
    else:
        disease_title = f"{crop_translated} - {data['name']}"

    return disease_title, data["solution"], data["crops"], data.get("fertilizer", "N/A"), data.get("pesticides", "N/A"), data.get("organic", "N/A")

def get_crop_diseases_encyclopedia(crop_key, lang):
    """
    Returns a list of all diseases associated with a crop key, with details
    """
    # Find all disease profiles that can affect this crop or show all general diseases if crop is general
    results = []
    
    # Read classes.txt if available to find specific class names, otherwise construct simulated ones
    try:
        with open('classes.txt', 'r') as f:
            classes = [line.strip() for line in f.readlines() if line.strip()]
    except:
        classes = []

    crop_classes = [c for c in classes if c.lower().startswith(crop_key.lower() + "___")]
    
    if not crop_classes:
        # Fallback list for the crop if classes.txt is missing
        simulated_diseases = ["healthy"]
        if crop_key == "tomato":
            simulated_diseases += ["early_blight", "late_blight", "bacterial_spot", "yellow_leaf_curl_virus"]
        elif crop_key == "potato":
            simulated_diseases += ["early_blight", "late_blight"]
        elif crop_key == "apple":
            simulated_diseases += ["apple_scab", "black_rot", "cedar_apple_rust"]
        else:
            simulated_diseases += ["leaf_spot"]
        
        for d in simulated_diseases:
            crop_classes.append(f"{crop_key}___{d}")

    for cls in crop_classes:
        disease_title, solution, crops, fertilizer, pesticides, organic = get_all_disease_recommendations(cls, lang)
        _, disease_type = parse_class_name(cls)
        results.append({
            "title": disease_title,
            "solution": solution,
            "crops": crops,
            "fertilizer": fertilizer,
            "pesticides": pesticides,
            "organic": organic,
            "is_healthy": (disease_type == "healthy")
        })
        
    return results
