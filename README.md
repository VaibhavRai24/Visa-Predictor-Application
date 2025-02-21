# Visa Prediction Application - MLOps Implementation

## Overview
The **Visa Prediction Application** is an AI-driven solution that predicts visa approval outcomes based on various applicant parameters. This project leverages **MLOps techniques and tools** to streamline the entire machine learning lifecycle, ensuring automation, reproducibility, and scalability.

## Features
- **Data Preprocessing:** Cleans and prepares data for training.
- **Feature Engineering:** Selects and transforms key features.
- **Model Training:** Utilizes machine learning models to predict visa outcomes.
- **Model Evaluation:** Measures model accuracy, precision, and recall.
- **CI/CD Pipeline:** Automates training, testing, and deployment using MLOps.
- **Cloud Deployment:** Deploys the model via AWS services.
- **Monitoring:** Tracks model performance and data drift over time.

## Tech Stack
- **Programming Language:** Python
- **Machine Learning Framework:** TensorFlow / Scikit-learn
- **MLOps Tools:**
  - **Modular Coding:** MLOps modular coding
  - **Version Control:** Git & GitHub
  - **Containerization:** Docker
  - **Cloud Services:** AWS (IAM User, ECR, EC2, S3)
  - **CI/CD:** GitHub Actions
  - **Model Deployment:** AWS Lambda / Flask API
  - **Monitoring:** Prometheus & Grafana
  - **Database:** MongoDB Atlas
  - **Frontend:** HTML & CSS
  - **Dataset Source:** Kaggle

## Project Structure
```
visa-prediction-app/
│── data/                 # Raw and processed data
│── notebooks/            # Jupyter notebooks for EDA & experiments
│── src/                  # Source code for model training & inference
│── models/               # Saved machine learning models
│── pipelines/            # MLOps pipelines for automation
│── configs/              # Configuration files
│── scripts/              # Utility scripts for automation
│── tests/                # Unit and integration tests
│── Dockerfile            # Docker container setup
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── .github/workflows/    # CI/CD pipeline configuration
```

## Setup & Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/visa-prediction-app.git
   cd visa-prediction-app
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the application locally:
   ```sh
   python src/app.py
   ```

## Model Training
To train the model, execute:
```sh
python src/train.py
```

## Deployment
### Docker Deployment
```sh
docker build -t visa-predictor .
docker run -p 5000:5000 visa-predictor
```

## CI/CD Pipeline
The CI/CD pipeline includes:
- Automated testing with GitHub Actions
- Model retraining on new data
- Deployment updates upon successful validation

## Monitoring & Maintenance
- Use **Prometheus** and **Grafana** to monitor performance.
- Set up alerts for model drift and API failures.

## Contributors
- **Your Name** - VAIBHAV RAI

## License
This project is licensed under the MIT License.

