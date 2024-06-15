# Use official Node.js image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app
COPY . .

# Copy package.json and app.js to container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]