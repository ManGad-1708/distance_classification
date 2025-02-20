# Use the official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Default command: Run the main script
CMD ["python", "distance_classification.py"]
