import re

def extract_dates(text):
    pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
    return re.findall(pattern, text)

def extract_stakeholders(text):
    stakeholders = []

    keywords = [
        "Client",
        "Company",
        "Vendor",
        "Employee",
        "Customer",
        "Contractor"
    ]

    for keyword in keywords:
        if keyword.lower() in text.lower():
            stakeholders.append(keyword)

    return list(set(stakeholders))

def extract_risks(text):
    risks = []

    risk_keywords = [
        "risk",
        "penalty",
        "liability",
        "breach",
        "termination"
    ]

    for word in risk_keywords:
        if word.lower() in text.lower():
            risks.append(word)

    return list(set(risks))