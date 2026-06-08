def compute_language_match(
required_languages,
candidate_languages
):


    if not required_languages:
        return 100

    matches = 0

    candidate_languages = [
        language.lower()
        for language in candidate_languages
    ]

    for language in required_languages:

        if language.lower() in candidate_languages:
            matches += 1

    return round(
        matches / len(required_languages) * 100,
        2
    )


def compute_certification_match(
required_certifications,
candidate_certifications
):


    if not required_certifications:
        return 100

    matches = 0

    candidate_certifications = [
        cert.lower()
        for cert in candidate_certifications
    ]

    for cert in required_certifications:

        if cert.lower() in candidate_certifications:
            matches += 1

    return round(
        matches / len(required_certifications) * 100,
        2
    )


def compute_education_match(
required_education,
candidate_education
):


    levels = {
        "bac": 1,
        "licence": 2,
        "master": 3,
        "ingénieur": 3,
        "doctorat": 4
    }

    required_score = levels.get(
        required_education.lower(),
        0
    )

    candidate_score = levels.get(
        candidate_education.lower(),
        0
    )

    if candidate_score >= required_score:
        return 100

    if required_score == 0:
        return 0

    return round(
        candidate_score / required_score * 100,
        2
    )

def compute_domain_match(
required_domain,
cv_text
):


    cv_text = cv_text.lower()

    domain_keywords = {

        "software engineering": [
            "python",
            "java",
            "react",
            "sql",
            "docker",
            "django"
        ],

        "finance": [
            "finance",
            "audit",
            "comptabilité",
            "excel"
        ],

        "marketing": [
            "marketing",
            "seo",
            "communication"
        ],

        "medicine": [
            "médecine",
            "hôpital",
            "santé"
        ],

        "data science": [
            "machine learning",
            "tensorflow",
            "pytorch",
            "data analysis"
        ]
    }

    keywords = domain_keywords.get(
        required_domain.lower(),
        []
    )

    if not keywords:
        return 0

    matches = 0

    for keyword in keywords:

        if keyword.lower() in cv_text:
            matches += 1

    return round(
        matches / len(keywords) * 100,
        2
    )