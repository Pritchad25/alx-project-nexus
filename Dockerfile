# Use a modern base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (if needed for your packages)
RUN apt update && apt install -y build-essential libpq-dev

# Copy your requirements file into the container
COPY requirements.txt .

# Install Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Copy your actual project code
COPY . .

# Runserver default (can be overridden in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

