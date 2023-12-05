# Use the base Python image
FROM python:3.9

# Update and install additional OS packages if needed
RUN apt-get update && apt-get -y install --no-install-recommends \
   gcc

# Create a non-root user (optional but recommended)
ARG USER="ashley"
RUN useradd -m -s /bin/bash ${USER}

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY requirements.txt Makefile ./
COPY ./hugohu_project_4 /app/hugohu_project_4

# Create a virtual environment and install dependencies
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

RUN chown -R ${USER}:${USER} /app

# Switch to the non-root user (optional but recommended)
USER ${USER}

# Specify the command to run your application
CMD ["python", "-m", "hugohu_project_4"]