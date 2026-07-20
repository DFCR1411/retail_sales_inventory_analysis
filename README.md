# Retail Sales & Inventory Analysis

## Project Overview

This project presents an exploratory data analysis of retail sales and inventory data for a multi-store business. The goal is to identify sales patterns, product performance, store-level trends, and potential inventory optimization opportunities.

The analysis is designed as a business-oriented case study, focusing not only on descriptive statistics and visualizations, but also on actionable insights that could support decision-making in a retail environment.

## Business Objective

The main objective of this analysis is to answer the following question:

**How can sales and inventory data be used to identify business opportunities, improve product performance, and support better store-level decisions?**

## Business Questions

This project explores the following questions:

* Which stores generate the highest and lowest sales?
* Which products and categories drive revenue?
* Are there seasonal or time-based sales patterns?
* Which products show strong sales performance?
* Are there signs of overstocking or understocking?
* How does inventory availability relate to sales performance?
* What operational or commercial recommendations can be made from the data?

## Dataset

The dataset used in this project contains retail sales and inventory information from a fictional business scenario. It includes data related to stores, products, sales transactions, and inventory levels.

The dataset is used for educational and portfolio purposes. The analysis simulates a real-world business consulting case.

## General Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── environment.yml    <- Conda environment specification for reproducibility
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, clean data sets for analysis and reporting
│   └── raw            <- The original, immutable data dump
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
└── src                <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    ├── config.py               <- Store useful variables and configuration
    ├── load_data.py            <- Functions to load raw, interim, or processed datasets
    ├── business_metrics.py     <- Code to calculate business KPIs and analytical metrics
    └── plots.py                <- Code to create visualizations 

```

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* VS Code
* Conda / Miniforge

## Analysis Workflow

The project follows a structured data analysis workflow:

1. Data loading and initial inspection
2. Data quality assessment
3. Data cleaning and preparation
4. Exploratory data analysis
5. Sales performance analysis
6. Inventory analysis
7. Store and product performance comparison
8. Business insights and recommendations

## Key Deliverables

* Technical Jupyter Notebook with the full analysis process
* Executive PDF report with key insights and recommendations
* Visualizations exported for reporting and portfolio presentation
* Documented project structure for reproducibility

## Expected Insights

This analysis aims to identify:

* Top-performing stores and products
* Low-performing stores or categories
* Sales trends over time
* Inventory inefficiencies
* Potential stock optimization opportunities
* Business recommendations based on the data

## Repository Status

This project is currently in progress.

Planned next steps:

* Download and document the dataset
* Perform initial data quality checks
* Build the exploratory analysis notebook
* Export key charts
* Create the executive report
* Prepare the project for portfolio presentation

## Author

**Daniel Farid Calvo Ramos**  
Data Analytics & Business Intelligence

## Disclaimer

This project uses a public or simulated dataset for educational and portfolio purposes. Any business recommendations are based on the available data and are intended to demonstrate an analytical workflow rather than provide operational advice for a specific real company.
