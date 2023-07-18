FROM python:3.10
COPY . /app
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Install Python packages
RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

CMD python app.py