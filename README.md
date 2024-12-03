# RespiratorySounds

## Description
Ce projet vise à analyser et traiter des enregistrements audio de sons respiratoires pour diagnostiquer diverses conditions médicales. Le projet utilise des techniques de traitement du signal et d'apprentissage automatique pour extraire des caractéristiques des enregistrements audio et les utiliser pour la classification des maladies.

## Structure du projet
La structure du projet est la suivante :

```
.gitignore
data/
    audio_and_txt_files/
    ...
    data.csv
    demographic_info.txt
    filename_differences.txt
    filename_format.txt
    patient_diagnosis.csv
    processed_audio_files/
    processed_data.csv
    selected_files/
    ...
    train.csv
    val.csv
data-analysis.ipynb
exploration.ipynb
handle_imbalance_and_creating_spectrogram_2.ipynb
mst.ipynb
preprocessing_1.ipynb
README.md
split_data.ipynb
```

## Fichiers et dossiers principaux
- `data/`: Contient les données brutes et traitées.
- `data/audio_and_txt_files/`: Contient les fichiers audio et texte bruts.
- `data/processed_audio_files/`: Contient les fichiers audio traités.
- `data-analysis.ipynb`: Notebook pour l'analyse des données.
- `exploration.ipynb`: Notebook pour l'exploration initiale des données.
- `handle_imbalance_and_creating_spectrogram_2.ipynb`: Notebook pour gérer le déséquilibre des classes et créer des spectrogrammes.
- `mst.ipynb`: Notebook pour la visualisation et l'analyse des données.
- `preprocessing_1.ipynb`: Notebook pour le prétraitement des données.
- `split_data.ipynb`: Notebook pour diviser les données en ensembles d'entraînement et de validation.

## Prérequis
- Python 3.12.0
- Bibliothèques Python : pandas, numpy, TensorFlow, Matplotlib, Librosa, Seaborn, SoundFile

## Installation

Pour installer les dépendances nécessaires, exécutez :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter l'analyse, utilisez le script principal :

```bash
python scripts/main.py
```

## Auteurs

- Alexandre Fayolle
- Florian Brunel
- Mathieu Suchet
- Valentin Poigt
