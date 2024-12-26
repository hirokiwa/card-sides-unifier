# Use an official Python runtime
FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy over your code and pdf folder
COPY . /app/

# Default command to run your script
CMD ["python", "index.py"]
