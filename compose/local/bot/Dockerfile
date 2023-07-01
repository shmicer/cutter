# Use a Python base image
FROM python:3.11-alpine

# Install bot dependencies
RUN pip install --upgrade pip
COPY requirements/local/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Set the working directory
WORKDIR /app/bot

# Run the bot script
CMD ["python", "bot.py"]
