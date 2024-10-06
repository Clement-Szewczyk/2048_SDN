# backend.py

import mysql.connector
import bcrypt

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplace par ton utilisateur MySQL
    password="root",  # Remplace par ton mot de passe MySQL
    database="jeu2048",
    port=3305
)

cursor = db.cursor()

def signup(nom, prenom, adresseMail, motDePasse):
    
    """Inscrit un nouvel utilisateur dans la base de données."""
    hashed_password = bcrypt.hashpw(motDePasse.encode('utf-8'), bcrypt.gensalt())
    print(f"Essayez d'ajouter : {nom}, {prenom}, {adresseMail}")  # Debugging
    try:
        cursor.execute("INSERT INTO Utilisateur (nom, prenom, adresseMail, motDePasse) VALUES (%s, %s, %s, %s)",
                       (nom, prenom, adresseMail, hashed_password))
        db.commit()
        print("Inscription réussie.")  # Debugging
        return True
    except mysql.connector.IntegrityError:
        print("L'adresse email est déjà utilisée.")  # Debugging
        return False
    except Exception as e:
        print(f"Erreur lors de l'inscription : {e}")  # Gestion des erreurs
        return False


def login(adresseMail, motDePasse):
    """Vérifie les informations d'identification de l'utilisateur."""
    cursor.execute("SELECT * FROM Utilisateur WHERE adresseMail=%s", (adresseMail,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(motDePasse.encode('utf-8'), user[4].encode('utf-8')):
        print(f"Connexion réussie pour : {user[1]} {user[2]}, Email : {user[3]}")  # Afficher l'information
        return user  # L'utilisateur est authentifié
    print("Nom d'utilisateur ou mot de passe incorrect.")  # Afficher l'erreur
    return None  # Échec de l'authentification
