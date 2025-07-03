# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python application
COPY app.py .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_NAME="Simple Python App"
ENV ENVIRONMENT="production"

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Run the application
CMD ["python", "app.py"]
