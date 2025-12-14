# Welcome to Coleridge Initiative
***

## Task
The task involves detecting mentions of datasets across thousands of unstructured scientific documents.
The challenge lies in:
Variability of dataset names (abbreviated, partial, or embedded in sentences)
Noise from non-dataset terms and metadata
Maintaining accuracy without losing contextual meaning
Handling large-scale documents efficiently

## Description
To solve this challenge, the workflow includes:
Data Loading & Cleaning: Remove unwanted characters, normalize whitespace, lowercase text, 
remove non-textual noise.
Tokenization & Filtering: Break documents into words, remove stopwords, and keep only relevant tokens.
Frequency Analysis: Count occurrences of dataset names and related keywords.
Exports & Visualization: Produce summaries, statistics, and processed datasets ready for modeling.
The approach enables reliable dataset extraction and produces a cleaned output suitable for 
downstream NLP training, analysis, or machine learning evaluation.

## Installation
use pip install -r requirements.txt to run all libraries. 
If your python version does not correspond to the various versions, install the libraries individually.
Run python -m spacy download en_core_web_sm to enable spacy environment


## Usage
Run each cell on the jupyter notebook to get results. 

and find the presentation in the presentation.txt file


```
./my_coleridge_initiative Project
```

### The Core Team
Tamambang Nji Fru Duna

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
