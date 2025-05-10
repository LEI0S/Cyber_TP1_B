# TP Cybersécurité : Sujet B - Vérificateur de Force de Mot de Passe

**Objectif :** L'objectif de ce TP est de vous familiariser avec les bases du développement sécurisé (DevSecOps) en créant une API FastAPI qui évalue la force d'un mot de passe. Vous allez la tester, analyser son code et ses dépendances pour des vulnérabilités, et mettre en place une intégration continue simple avec GitLab CI.

**Durée estimée :** 4 heures

**Prérequis :**
*   Python 3.8+ et pip installés
*   Git installé et configuré
*   Un compte GitLab
*   Un éditeur de code (VS Code, PyCharm, etc.)
*   Une connexion internet

---

## Partie 0 : Mise en Place Initiale

1.  **Clonez le dépôt de base pour le Sujet B :**
    Un dépôt GitLab a été préparé avec les squelettes des fichiers nécessaires pour ce sujet. Clonez-le sur votre machine locale :
    ```bash
    git clone https://gitlab.com/epf-cachan/tp1-sujet-b.git
    cd tp1-sujet-b
    ```
   

2.  **Explorez les fichiers :**
    Vous trouverez les fichiers suivants :
    *   `main.py` : Squelette de l'application FastAPI pour le vérificateur de force de mot de passe (avec des `#TODO`).
    *   `requirements.txt` : Dépendances Python initiales.
    *   `README.md` : Fichier de description du projet (à compléter).
    *   `.gitlab-ci.yml` : Squelette pour l'intégration continue GitLab (avec des `#TODO`).
    *   `tests/test_main.py` : Squelette pour les tests (avec des `#TODO`).

---

## Partie 1 : Création de l'Application FastAPI (Python)

Notre application sera une API qui évalue la force d'un mot de passe fourni par l'utilisateur.

1.  **Créez et activez un environnement virtuel Python :**
    ```bash
    python -m venv venv
    # Sur macOS/Linux:
    source venv/bin/activate
    # Sur Windows (cmd/powershell):
    # venv\Scripts\activate
    ```

2.  **Installez les dépendances :**
    Le fichier `requirements.txt` contient déjà `fastapi` et `uvicorn`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Complétez l'application (`main.py`) :**
    Ouvrez `main.py`. Vous y trouverez de nombreux commentaires `#TODO` qui vous guideront. Votre tâche principale est de :
    *   **Implémenter la fonction `check_password_strength_logic` :**
        *   Suivez les instructions des `#TODO 1` à `#TODO 5` pour évaluer différents critères du mot de passe (longueur, présence de majuscules, minuscules, chiffres, symboles). Utilisez les expressions régulières (`re.search()`) comme suggéré pour détecter les types de caractères.
        *   Incrémentez une variable `score` pour chaque critère rempli.
        *   Construisez une liste de `suggestions` pour améliorer le mot de passe si certains critères ne sont pas respectés.
        *   Au `#TODO 6`, déterminez une catégorie de force (`strength_category`) finale (ex: "very_weak", "weak", "medium", "strong", "very_strong") basée sur le `score` total. Pensez à gérer les cas limites (ex: un mot de passe très court même s'il contient des types de caractères variés devrait rester "faible").
        *   La fonction doit instancier et retourner un objet `PasswordStrengthResponse` contenant le mot de passe original (ou une version masquée), la catégorie de force, le score, et les suggestions.
    *   **Compléter l'endpoint `POST /check_password_strength` :**
        *   Appelez votre fonction `check_password_strength_logic` avec le mot de passe reçu dans `payload.password`.
        *   Retournez le résultat de cette fonction. L'objet `PasswordStrengthResponse` sera automatiquement converti en JSON.

4.  **Lancez l'application localement :**
    ```bash
    uvicorn main:app --reload
    ```
    Ouvrez votre navigateur à `http://127.0.0.1:8000/docs`. Utilisez l'interface Swagger UI pour tester votre endpoint `/check_password_strength` avec différents mots de passe et observer les réponses. Vérifiez également que `/health_strength_checker` fonctionne.

5.  **Rédigez le `README.md` :**
    Complétez le fichier `README.md` pour décrire :
    *   Le but de l'application (vérificateur de force de mot de passe).
    *   Comment installer les dépendances et lancer l'application.
    *   Comment utiliser l'endpoint `/check_password_strength` (format du corps de la requête, exemple de réponse). Référez-vous aux sections `#TO BE COMPLETED BY STUDENTS`.

---

## Partie 2 : Vérification des Normes avec Flake8 (Linting)

Flake8 est un outil qui vérifie que votre code respecte les conventions de style PEP 8 et détecte certaines erreurs de programmation.

1.  **Installez Flake8 :**
    ```bash
    pip install flake8
    ```

2.  **Lancez Flake8 :**
    À la racine de votre projet :
    ```bash
    flake8 .
    ```

3.  **Analysez et corrigez :**
    Flake8 va lister les lignes qui ne respectent pas les normes. Corrigez votre code dans `main.py` et `tests/test_main.py` jusqu'à ce que `flake8 .` ne retourne plus d'erreurs.

---

## Partie 3 : Implémentation des Tests avec Pytest

Pytest est un framework de test populaire pour Python. Nous allons compléter des tests pour vérifier que notre API fonctionne comme attendu.

1.  **Installez Pytest et HTTPX :**
    HTTPX nous permettra de faire des requêtes HTTP vers notre API dans les tests.
    ```bash
    pip install pytest httpx
    ```

2.  **Complétez le fichier de tests (`tests/test_main.py`) :**
    Ouvrez `tests/test_main.py`. Des squelettes de tests sont fournis avec des commentaires `#TODO` :
    *   Le test `test_health_check_strength_checker` est déjà fonctionnel.
    *   Dans `test_check_password_strength_very_weak_short` :
        *   Suivez les `#TODO` pour ajouter des assertions (`assert`) vérifiant que pour un mot de passe très court, la catégorie de force retournée est "very_weak" (ou l'équivalent que vous avez défini), le score est bas, et que la liste des suggestions contient bien une recommandation sur la longueur minimale.
    *   Dans `test_check_password_strength_medium_only_lowercase_and_long` :
        *   Suivez les `#TODO` pour ajouter des assertions vérifiant la catégorie de force (qui devrait être "weak" ou "medium") et que les suggestions incluent l'ajout de majuscules, de chiffres, et de symboles.
    *   Dans `test_check_password_strength_strong_all_criteria` :
        *   Suivez les `#TODO` pour ajouter des assertions vérifiant que pour un mot de passe respectant tous les critères, la catégorie de force est "strong" ou "very_strong", le score est élevé, et qu'il y a peu ou pas de suggestions.
    *   Examinez les tests `test_check_password_strength_missing_payload` et `test_check_password_strength_empty_password`. Ils vérifient la validation des données d'entrée par Pydantic et devraient passer sans modification si votre modèle `PasswordInput` est correctement défini dans `main.py`.

3.  **Lancez Pytest :**
    À la racine de votre projet :
    ```bash
    pytest
    ```
    Assurez-vous que tous vos tests passent. Si ce n'est pas le cas, déboguez votre code applicatif (`main.py`) ou vos tests (`tests/test_main.py`).

4.  **Passez Flake8 sur vos tests :**
    ```bash
    flake8 tests/test_main.py
    ```
    Corrigez les éventuels problèmes de style dans votre fichier de test.

---

## Partie 4 : Analyse de Composition de Logiciels (SCA) avec pip-audit

SCA (Software Composition Analysis) permet de détecter les vulnérabilités connues dans les dépendances de votre projet.

1.  **Générez/Mettez à jour `requirements.txt` :**
    Assurez-vous que toutes vos dépendances (y compris celles de développement comme `flake8`, `pytest`, `httpx`) sont listées.
    ```bash
    pip freeze > requirements.txt
    ```

2.  **Installez pip-audit :**
    ```bash
    pip install pip-audit
    ```

3.  **Lancez pip-audit :**
    ```bash
    pip-audit -r requirements.txt
    ```

4.  **Analysez les résultats :**
    Discutez des éventuels résultats. Avec les dépendances de base, il ne devrait pas y en avoir, mais l'exercice est de comprendre l'outil.

---

## Partie 5 : Analyse Statique de Sécurité (SAST) avec Bandit

SAST (Static Application Security Testing) analyse votre code source pour y déceler des motifs de code potentiellement problématiques en termes de sécurité.

1.  **Installez Bandit :**
    ```bash
    pip install bandit
    ```

2.  **Lancez Bandit :**
    À la racine de votre projet :
    ```bash
    bandit -r . -x venv
    ```
    *L'option `-x venv` exclut le dossier de l'environnement virtuel de l'analyse.*

3.  **Analysez les résultats :**
    Discutez des résultats. Bandit pourrait signaler des problèmes de faible sévérité ou des faux positifs. L'important est de comprendre ce qu'il signale.

---

## Partie 6 : Intégration Continue avec GitLab CI

Nous allons configurer GitLab CI pour qu'il exécute automatiquement Flake8 et Pytest à chaque fois que vous poussez du code sur le dépôt.

1.  **Examinez le fichier `.gitlab-ci.yml` :**
    Ce fichier décrit les "jobs" que GitLab CI doit exécuter.

2.  **Complétez les scripts des jobs :**
    Dans `.gitlab-ci.yml`, trouvez les sections `script:` pour les jobs `flake8_check` et `pytest_run`.
    *   Repérez les commentaires `# TODO: Add the command...` ou `# Students to fill this line`.
    *   Remplacez ces commentaires par les commandes correctes pour exécuter Flake8 (sur tout le projet, ex: `flake8 .`) et Pytest (sur le dossier `tests/`, ex: `pytest tests/`).
    *   Le `before_script` s'assure que les dépendances et outils sont installés dans l'environnement CI.

3.  **Commit et Push sur GitLab :**
    Sauvegardez tout votre travail sur GitLab.
    ```bash
    git add .
    git commit -m "Implemented password strength checker, tests, and analysis tools"
    git push
    ```
    *(Utilisez `git push -u origin main` ou `master` pour le premier push si nécessaire).*

4.  **Vérifiez le Pipeline dans GitLab :**
    Allez sur votre projet GitLab, puis dans la section "CI/CD" > "Pipelines". Vous devriez voir un pipeline en cours d'exécution (ou terminé). Cliquez dessus pour voir l'état de chaque job. S'il y a des erreurs, lisez les logs pour comprendre et corriger votre code ou votre fichier `.gitlab-ci.yml`.

---

## Partie 7 : Vérification de Secrets avec TruffleHog

TruffleHog scanne les dépôts Git à la recherche de secrets qui auraient pu être commités par erreur.

1.  **Installez TruffleHog :**
    ```bash
    pip install trufflehog
    ```

2.  **(Optionnel) Introduisez un faux secret :**
    Pour voir TruffleHog en action, ajoutez temporairement un commentaire dans `main.py` avec une chaîne ressemblant à un secret, par exemple :
    ```python
    # FAKE_DB_PASSWORD = "superS3cretP@ssword!" 
    ```
    N'oubliez pas de le `git add .` et `git commit -m "Test secret"` pour qu'il soit dans l'historique.

3.  **Lancez TruffleHog sur votre dépôt local :**
    ```bash
    trufflehog git file://$(pwd)
    ```

4.  **Analysez les résultats et nettoyez :**
    Si vous aviez ajouté un faux secret, supprimez-le de votre code.

---

Félicitations ! Vous avez mis en place une API de vérification de force de mot de passe, l'avez testée, analysée avec des outils de sécurité, et configuré une CI basique.