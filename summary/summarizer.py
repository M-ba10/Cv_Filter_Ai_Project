def generate_summary(candidate):


    strengths = []
    warnings = []

    # Points forts
    if candidate["experience"] >= 5:
        strengths.append("Expérience professionnelle solide")

    if len(candidate["skills"]) >= 5:
        strengths.append("Nombreuses compétences techniques")

    if len(candidate["languages"]) >= 2:
        strengths.append("Profil multilingue")

    if len(candidate["certifications"]) >= 1:
        strengths.append("Possède des certifications reconnues")

    # Points de vigilance
    if candidate["experience"] < 2:
        warnings.append("Expérience limitée")

    if len(candidate["skills"]) < 3:
        warnings.append("Compétences techniques limitées")

    if len(candidate["languages"]) < 1:
        warnings.append("Langues non clairement identifiées")

    if not warnings:
        warnings.append("Aucun point critique détecté")

    return {
        "strengths": strengths,
        "warnings": warnings
}