import socket  # Bibliothèque pour gérer les connexions réseau
from datetime import datetime  # Pour afficher le temps de scan

# 1. Demander l'adresse IP ou le nom de domaine à scanner
target = input("Entrez l'adresse IP ou le nom de domaine à scanner : ")
print(f"Scan de l'hôte {target}...")

# 2. Vérifier si l'adresse IP ou le nom de domaine est valide
try:
    target_ip = socket.gethostbyname(target)  # Résout le nom de domaine en adresse IP
    print(f"Adresse IP résolue : {target_ip}")
except socket.gaierror:
    print("Erreur : nom de domaine ou adresse IP invalide.")
    exit()

# 3. Définir la plage de ports à scanner
start_port = int(input("Entrez le port de départ (exemple : 1) : "))
end_port = int(input("Entrez le port de fin (exemple : 100) : "))

# 4. Afficher le début du scan
print(f"\nDébut du scan des ports de {start_port} à {end_port}...")
start_time = datetime.now()

# 5. Scanner les ports
for port in range(start_port, end_port + 1):
    try:
        # Création d'un socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Temps limite pour une connexion
            # Tente une connexion au port
            result = s.connect_ex((target_ip, port))  
            if result == 0:  # 0 signifie "port ouvert"
                print(f"Port {port} : Ouvert")
    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")
        exit()
    except socket.error:
        print(f"Erreur sur le port {port}.")

# 6. Afficher la fin du scan
end_time = datetime.now()
total_time = end_time - start_time
print(f"\nScan terminé en {total_time}.")
