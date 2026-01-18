FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY picture_download/ ./picture_download/

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "picture_download.main:app", "--host", "0.0.0.0", "--port", "8000"]
