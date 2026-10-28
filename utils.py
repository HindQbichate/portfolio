import csv
import os
from datetime import datetime


# ---------- Étape 4 : page Projects ----------

def all_tags(projects):
    tags = set()
    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)
    return sorted(tags)


def filter_projects(projects, chosen):
    if len(chosen) == 0:
        return projects
    result = []
    for project in projects:
        for tag in project["tags"]:
            if tag in chosen:
                result.append(project)
                break
    return result


# ---------- Étape 6 : page Contact ----------

# Q12 : vérifier le formulaire
def check(name, email, message):
    problems = []
    if name.strip() == "":
        problems.append("Please enter your name.")
    if "@" not in email or "." not in email.split("@")[-1]:
        problems.append("Please enter a valid e-mail address.")
    if len(message.strip()) < 10:
        problems.append("Your message must contain at least 10 characters.")
    return problems


# Q13 : enregistrer le message dans messages.csv
def save(name, email, message):
    file_exists = os.path.exists("messages.csv")
    with open("messages.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "name", "email", "message"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        writer.writerow([date, name, email, message])