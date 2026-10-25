# Q3 :
# - PROFILE et SKILLS sont des dictionnaires : on trouve une info par son nom (ex. PROFILE["email"]).
# - PROJECTS est une liste de dictionnaires, et "tags" est une liste.
# - TIMELINE est une liste de tuples (années, formation).
#
# J'ai choisi une liste de dictionnaires pour les projets parce que 
# - La liste permet de parcourir les projets facilement avec une boucle for,
#   pour les filtrer et les trier.
# - Le dictionnaire donne un nom à chaque info (ex. projet["year"]), c'est plus clair.
# - Pour ajouter un projet, il suffit d'ajouter un dictionnaire, sans changer le code.


PROFILE = {
    "name": "Hind Qbichate",
    "title": "M1 student in Health and Artificial Intelligence (SIA)",
    "city": "Dijon, France",
    "email": "hind.qbichate@etu.u-bourgogne.fr",
    "github": "https://github.com/HindQbichate",            
    "linkedin": "https://www.linkedin.com/in/hind-qbichate-b607b4234",  
    "about": "I am a first-year master's student in Health and Artificial Intelligence "
             "at the Université de Bourgogne, passionate about applying AI and data "
             "engineering to the medical field. With a research-oriented profile and "
             "a strong command of English, I aim to pursue a PhD in personalised "
             "medicine and medical imaging.",
}

SKILLS = {  # level out of 100
    "Python": 80,
    "Java": 70,
    "C / C++": 70,
    "SQL": 75,
    "Web (HTML, CSS, JavaScript)": 75,
    "R": 60,
    "Git / GitHub": 65,
}

PROJECTS = [
    {
        "title": "Fraud detection system",
        "description": "Intelligent system detecting fraud and budget overruns "
                       "in road construction projects (internship at TGR, Fès).",
        "tags": ["Python", "Machine learning", "Data"],
        "year": 2025,
        "link": "https://github.com/HindQbichate/public-jobs-fraud-detector",
    },
    {
        "title": "Pregnancy follow-up mobile app",
        "description": "Smart mobile application that supports pregnant women "
                       "throughout their pregnancy (PFA project).",
        "tags": ["Mobile", "Health"],
        "year": 2025,
        "link": "https://github.com/HindQbichate/ApplicationSuiviGrossesse",
    },
        {
        "title": "Skin care e-commerce website",
        "description": "Team project online shop for cosmetic products (make-up, skin care) "
                       "built with HTML, CSS and JavaScript.",
        "tags": ["Web", "JavaScript"],
        "year": 2024,
        "link": "https://github.com/IliassNAJEME/TheBeauty",
    },
]

TIMELINE = [
    ("2026 - 2027", "Master 1 Health and Artificial Intelligence (SIA), Université de Bourgogne, Dijon"),
    ("2025 - 2026", "Master 1 Information Systems Engineering applied to AI (IS2IA), ESISA"),
    ("2024 - 2025", "Bachelor's degree in Software Engineering, ESISA"),
    ("2020 - 2021", "Baccalaureate in Life and Earth Sciences"),
    ("2019 - 2020", "Baccalaureate in Physical Sciences (international option)"),
]