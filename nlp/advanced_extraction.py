def extract_location(text):

    locations = [

        "casablanca",
        "rabat",
        "marrakech",
        "tanger",
        "fes",

        "morocco",
        "france",
        "spain",
        "canada",
        "germany",
        "tunisia",
        "algeria"
    ]

    text = text.lower()

    for location in locations:

        if location in text:
            return location.title()

    return "Non détectée"
def extract_availability(text):

    text = text.lower()

    keywords = {

        "Immédiate": [
            "disponible immédiatement",
            "immediate availability",
            "available immediately"
        ],

        "Préavis 1 mois": [
            "1 mois",
            "one month notice"
        ],

        "Préavis 3 mois": [
            "3 mois",
            "three months notice"
        ]
    }

    for label, patterns in keywords.items():

        for pattern in patterns:

            if pattern in text:
                return label

    return "Non précisée"
def extract_contract_type(text):

    contracts = [
        "cdi",
        "cdd",
        "stage",
        "freelance",
        "alternance"
    ]

    text = text.lower()

    for contract in contracts:

        if contract in text:
            return contract.upper()

    return "Non précisé"
def extract_sector(text):

    sectors = {

        "IT": [
            "software",
            "developer",
            "python",
            "react",
            "django"
        ],

        "Finance": [
            "finance",
            "audit",
            "accounting"
        ],

        "Santé": [
            "hospital",
            "medical",
            "healthcare"
        ],

        "Marketing": [
            "marketing",
            "seo",
            "communication"
        ]
    }

    text = text.lower()

    best_sector = "Non détecté"
    best_score = 0

    for sector, keywords in sectors.items():

        score = sum(
            keyword in text
            for keyword in keywords
        )

        if score > best_score:

            best_score = score
            best_sector = sector

    return best_sector