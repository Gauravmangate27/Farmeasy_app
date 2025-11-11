# disease_data.py

disease_info = {
    "Fusarium Wilt": "Symptoms: Plant wilting, yellowing leaves, brown discoloration in stem base.",
    "Dry Root Rot": "Symptoms: Drying and rotting of roots, stunted growth in dry conditions.",
    "Alternaria Leaf Spot": "Symptoms: Circular or irregular brown spots on leaves causing defoliation.",
    "Powdery Mildew": "Symptoms: White powdery fungal growth on leaf surface.",
    "Sterility Mosaic Disease": "Symptoms: Mosaic patterns on leaves, stunted growth, sterility of flowers.",
    "Nete Disease": "Symptoms: Yellowing of leaves, reduced yield mainly in excess rainfall.",
    "Leaf Spot (Cercospora)": "Symptoms: Brown to black spots on leaves, premature leaf drop."
}

stage_durations = {
    "Seedling": (0, 20),
    "Vegetative": (21, 40),
    "Pre-Flower": (41, 50),
    "Flowering": (51, 80),
    "Pod Formation": (81, 120),
    "Maturity": (121, 180)
}

stage_diseases = {
    "Seedling": ["Fusarium Wilt", "Dry Root Rot"],
    "Vegetative": ["Alternaria Leaf Spot", "Powdery Mildew"],
    "Pre-Flower": ["Sterility Mosaic Disease"],
    "Flowering": ["Sterility Mosaic Disease", "Nete Disease"],
    "Pod Formation": ["Nete Disease", "Leaf Spot (Cercospora)"],
    "Maturity": ["Leaf Spot (Cercospora)"]
}
