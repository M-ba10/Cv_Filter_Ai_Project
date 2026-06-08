def compute_skill_match(
required_skills,
candidate_skills
):


    if not required_skills:
        return 100

    matched = 0

    for skill in required_skills:

        if skill.lower() in [
            s.lower()
            for s in candidate_skills
        ]:
            matched += 1

    return round(
        matched / len(required_skills) * 100,
        2
    )