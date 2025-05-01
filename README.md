Step 1: Python Script - CSV Analyzer
The first step was to write a simple Python script that processes a CSV file and outputs some basic statistics. This was achieved by using the Pandas library.

Step 2: Create a requirements.txt File
To ensure that the necessary dependencies are installed when building the Docker image, I created a requirements.txt file with the following contents:

Step 3: Writing the Dockerfile
The Dockerfile defines the instructions for building the Docker image. Below is the Dockerfile that sets up the Python environment, installs dependencies, copies the script into the image, and runs it.
# Use official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements.txt into the container
COPY csv_analyzer.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script
CMD ["python", "csv_analyzer.py"]

Step 4: Building the Docker Image
docker build -t csv-analyzer .

Step 5: Running the Docker Container
docker run -v /path/to/csv/files:/app csv-analyzer
