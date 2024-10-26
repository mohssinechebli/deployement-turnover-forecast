FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Flask API
EXPOSE 8000

# Run the Flask application
CMD ["python", "main.py"]