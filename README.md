# Kaggle Data Cleaning Challenge

## Overview
This repository contains Jupyter notebooks for the **Kaggle Data Cleaning Challenge**, a hands-on project focused on improving data quality through various preprocessing techniques. The challenge consists of five key tasks:

1. **Handling Missing Values** – Identifying and addressing missing data issues.  
   [Access Notebook on Kaggle](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values)
   
2. **Parsing Dates** – Standardizing date formats for consistency.  
   [Access Notebook on Kaggle](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-parsing-dates)
   
3. **Scaling and Normalizing Data** – Preparing numerical data for analysis by applying appropriate transformations.  
   [Access Notebook on Kaggle](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data)
   
4. **Handling Character Encodings** – Resolving text encoding issues to ensure data integrity.  
   [Access Notebook on Kaggle](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-character-encodings)
   
5. **Fixing Inconsistent Data Entry** – Standardizing categorical values to remove inconsistencies.  
   [Access Notebook on Kaggle](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-inconsistent-data-entry)  
   *(This notebook also provides the dataset for the final task, nb6)*

These notebooks demonstrate practical data cleaning techniques using Python and `pandas` within a structured Jupyter Lab environment.

### Highlight: Data Cleaning in nb6 - Fixing Inconsistent Data Entry

In the **nb6-data-cleaning-challenge-full-cleaning.ipynb** notebook, I demonstrate my ability to clean data by addressing issues of inconsistent data entry, which is a common challenge in real-world datasets. Specifically, I focus on:

- **Identifying Inconsistencies**: I analyse the dataset to find discrepancies such as different formats for categorical variables or variations in text encoding.
  
- **Standardising Categories**: I ensure consistency by converting categorical data to a uniform format. For example, I may merge different spellings of the same value or standardise abbreviations.

- **Handling Invalid Entries**: Any rows with erroneous data (such as invalid or impossible values) are removed or replaced with appropriate substitutes.

- **Creating Cleaned Datasets**: After addressing inconsistencies, I generate a cleaned dataset that is ready for further analysis or modelling.

This task demonstrates my ability to recognise and resolve issues with inconsistent data, ensuring that the dataset is reliable and ready for analysis. The notebook showcases my proficiency in using `pandas` for data manipulation and cleaning techniques.

## Project Structure
```
Kaggle-Data_Cleaning_Challenge/
│── notebooks/
│   │── nb1-data-cleaning-challenge-handling-missing-values.ipynb
│   │── nb2-data-cleaning-challenge-scale-and-normalize-data.ipynb
│   │── nb3-data-cleaning-challenge-parsing-dates.ipynb
│   │── nb4-data-cleaning-challenge-character-encodings.ipynb
│   │── nb5-data-cleaning-challenge-inconsistent-data-entry.ipynb
|   |── nb6-data-cleaning-challenge-full-cleaning.ipyb
│── data/      # Scripts and utilities
│   │── d0-raw/
│   │── d1-interim/
│   │── d2-clean/
│── kaggle_cleaning/      # Scripts and utilities
│   │── config.py
│   │── data.py
│   │── utils.py
│   │── __init__.py
│── scripts/archive/      # Archived scripts
│── LICENSE               # License file
│── README.md             # Project documentation
│── setup.py              # Project setup script
│── .gitignore            # Files and directories to ignore in version control
```

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/jgp-13/kaggle-data-cleaning-challenge
cd Kaggle-Data_Cleaning_Challenge
```

### 2. Set Up the Environment
If using Conda, create and activate the environment:
```bash
conda env create -f environment.yml
conda activate kaggle-cleaning
```
Otherwise, install dependencies manually using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Download the Datasets
- Visit the Kaggle websites to download the datasets used in this challenge:
  - [Handling Missing Values](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values)
  - [Parsing Dates](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-parsing-dates)
  - [Scaling and Normalizing Data](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data)
  - [Handling Character Encodings](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-character-encodings)
  - [Fixing Inconsistent Data Entry (including nb6 dataset)](https://www.kaggle.com/code/rtatman/data-cleaning-challenge-inconsistent-data-entry)
- Place the raw datasets in the `data/d0-raw/` directory.


### 4. Launch Jupyter Lab
```bash
jupyter lab
```

## Dependencies
The required dependencies can be installed via `pip` or Conda. They include:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `jupyterlab`

Ensure your environment is correctly set up to run the notebooks.

## Usage
- Open each notebook under the `notebooks/` directory.
- Follow the markdown instructions and run the provided code cells.
- Modify or experiment with the code to further understand data cleaning techniques.

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is open-source and available under the MIT License.

---

For questions or feedback, reach out via GitHub Issues.