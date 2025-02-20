# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Ensure Jupyter Notebook works inside Docker (if needed)
EXPOSE 8888

# Default command: Run Jupyter Notebook (if needed) or Python script
CMD ["python", "distance_classification.py"]
