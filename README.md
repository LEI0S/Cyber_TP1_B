# TP de Paolantoni Jules MIN 2
# 🔐 Password Strength Checker API

## 📄 Description

Une API développée avec **FastAPI** qui évalue la force d’un mot de passe donné. Elle attribue une note et une étiquette descriptive (ex: `weak`, `strong`, etc.) selon plusieurs critères de sécurité. L’API fournit également des **suggestions d’amélioration** pour renforcer les mots de passe jugés faibles.

---

## ✅ Prérequis

Pour exécuter ce projet localement, vous aurez besoin de :

- **Python 3.8+**
- **pip** (généralement fourni avec Python)
- **Git** (optionnel, pour cloner le projet)

---

## ⚙️ Installation

1. Clonez ce dépôt :
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Créez et activez un environnement virtuel Python :
    ```bash
    python -m venv venv
    # Sur macOS/Linux :
    source venv/bin/activate
    # Sur Windows :
    venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Exécution de l'application

Pour lancer l'application localement avec Uvicorn :

```bash
uvicorn main:app --reload
Une fois lancée, l'API est accessible à :

http://127.0.0.1:8000

Documentation interactive : http://127.0.0.1:8000/docs

📡 API Endpoints
🔸 POST /check_password_strength
Description :
Analyse un mot de passe et retourne sa force estimée avec des suggestions d'amélioration.


Corps de la requête :

json
Copier
Modifier
{
  "password": "yourPassword123"
}
Réponse (200 OK) — Exemple :

json
Copier
Modifier
{
  "password": "yourPassword123", 
  "strength": "verystrong", 
  "score": 4,
  "suggestions": ["Add symbols (e.g., !@#$%)"]
}
🔹 GET /health_strength_checker
Description :
Vérifie que l’API fonctionne correctement.

Réponse (200 OK) :

json
Copier
Modifier
{
  "status_strength_checker": "ok"
}
