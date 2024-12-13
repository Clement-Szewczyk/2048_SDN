import mysql.connector
import bcrypt

class User:
    """Gère les opérations liées à l'utilisateur dans la base de données."""

    def __init__(self, host="localhost", user="root", 
                 password="", database="jeu2048", port=3306):
        """Initialise la connexion à la base de données et prépare le curseur."""
        # Connexion à la base de données MySQL
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.db.cursor()

    def inscription(self, nom, prenom, adresseMail, motDePasse):
        """Inscrit un nouvel utilisateur dans la base de données."""
        
        mddpHashe = bcrypt.hashpw(motDePasse.encode('utf-8'), bcrypt.gensalt())
        print(f"Essayez d'ajouter : {nom}, {prenom}, {adresseMail}")  # Debugging
        try:
            self.cursor.execute("INSERT INTO Utilisateur (nom, prenom, adresseMail, motDePasse) VALUES (%s, %s, %s, %s)",
                                (nom, prenom, adresseMail, 
                                mddpHashe
                    ))
            self.db.commit()
            print("Inscription réussie.")  # Debugging
            return True
        except mysql.connector.IntegrityError:
            print("L'adresse email est déjà utilisée.")  # Debugging
            return False
        except Exception as e:
            print(f"Erreur lors de l'inscription : {e}")  # Gestion des erreurs
            return False

    def seConnecter(self, adresseMail, motDePasse):
        print("adresseMail",adresseMail)
        print("motDePasse",motDePasse)

        """Vérifie les informations d'identification de l'utilisateur."""
        self.cursor.execute("SELECT * FROM Utilisateur WHERE adresseMail=%s", (adresseMail,))
        user = self.cursor.fetchone()

        if user and bcrypt.checkpw(motDePasse.encode('utf-8'), user[4].encode('utf-8')):  # Vérifier le mot de passe
            print(f"Connexion réussie pour : {user[1]} {user[2]}, Email : {user[3]}")  # Afficher l'information
            return user[0]  # Retourner l'ID de l'utilisateur 
        print("Nom d'utilisateur ou mot de passe incorrect.")  # Afficher l'erreur
        return None  # Échec de l'authentification
    

    def emailExiste(self, adresseMail):
     """
     Vérifie si une adresse email existe dans la base de données.
     Retourne l'ID de l'utilisateur si l'email existe, sinon None.
      """
     # Exécuter la requête SQL pour vérifier l'adresse email
     self.cursor.execute("SELECT id FROM Utilisateur WHERE adresseMail=%s", (adresseMail,))
     utilisateur = self.cursor.fetchone()

     if utilisateur:  # Si un utilisateur est trouvé
        print(f"L'adresse email {adresseMail} existe dans la base de données.")
        return utilisateur[0]  # Retourner l'ID de l'utilisateur
     else:  # Aucun utilisateur trouvé
        print(f"Aucun utilisateur trouvé pour l'adresse email {adresseMail}.")
        return None
    

    def modifierMotDePasse(self, adresseMail, nouveauMotDePasse):
     """
     Modifie le mot de passe de l'utilisateur correspondant à l'adresse email donnée.
     """
      # Vérifier si l'email existe
     utilisateurId = self.Email_existe(adresseMail)
     print("user_iddddd",utilisateurId)
     
     mddpHashe = bcrypt.hashpw(nouveauMotDePasse.encode('utf-8'), bcrypt.gensalt())

     if utilisateurId:  # Si l'utilisateur existe
        try:
            # S'assurer que l'email est une chaîne et qu'il est correctement passé à la requête
            emailSaisi = str(adresseMail)  # Cela garantit que l'email est une chaîne
            self.cursor.execute(
                "UPDATE Utilisateur SET motDePasse=%s WHERE adresseMail=%s",
                (
                    mddpHashe
        , emailSaisi)  # Passer l'email comme chaîne
            )
            self.db.commit()
            print(f"Le mot de passe a été modifié pour l'email {emailSaisi}.")
            return True
        except Exception as e:
            print(f"Erreur lors de la modification du mot de passe : {e}")
            return False
     else:
        print(f"Aucun utilisateur trouvé pour l'adresse email {adresseMail}.")
        return False




    def existeUtilisateur(self, utilisateurId):
        """Vérifie si un utilisateur existe dans la table profil."""
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM profil WHERE utilisateurId=%s)", (utilisateurId,))
        existe = self.cursor.fetchone()[0]  # Récupère le résultat de la requête
        return bool(existe)  # Retourne True si l'utilisateur existe, sinon False

    def insererScore(self, utilisateurId, meilleurScore):
        """Insère un score dans la table profil pour un utilisateur donné."""
        try:
            self.cursor.execute("""
                INSERT INTO profil (utilisateurId, dateCreation, meilleurScore)
                VALUES (%s, CURDATE(), %s)
            """, (utilisateurId, meilleurScore))
            self.db.commit()
            print("Score inséré avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'insertion du score : {e}")

    def afficherScore(self, utilisateurId):
        """Renvoie le meilleur score d'un utilisateur donné."""
        self.cursor.execute("SELECT meilleurScore FROM profil WHERE utilisateurId=%s", (utilisateurId,))
        meilleurScore = self.cursor.fetchone()  # Récupérer le meilleur score

        if meilleurScore:
            print("meilleurScore[0] ",meilleurScore[0])
            return meilleurScore[0]  # Retourne seulement le meilleur score
        else:
            print(f"Aucun score trouvé pour l'utilisateur ID {utilisateurId}.")
            return 0  # Retourne None si aucun score n'est trouvé

    def mettreAJourScore(self, utilisateurId, nouveauScore):
        """Met à jour le meilleur score d'un utilisateur donné si le nouveau score est supérieur."""
        try:
            # Vérifier le meilleur score actuel
            self.cursor.execute("SELECT meilleurScore FROM profil WHERE utilisateurId=%s", (utilisateurId,))
            scoreActuel = self.cursor.fetchone()

            if scoreActuel is not None:
                meilleurScore = scoreActuel[0]
                # Ne mettre à jour que si le nouveau score est supérieur
                if nouveauScore > meilleurScore:
                    self.cursor.execute("""
                        UPDATE profil 
                        SET meilleurScore=%s, dateCreation=CURDATE() 
                        WHERE utilisateurId=%s
                    """, (nouveauScore, utilisateurId))
                    self.db.commit()
                    print("Score mis à jour avec succès.")
                else:
                    print("Le nouveau score n'est pas supérieur au meilleur score actuel.")
            else:
                print(f"Aucun profil trouvé pour l'utilisateur ID {utilisateurId}.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour du score : {e}")

    def fermerConnexionBdd(self):
        """Ferme la connexion à la base de données."""
        self.cursor.fermerConnexionBdd()
        self.db.fermerConnexionBdd()


