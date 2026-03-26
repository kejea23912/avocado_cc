# Application Dash — Analyse des ventes d'avocats

Application web interactive développée avec **Python Dash** et **Dash Bootstrap Components**,
permettant d'analyser les ventes d'avocats aux États-Unis entre 2015 et 2018.

---

## Structure du projet

```
avocado_dash/
├── app.py                  ← Point d'entrée de l'application
├── pages/
│   ├── __init__.py
│   ├── page1.py            ← Layout Page 1 (graphiques de comparaison)
│   ├── page1_cb.py         ← Callbacks Page 1
│   ├── page2.py            ← Layout Page 2 (tableau filtrable)
│   ├── page2_cb.py         ← Callbacks Page 2
│   └── page3.py            ← Layout Page 3 (documentation Markdown)
├── assets/
│   ├── style.css           ← Styles CSS personnalisés
│   └── BG.jpg              ← Image de fond
├── datas/
│   └── avocado.csv         ← Jeu de données
├── markdowns/
│   ├── expli1.md           ← Documentation : Accueil
│   ├── expli2.md           ← Documentation : Layout
│   └── expli3.md           ← Documentation : Callbacks
└── README.md               ← Ce fichier
```

---

##  Présentation des pages

### Page 1 — Comparaison des quantités vendues
- Graphique fixe affichant les 6 régions principales (MidSouth, Northeast, SouthCentral, Southeast, TotalUS, West)
- Graphique dynamique mis à jour selon la région sélectionnée dans le menu déroulant

### Page 2 — Affichage des données
- Tableau filtrable par **région** (Dropdown) et par **type d'avocat** (RadioItems)
- Badge affichant le nombre de lignes correspondant aux filtres appliqués
- Tri disponible sur toutes les colonnes

### Page 3 — Aide en ligne
- Documentation affichée dans des **onglets** (Tabs)
- 3 onglets : Accueil, Layout, CallBack

---


**2. Installer les dépendances avec UV**
```bash
uv sync
```

> Si le fichier `pyproject.toml` n'est pas présent, initialiser avec :
> ```bash
> uv init
> uv add dash dash-bootstrap-components pandas plotly
> ```

##  Dépendances principales

| Paquet | Rôle |
|---|---|
| `dash` | Framework principal de l'application |
| `dash-bootstrap-components` | Composants Bootstrap (Card, Badge, Tabs, etc.) |
| `pandas` | Chargement et manipulation du CSV |
| `plotly` | Génération des graphiques interactifs |

---

##  Historique des commits

| Commit | Description |
|---|---|
| `Initial commit` | Initialisation du projet avec UV, structure de base |
| `Commit 1` | Création du layout de la page 1 |
| `Commit 2` | Mise en place des callbacks pour la page 1 |
| `Commit 3` | Création du layout de la page 2 |
| `Commit 4` | Mise en place des callbacks pour la page 2 |
| `Commit 5` | Création du layout de la page 3 |
| `Commit 6` | Passage à une application multipages |
| `Commit 7` | Améliorations finales et nettoyage du code |

---

##  Auteur

**Kenny Jean-elie** — M1 MECEN — Université de Tours 2025/2026