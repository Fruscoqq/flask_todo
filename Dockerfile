# Python base image.
FROM python:3.8
# Create and set the work directory inside the image named 'app'
WORKDIR /app
COPY . .
# Execute a pip install command using the list 'requirements.txt'
RUN pip install -r requirements.txt

EXPOSE 5000
# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"]