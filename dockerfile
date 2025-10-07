# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt if you have dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script(s) into the container
COPY . .

# Set the default command to run your script (replace main.py with your script name)
CMD ["python", "main.py"]