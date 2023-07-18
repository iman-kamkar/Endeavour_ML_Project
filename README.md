# ML Engineering Project
## Overview
This project is a web application built using the Flask framework, that serves a machine learning model for making predictions based on user input. The application is designed to be run inside a Docker container to ensure a consistent environment and easy deployment. The code and all its dependencies have been Dockerized and pushed to Dockerhub for easy access and distribution.

The application has two key endpoints:
- `/` : The home page of the web application.
- `/predictdata` : The endpoint for making predictions using the machine learning model.

## Getting Started

1. **Pull the Docker Image**

    To get started with the application, the first step is to pull the Docker image from Dockerhub. Use the command below:
    
    ```bash
    docker pull iman2546/ml-proj:latest
    ```

2. **Run the Docker Image**

    After pulling the Docker image, you can run it using the command below:
    
    ```bash
    docker run -p 5000:5000 iman2546/ml-proj
    ```

    This command runs the Docker image and maps the container's port 5000 to your machine's port 5000. This allows you to access the web application by visiting `http://localhost:5000` on your web browser.

## Project Structure

- **Flask App (`app.py`):** This file contains the Flask web application.
    - `@app.route('/')`: This is the home page of the application. It renders the 'index.html' template.
    - `@app.route('/predictdata',methods=['GET','POST'])`: This is the endpoint for making predictions with the model. If a GET request is made, it simply returns the 'home.html' template. If a POST request is made, it uses the `PredictPipeline` to make a prediction based on the user's input.

- **Predict Pipeline (`src/pipeline/predict_pipeline.py`):** This file contains the `PredictPipeline` class which is used to make predictions with the model.

- **Templates:** The HTML templates for the application are located in the 'templates' directory. These templates are used to generate the web pages of the application.

## Usage

Visit `http://localhost:5000` on your web browser to view the application. The home page simply presents the application.

To make a prediction, navigate to `http://localhost:5000/predictdata`. If you are making a GET request, it will present a form for you to input your data. If you are making a POST request (i.e., submitting the form), it will take the input, use it to make a prediction with the model, and then display the result on the 'home.html' template.

