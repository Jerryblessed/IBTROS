# Base image
FROM python:3.10 AS base

# Set working directory
WORKDIR /usr/src/ibtros

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV CONFIG_PATH="/etc/ibtros/config.toml"
ENV DB_ENGINE="sqlite:////var/lib/ibtros/database.sqlite"

# Start the Flask application
ENTRYPOINT ["python", "-OO"]
CMD ["app.py"]
