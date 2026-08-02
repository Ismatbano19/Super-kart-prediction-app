
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the application port
EXPOSE 7860

# Start the Flask application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_sales_api"]
