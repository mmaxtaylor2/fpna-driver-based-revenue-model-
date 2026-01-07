## FP&A Monthly Variance Analysis Workflow

A Python-based FP&A project that combines a driver-based planning model with an automated monthly actual vs budget variance analysis workflow. The project mirrors how FP&A teams translate operating assumptions into forecasts and then reconcile performance through structured variance analysis and management-ready reporting.

## Problem Context

Top-down forecasting approaches often obscure the underlying business drivers that explain financial performance. FP&A teams rely on driver-based planning models and systematic variance analysis to understand why results differ from plan and to communicate those insights clearly to stakeholders.

This project was built to replicate that end-to-end FP&A workflow by linking a driver-based planning model with a Python-driven variance analysis engine and spreadsheet-based dashboards.

## Project Overview

The workflow integrates planning, analysis, and reporting layers commonly used in FP&A:

- A driver-based planning model defining monthly budget assumptions  
- A Python engine performing automated actual vs budget variance analysis  
- Spreadsheet-based dashboards designed for management review  

## Key Components

### 1. Driver-Based Planning Model

- Maintained as a standalone FP&A planning workbook  
- Defines monthly budget assumptions and revenue drivers  
- Serves as the source of truth for variance analysis inputs  

The planning model is located in:

05_planning_models/Monthly Variance Analysis Engine.xlsx

### 2. Monthly Variance Analysis Engine

- Python-based engine comparing actuals vs budget  
- Calculates dollar and percentage variances  
- Applies favorable / unfavorable logic using FP&A conventions  
- Exports structured outputs for downstream reporting  

Core outputs are written to the `03_outputs/` directory for traceability and reuse.

### 3. Dashboards and Reporting Artifacts

- Variance outputs are visualized using Google Sheets pivot tables and charts  
- Dashboards are designed to mirror management-facing FP&A reporting  

A snapshot of the final dashboard is included in:

04_dashboards/monthly_variance_by_account.png


This represents the reporting layer of the workflow rather than exploratory analysis.

## Key Takeaways

- Driver-based planning provides more insight than top-down forecasting  
- Variance analysis is most effective when paired with clear visual reporting  
- Separating planning, analysis, and reporting improves transparency  
- Automating repeatable FP&A workflows improves consistency and scalability  

## Repository Structure

The repository is organized to reflect a typical FP&A workflow rather than a standalone application.

fpna-driver-based-revenue-model/
├── 01_data/ # Actuals and input data
├── 02_models/ # Python variance analysis logic
├── 03_outputs/ # CSV outputs from variance engine
├── 04_dashboards/ # Management-facing reporting artifacts
├── 05_planning_models/ # Driver-based FP&A planning models
├── README.md # Project documentation


