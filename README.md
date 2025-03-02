# Kaggle Data Cleaning Challenge

## Overview
This repository contains Jupyter notebooks for the **Kaggle Data Cleaning Challenge**, a hands-on project focused on improving data quality through various preprocessing techniques. The challenge consists of five key tasks:

1. **Handling Missing Values** – Identifying and addressing missing data issues.
2. **Parsing Dates** – Standardizing date formats for consistency.
3. **Scaling and Normalizing Data** – Preparing numerical data for analysis by applying appropriate transformations.
4. **Handling Character Encodings** – Resolving text encoding issues to ensure data integrity.
5. **Fixing Inconsistent Data Entry** – Standardizing categorical values to remove inconsistencies.

These notebooks demonstrate practical data cleaning techniques using Python and `pandas` within a structured Jupyter Lab environment.

## Project Structure
```
Kaggle-Data_Cleaning_Challenge/
│── notebooks/
│   │── nb1-data-cleaning-challenge-handling-missing-values.ipynb
│   │── nb2-data-cleaning-challenge-scale-and-normalize-data.ipynb
│   │── nb3-data-cleaning-challenge-parsing-dates.ipynb
│   │── nb4-data-cleaning-challenge-character-encodings.ipynb
│   │── nb5-data-cleaning-challenge-inconsistent-data-entry.ipynb
│── data/
│   │── d0-raw/          # Raw datasets
│   │── d1-interim/      # Intermediate processed data
│   │── d2-clean/        # Cleaned datasets
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

### 3. Launch Jupyter Lab
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