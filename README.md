# csalgcm-practical-quiz
Practical Quiz: Detecting Spelling Variants  
Authors: Keisha Ko and Jeannine Ledesma

## How to run:

### I. (OPTIONAL) Cleaning and extracting from the raw text file
> [!NOTE]  
> This process for cleaning and extracting has already been completed by the authors. This entire process is optional. Be warned that the process will take hours to finish when you do want to perform it.

#### Libraries to install (in terminal):
NLTK:  
```python
pip install nltk
```  
CalamanCy:  
```python
pip install calamanCy
```
> [!WARNING]  
> CalamanCy only works on Python 3.12 or lower.

1. To clean and extract everything in one file (faster than second process; might lose progress if something happens):  
   1. Go to `scripts for cleaning dataset` folder
   2. Run `split_dataset.py`
   3. Run `cleaning_files.py`
   4. Run `calamanCy_test.py`
2. To clean and extract everything one-by-one (slower than first process; can save progress if something happens):
   1. Go to `scripts for cleaning dataset` folder
   2. Run `split_dataset.py`
   3. Run `cleaning_files.py`
   4. Run `calamancy_corpus.py`
   5. Run `merge_corpus.py`
  
### II. Detecting Tagalog spelling variants



