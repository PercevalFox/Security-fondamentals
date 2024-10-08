import logging

# Config du système de logs
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Event log
def log_user_activity(username, action):
    logging.info(f"Utilisateur: {username} | Action: {action}")

if __name__ == '__main__':
    log_user_activity("admin", "Connexion réussie")
    log_user_activity("admin", "ALERTE !!! Tentative d'accès à une ressource protégée")
