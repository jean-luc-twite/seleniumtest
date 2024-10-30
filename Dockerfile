# Use the official Python image as a base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    unzip \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Download ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    curl -sS -o /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Copy your test files into the container
COPY . .

# Set the display port to avoid errors
ENV DISPLAY=:99

# Start Xvfb (X virtual framebuffer) to run Chrome in the background
RUN apt-get update && apt-get install -y xvfb

# Command to run your tests
CMD ["xvfb-run", "-a", "python", "-m", "unittest", "your_test_file.py"]
