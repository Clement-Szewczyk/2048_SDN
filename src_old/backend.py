# backend.py

import mysql.connector
import bcrypt

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplace par ton utilisateur MySQL
    password="",  # Remplace par ton mot de passe MySQL
    database="jeu2048",
    #port=3305
    port=3306
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

    if user and bcrypt.checkpw(motDePasse.encode('utf-8'), user[4].encode('utf-8')):  # Vérifier le mot de passe
        print(f"Connexion réussie pour : {user[1]} {user[2]}, Email : {user[3]}")  # Afficher l'information
        return user[0]  # Retourner l'ID de l'utilisateur 
    
    print("Nom d'utilisateur ou mot de passe incorrect.")  # Afficher l'erreur
    return None  # Échec de l'authentification


def existe_utilisateur(utilisateur_id):
    """Vérifie si un utilisateur existe dans la table profil."""
    cursor.execute("SELECT EXISTS(SELECT 1 FROM profil WHERE utilisateurId=%s)", (utilisateur_id,))
    existe = cursor.fetchone()[0]  # Récupère le résultat de la requête

    return bool(existe)  # Retourne True si l'utilisateur existe, sinon False

def inserer_score(utilisateur_id, meilleur_score):
    """Insère un score dans la table profil pour un utilisateur donné."""
    try:
        cursor.execute("""
            INSERT INTO profil (utilisateurId, dateCreation, meilleurScore)
            VALUES (%s, CURDATE(), %s)
        """, (utilisateur_id, meilleur_score))
        db.commit()
        print("Score inséré avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'insertion du score : {e}")

def afficher_score(utilisateur_id):
    """Renvoie le meilleur score d'un utilisateur donné."""
    cursor.execute("SELECT meilleurScore FROM profil WHERE utilisateurId=%s", (utilisateur_id,))
    meilleur_score = cursor.fetchone()  # Récupérer le meilleur score

    if meilleur_score:
        print("meilleur_score[0] ",meilleur_score[0] )
        return meilleur_score[0]  # Retourne seulement le meilleur score
    else:
        print(f"Aucun score trouvé pour l'utilisateur ID {utilisateur_id}.")
        return 0  # Retourne None si aucun score n'est trouvé


def update_score(utilisateur_id, nouveau_score):
    """Met à jour le meilleur score d'un utilisateur donné si le nouveau score est supérieur."""
    try:
        # Vérifier le meilleur score actuel
        cursor.execute("SELECT meilleurScore FROM profil WHERE utilisateurId=%s", (utilisateur_id,))
        score_actuel = cursor.fetchone()

        if score_actuel is not None:
            meilleur_score = score_actuel[0]
            # Ne mettre à jour que si le nouveau score est supérieur
            if nouveau_score > meilleur_score:
                cursor.execute("""
                    UPDATE profil 
                    SET meilleurScore=%s, dateCreation=CURDATE() 
                    WHERE utilisateurId=%s
                """, (nouveau_score, utilisateur_id))
                db.commit()
                print("Score mis à jour avec succès.")
            else:
                print("Le nouveau score n'est pas supérieur au meilleur score actuel.")
        else:
            print(f"Aucun profil trouvé pour l'utilisateur ID {utilisateur_id}.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour du score : {e}")
