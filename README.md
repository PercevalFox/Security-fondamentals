# Security Fundamentals Demo

## Description

**Security-Fundamentals-Demo** est une application web qui illustre les concepts fondamentaux de la sécurité des systèmes d'information à travers une série d'implémentations pratiques. Le projet se concentre sur les aspects suivants :

- **Authentification et Autorisation**
- **Chiffrement de données**
- **Journalisation et Traçabilité**
- **Contrôle d'accès basé sur les rôles (RBAC)**
- **Test d'intégrité des fichiers**
- **Gestion des risques**

L'application est construite avec **Flask (Python)** pour le backend et utilise **SQLite** comme base de données.

## Fonctionnalités

1. **Authentification et Gestion des Sessions** : 
   - Authentification utilisateur avec hachage sécurisé des mots de passe.
   - Gestion des sessions pour garder l'utilisateur connecté.
   
2. **Chiffrement des Données** :
   - Chiffrement et déchiffrement des messages sensibles en utilisant l'AES (système de chiffrement symétrique).

3. **Journalisation et Traçabilité** :
   - Journalisation des actions des utilisateurs pour assurer la traçabilité et la responsabilité des événements.

4. **Contrôle d'Accès Basé sur les Rôles (RBAC)** :
   - Contrôle de l'accès aux ressources en fonction des rôles d'utilisateur (ex: administrateur, utilisateur standard).

5. **Test d'Intégrité des Fichiers** :
   - Vérification de l'intégrité des fichiers à l'aide de sommes de contrôle (hash SHA-256).

6. **Gestion des Risques** :
   - Simule une analyse de risque avec différents niveaux de menaces (faible, modéré, élevé).

## Structure du Projet

```bash
Security-Fundamentals-Demo/
│
├── app.py              # Fichier principal de l'application Flask
├── encryption.py       # Implémentation du chiffrement AES
├── logging_setup.py    # Journalisation des activités utilisateur
├── rbac.py             # Contrôle d'accès basé sur les rôles
├── file_integrity.py   # Test d'intégrité des fichiers avec SHA-256
├── risk_management.py   # Simulation de gestion des risques
├── templates/
│   └── login.html      # Template pour la page de connexion
└── requirements.txt    # Liste des dépendances Python
```

## Prérequis

- Python 3.x
- Pip (gestionnaire de paquets Python)

Installation
Cloner le dépôt :
```
git clone https://github.com/ton_nom_utilisateur/Security-Fundamentals-Demo.git
cd Security-Fundamentals-Demo
```
Créer un environnement virtuel (optionnel mais recommandé) :

```
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```
Installer les dépendances :

```
pip install -r requirements.txt
```
Lancer l'Application

Démarrer l'application Flask :

```
python app.py
```
Ouvrir un navigateur web et aller à l'adresse suivante :

```
http://127.0.0.1:5000/login
```
Utiliser les informations de connexion suivantes pour accéder au tableau de bord :

Nom d'utilisateur : admin
Mot de passe : adminpassword
Fonctionnalités Détailées
1. **Authentification et Sessions**
L'utilisateur doit se connecter pour accéder à des pages protégées comme le tableau de bord. Les mots de passe sont protégés par un hachage sécurisé.

2. **Chiffrement des Données**
Le fichier encryption.py contient une implémentation du chiffrement AES. Exécuter le script pour tester le chiffrement/déchiffrement de données sensibles.

```
python encryption.py
```

3. **Journalisation des Actions**
Les actions des utilisateurs (connexion, accès à des ressources protégées) sont enregistrées dans un fichier app.log. Exécuter logging_setup.py pour voir la journalisation en action.

4. **Contrôle d'Accès Basé sur les Rôles (RBAC)**
Le fichier rbac.py contrôle l'accès aux ressources en fonction des rôles d'utilisateur (administrateur ou utilisateur standard). Un administrateur a accès aux paramètres, tandis que les utilisateurs standards n'ont accès qu'à certaines sections.

5. **Test d'Intégrité des Fichiers**
Le fichier file_integrity.py génère un hash SHA-256 pour vérifier l'intégrité des fichiers.

```
python file_integrity.py
```
6. **Gestion des Risques**
Le fichier risk_management.py simule une analyse des risques pour différents niveaux de menaces.

```
python risk_management.py
```

Contribution
Les contributions sont les bienvenues ! N'hésitez pas à soumettre des issues ou à proposer des pull requests pour améliorer le projet.
