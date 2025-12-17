# Welcome to Classically Punk
***

## Task
The goal of this project is to classify music tracks into two genres—Classical and Punk—using machine learning.
The main challenge was handling audio processing, extracting useful features, and ensuring the models could learn meaningful patterns.
An additional difficulty occurred because the project was originally developed locally on my computer, but later the code was moved to a Jupyter environment where the dataset could not be loaded, requiring path adjustments and manual dataset extraction.

## Description
This project solves the classification problem by:
Preparing the dataset locally and verifying audio file paths before training.
Extracting audio features using libraries such as librosa (MFCCs, Chroma, Spectral Centroid, Zero-Crossing Rate, etc.).
Building feature vectors and normalizing them for machine learning.
Training multiple classifiers (Random Forest, SVM) to distinguish between Classical and Punk music.
Evaluating performance using accuracy, confusion matrices, and classification reports.
The dataset must remain stored locally, and users should ensure they extract and point to the correct local file path.

## Installation
Install the required dependencies

pip install -r requirements.txt

Ensure the dataset (classically_punk_music_genres or genre) is extracted locally and that the project code points to 
the correct absolute path, such as:

## Usage
Run the main notebook or script to extract features, train models, and evaluate performance:
update the dataset path and make sure the dataset exists in current location as project was moved.
```
./my_classicaly_Punk
```

### The Core Team
Tamambang Nji Fru Duna

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
