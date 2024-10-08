risks = {
    "faible": ["perte de données", "panne système"],
    "modéré": ["intrusion réseau", "vol de données"],
    "élevé": ["cyberattaque", "rançongiciel"]
}

def evaluate_risk(risk_level):
    print(f"Risques au niveau {risk_level}:")
    for risk in risks.get(risk_level, []):
        print(f"- {risk}")

if __name__ == '__main__':
    evaluate_risk("élevé")
