# Project: Natural Language to ABAC Policy Conversion

## Overview
This project aims to bridge the gap between natural language policy definitions and their implementation in digital access control systems using Attribute-Based Access Control (ABAC). By leveraging natural language processing (NLP) techniques, the project automates the conversion of textual policy descriptions into structured digital formats compatible with ABAC systems.

## Objective
- **Primary Goal**: Automate the translation of natural language access control policies into digital policies for ABAC systems.
- **Secondary Goals**:
  - Improve the accuracy and efficiency of policy translation.
  - Provide a user-friendly interface for non-technical stakeholders to define access control rules.

## Methodology

### 1. Natural Language Processing (NLP)
Using the spaCy library, the project processes and analyzes natural language to extract relevant entities, actions, and conditions that dictate access control.

#### Tools and Technologies
- **spaCy**: A powerful Python library for advanced natural language processing.
- **Python**: The primary programming language used for the project.

### 2. Policy Rule Construction
Based on the extracted data, policy rules are constructed which outline who can perform what actions under which conditions.

### 3. Integration with ABAC Systems
The structured rules are then formatted to be compatible with ABAC systems such as Py-ABAC or Vakt.

### 4. User Interface
A simple web interface allows stakeholders to input policies in natural language and view the converted ABAC rules.

## System Architecture

### Components
1. **NLP Module**: Parses and interprets natural language to identify key elements of access control policies.
2. **Policy Management Module**: Converts parsed data into ABAC-compliant policy rules.
3. **ABAC Engine**: Uses Py-ABAC or Vakt to enforce the policies.
4. **User Interface**: Web-based platform for entering and managing policies.

### Data Flow
1. **Input**: User inputs a policy in natural language.
2. **Processing**: The NLP module processes the text and extracts relevant data.
3. **Conversion**: The Policy Management Module converts the data into ABAC policies.
4. **Output**: The ABAC engine uses these policies to make access decisions.

## Installation

```bash
pip install spacy
python -m spacy download en_core_web_sm
pip install py_abac vakt
