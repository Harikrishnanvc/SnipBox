# Use Python 3.9
FROM python:3.9

WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip setuptools wheel

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

