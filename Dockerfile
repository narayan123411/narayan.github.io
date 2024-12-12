FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Rasa API will run on
EXPOSE 5005

# Make the start.sh script executable
RUN chmod +x start.sh

# Set the entry point to run both commands (Rasa and your app)
CMD ["./start.sh"]
