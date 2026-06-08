def calculate_global_score(
    semantic_score,
    skills_match,
    experience_score,
    education_score,
    language_score,
    certification_score,
    domain_score
):


    final_score = (
        semantic_score * 0.35
        + skills_match * 0.20
        + experience_score * 0.15
        + education_score * 0.10
        + language_score * 0.08
        + certification_score * 0.05
        + domain_score * 0.07
   )

    return round(final_score, 2)