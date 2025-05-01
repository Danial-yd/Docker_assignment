# Docker Assignment: CSV Analyzer

## Objective

This project involves creating a Python data processing script that analyzes CSV files and outputs summary statistics. The Python script is packaged into a Docker container, making it easy to run anywhere. 

### Steps involved:
1. **Write a Python script** to analyze CSV data.
2. **Create a Dockerfile** to build a Docker image.
3. **Build the Docker image** and run the container.
4. **Push the image to Docker Hub**.

---

## Step 1: Python Script - CSV Analyzer

The first step is writing a Python script that processes a CSV file and outputs some basic statistics. This was done using the **Pandas** library.

## Step 2: Create a `requirements.txt` File

To ensure that the necessary dependencies are installed when building the Docker image, a `requirements.txt` file was created. This file lists the required Python packages that the script depends on.

### `requirements.txt`


This file specifies that the **Pandas** library version `1.5.3` is required for the Python script to run.

---

## Step 3: Writing the Dockerfile

The Dockerfile defines the instructions for building the Docker image. It sets up the Python environment, installs dependencies, copies the Python script and the `requirements.txt` file into the image, and specifies the command to run the Python script.

### Dockerfile

```Dockerfile
# Use official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements.txt into the container
COPY code.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script
CMD ["python", "code.py"]

---

## Step 4: Building the Docker Image

After creating the Dockerfile, the next step is to build the Docker image. This process will read the instructions in the Dockerfile and create an image that includes all the dependencies and the Python script.

### Build Command

To build the Docker image, run the following command in your terminal:

```bash
docker build -t csv-analyzer .


### Build Command
docker build -t csv-analyzer .

## Step 5:
docker run -v /path/to/csv/files:/app csv-analyzer


