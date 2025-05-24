FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install ADB (for Android automation)
RUN apt-get update && \
    apt-get install -y android-tools-adb && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose default Appium port (if needed)
EXPOSE 4723

# Default command
CMD ["python", "main.py"]
