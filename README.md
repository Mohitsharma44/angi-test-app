# angi-test-app
Sample web application for Angi Test

[![Deploy to ECR](https://github.com/Mohitsharma44/angi-test-app/actions/workflows/build_and_push.yaml/badge.svg?branch=main)](https://github.com/Mohitsharma44/angi-test-app/actions/workflows/build_and_push.yaml)

This web app has 2 endpoints:
- `/healthz`: for healthchecks
- `/`: for getting version info

## Running locally
```
uvicorn main:app --reload
```

## Running as docker image
```
docker build -t mohitsharma44/angi-test-app .
docker run -p 8000:80 mohitsharma44/angi-test-app
```
