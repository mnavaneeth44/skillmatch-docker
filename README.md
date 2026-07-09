# Skill Match — Dockerized Flask App

## What this is
A Dockerized Flask web application showcasing the Skill Match project —
a Resume Matcher and Skill Recommender built with Python & Flask.
This repo demonstrates how to package a Python web app into a Docker
container so it runs the same anywhere.

## Tech used
- Python 3.11
- Flask
- Docker & Dockerfile
- python:3.11-slim base image

## Project structure
skillmatch-docker/
├── app.py              # Flask web application
├── Dockerfile          # Container build instructions
├── .dockerignore       # Files excluded from the image
├── requirements.txt    # Python dependencies
└── README.md
## How to run

### 1. Build the image
```bash
docker build -t skillmatch:v1 .
```

### 2. Run the container
```bash
docker run -d -p 5000:5000 --name skillmatch-app skillmatch:v1
```

### 3. Open in browser
http://localhost:5000

### 4. Stop the container
```bash
docker stop skillmatch-app
```

## What I learned
- How to write a Dockerfile from scratch
- Why a small base image (python:3.11-slim) matters for performance
- How port mapping works between a container and the host machine
- How .dockerignore keeps the image clean and lightweight
- The difference between building an image and running a container

## Screenshots
- `docker-build-run.png` — terminal showing build + docker ps output
- `app-browser.png` — app running at localhost:5000 in browser
- 
