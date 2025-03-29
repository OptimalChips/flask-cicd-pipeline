Project:
  Name: "Flask CI/CD Pipeline"
  Description: >
    This project is a simple Flask web application that serves an interactive
    profile page. It is containerized with Docker and uses a CI/CD pipeline
    (configured with GitHub Actions) to automate testing, building, and deployment.

Features:
  - "Flask Web App: Displays an interactive profile with HTML, CSS, and JavaScript."
  - "Interactive UI: Includes a toggle button that changes the page style."
  - "Dockerized: Containerized for consistent deployment."
  - "CI/CD Pipeline: Automated build, test, and deployment via GitHub Actions."
  - "Configurable Port: Uses an environment variable to set the running port."

ProjectStructure:
  - "app.py: Main Flask application"
  - "requirements.txt: Python dependencies"
  - "Dockerfile: Docker configuration"
  - "README.md: Project documentation"
  - "templates/index.html: HTML template for the interactive profile page"
  - "static/styles.css: CSS for styling the webpage"
  - "static/script.js: JavaScript for interactivity"

Installation:
  - "Clone the repository: git clone https://github.com/OptimalChips/flask-cicd-pipeline.git"
  - "Navigate to the repository: cd flask-cicd-pipeline"
  - "Set up a virtual environment: python3 -m venv env"
  - "Activate the virtual environment: source env/bin/activate (on Windows use: env\\Scripts\\activate)"
  - "Install dependencies: pip install -r requirements.txt"

RunningLocally:
  - "Set the PORT environment variable (optional, default is 5000): export PORT=5001"
  - "Run the Flask app: python app.py"
  - "Access the app in a web browser: http://localhost:5000 (or http://localhost:5001 if PORT is changed)"

Docker:
  - "Build the Docker image: docker build -t optimalchips/flask-cicd-pipeline:latest ."
  - "Run the Docker container: docker run -p 5001:5000 optimalchips/flask-cicd-pipeline:latest"

CI_CD_Pipeline:
  - "Uses GitHub Actions for continuous integration and deployment."
  - "Pipeline steps include: code checkout, Python setup, dependency installation, running tests, building the Docker image, logging into Docker Hub, and pushing the image."

Contributing:
  - "Fork the repository and create a pull request with your changes."

License:
  - "This project is licensed under the MIT License."

Contact:
  - "For questions or feedback, please contact [OptimalChips] or visit the GitHub repository: https://github.com/OptimalChips/flask-cicd-pipeline"
