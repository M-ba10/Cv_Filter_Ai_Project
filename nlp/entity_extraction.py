from email.mime import text
import re

# =========================

# BASES DE DONNÉES

# =========================

SKILLS = [
"python",
"java",
"c++",
"sql",
"react",
"django",
"flask",
"tensorflow",
"pytorch",
"aws",
"docker",
"kubernetes",
"excel",
"autocad",
]

LANGUAGES = [
"anglais",
"français",
"arabe",
"espagnol",
"english",
"french",
"arabic",
"spanish",
]

CERTIFICATIONS = [
"aws",
"pmp",
"cisco",
"toefl",
"ielts",
"scrum",
]

EDUCATION_LEVELS = [
"bac",
"licence",
"master",
"doctorat",
"ingénieur",
]

# =========================

# EXTRACTION EMAIL

# =========================

def extract_email(text):


    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    matches = re.findall(pattern, text)

    return matches[0] if matches else None


# =========================

# EXTRACTION TÉLÉPHONE

# =========================

def extract_phone(text):


    pattern = r"(\+?\d[\d\s\-]{8,15})"

    matches = re.findall(pattern, text)

    return matches[0] if matches else None


# =========================

# EXTRACTION COMPÉTENCES

# =========================

def extract_skills(text):


    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# =========================

# EXTRACTION LANGUES

# =========================

def extract_languages(text):


    text = text.lower()

    found_languages = []

    for language in LANGUAGES:

        if language in text:
            found_languages.append(language)

    return list(set(found_languages))


# =========================

# EXTRACTION CERTIFICATIONS

# =========================

def extract_certifications(text):


    text = text.lower()

    found_certifications = []

    for cert in CERTIFICATIONS:

        if cert in text:
            found_certifications.append(cert)

    return list(set(found_certifications))


# =========================

# EXTRACTION NIVEAU ÉTUDE

# =========================

def extract_education(text):


    text = text.lower()

    for edu in EDUCATION_LEVELS:

        if edu in text:
            return edu

    return "Non détecté"


# =========================

# EXTRACTION EXPÉRIENCE

# =========================

def extract_experience(text):


    text = text.lower()

    pattern = r"(\d+)\s+(ans|years)"

    matches = re.findall(pattern, text)

    years = []

    for match in matches:

        years.append(int(match[0]))

    if years:
        return max(years)

    return 0



def extract_candidate_name(text):


    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 50:
            return line

    return "Nom non détecté"