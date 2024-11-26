# Use a minimal base image with Python 3.11
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary scripts and templates
COPY generate_readme.py .
COPY generate_file_templates.py .
COPY puzzle_scraper.py .
COPY challenges.json .
COPY README.template .
COPY docker_entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x docker_entrypoint.sh

# Create necessary directories
RUN mkdir -p output data solutions

# The folder where the generated README.md will be persisted
VOLUME ["/app/output"]

# Remove README files during build
RUN rm -f README.md
RUN rm -f /app/output/README.md

# Automatically exit the container after execution
ENTRYPOINT ["./docker_entrypoint.sh"]