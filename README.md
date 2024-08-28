# Natural-Language-to-ABAC-Policy-Conversion

![alt text](https://github.com/adityasissodiya/Natural-Language-to-ABAC-Policy-Conversion/blob/main/nLTXPC.png)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Pre-requisites](#pre-requisites)
  - [Running the Application with Docker](#running-the-application-with-docker)
  - [Alternative: Running Locally (Without Docker)](#alternative-running-locally-without-docker)
- [How to Use](#how-to-use)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

This project converts natural language policy descriptions into **Attribute-Based Access Control (ABAC)** policies. ABAC is a highly flexible and scalable method to control access to resources based on attributes (like subject, action, resource, and environmental conditions).

The project processes the natural language policy input using **spaCy** for Natural Language Processing (NLP), extracts relevant entities, and generates an **XACML**-style policy. The policies can then be enforced using the **vakt** library.

### Main Workflow
1. **Input**: Natural language text that describes an access control policy.
2. **NLP**: The policy text is processed to extract subjects, actions, resources, and conditions.
3. **XACML Policy**: The extracted entities are used to generate a policy in XACML format.
4. **Enforcement**: The policy is checked using the vakt library to determine if the given conditions allow or deny access.

## Features
- Process natural language input and extract ABAC entities (subjects, actions, resources, conditions).
- Convert the extracted entities into XACML policy.
- Enforce the policy to determine if access should be granted or denied.
- Web interface to input policies and view results.

## Technologies Used
- **Flask**: Web framework used for the backend.
- **spaCy**: For Natural Language Processing to extract entities.
- **vakt**: For enforcing ABAC policies.
- **Docker**: For containerizing the application, ensuring easy setup and consistent environments.
- **lxml**: For generating XACML policies in XML format.

## Project Structure
```
Natural-Language-to-ABAC-Policy-Conversion/
│
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── nlp_processing.py        # NLP processing with spaCy
│   ├── routes.py                # Defines routes for the web app
│   ├── static/
│   │   └── style.css            # CSS for the web interface
│   ├── templates/
│   │   └── index.html           # HTML page for input/output display
│   └── vakt_integration.py      # Handles ABAC policy enforcement with vakt
│
├── app.py                       # Entry point for the Flask application
├── docker-compose.yml           # Docker Compose configuration file
├── Dockerfile                   # Dockerfile for building the Docker image
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── __pycache__/                 # Cached Python files (ignored)
```

## Setup Instructions

### Pre-requisites
Ensure you have the following installed on your machine:
- **Docker**: Install from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install from [here](https://docs.docker.com/compose/install/).

### Running the Application with Docker

To run the project in a Docker container, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Natural-Language-to-ABAC-Policy-Conversion.git
   cd Natural-Language-to-ABAC-Policy-Conversion
   ```

2. **Build the Docker Image**:
   Docker Compose will use the provided `Dockerfile` to build the image.
   ```bash
   docker-compose build
   ```

3. **Run the Application**:
   Once the image is built, start the application with Docker Compose:
   ```bash
   docker-compose up
   ```

4. **Access the Application**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

5. **Stop the Application**:
   When you're done, stop the containers by pressing `Ctrl+C` or running:
   ```bash
   docker-compose down
   ```

### Alternative: Running Locally (Without Docker)

If you'd like to run the project locally without Docker, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Natural-Language-to-ABAC-Policy-Conversion.git
   cd Natural-Language-to-ABAC-Policy-Conversion
   ```

2. **Create a Virtual Environment**:
   Create a virtual environment to manage dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   Install all required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy Model**:
   Download the spaCy English model required for NLP:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Run the Application**:
   Run the Flask app locally:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## How to Use

1. **Open the Web Interface**: Once the application is running, go to `http://127.0.0.1:5000`.
   
2. **Enter a Policy**: In the input box, enter a natural language policy like:
   ```
   Alice can read the document if she is an employee.
   ```

3. **Process the Policy**: Click on the "Process" button. The application will:
   - Extract entities (subject, action, resource, and condition).
   - Generate a corresponding XACML policy.
   - Simulate enforcement of the policy.

4. **View the Results**: The extracted entities, generated XACML policy, and enforcement result ("Access Granted" or "Access Denied") will be displayed below the form.
---