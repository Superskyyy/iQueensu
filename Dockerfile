# Dockerfile

# Pull base Python image
FROM python:3.7

# Set environment variables
# Send output to terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory

RUN mkdir /iqueensu_backend
WORKDIR /iqueensu_backend

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /iqueensu_backend/
RUN pipenv install --system

# Copy project
COPY . /iqueensu_backend/