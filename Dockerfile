FROM ubuntu:20.04

# Désactiver les invites interactives pour apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Installer Python et les bibliothèques système nécessaires pour PySide2
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    libglib2.0-0 \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Ajouter un utilisateur non root
RUN groupadd -r appgroup && useradd -m -r -u 1001 -g appgroup appuser

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement le fichier requirements.txt pour PySide2
COPY ./Interface_test_PySide2/requirements.txt /app/Interface_test_PySide2/requirements.txt

# Installer les dépendances Python pour PySide2
RUN pip3 install --no-cache-dir -r /app/Interface_test_PySide2/requirements.txt

# Copier le reste du code source
COPY . /app

# Définir les variables d'environnement
ENV PYTHONPATH=/app

# Exposer le port 80
EXPOSE 80

# Commande par défaut pour exécuter l'application
CMD ["python3", "/app/Interface_test_PySide2/main_window.py"]