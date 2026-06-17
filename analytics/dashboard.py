from collections import Counter
import pandas as pd


def build_dataframe(results):

    rows = []

    for candidate in results:

        rows.append({
            "Nom": candidate["name"],
            "Score": candidate["score"],
            "Education": candidate["education"],
            "Experience": candidate["experience"],
            "Location": candidate.get("location", ""),
            "Sector": candidate.get("sector", "")
        })

    return pd.DataFrame(rows)


def get_skills_frequency(results):

    skills = []

    for candidate in results:

        skills.extend(candidate["skills"])

    return Counter(skills)


def get_languages_frequency(results):

    languages = []

    for candidate in results:

        languages.extend(candidate["languages"])

    return Counter(languages)