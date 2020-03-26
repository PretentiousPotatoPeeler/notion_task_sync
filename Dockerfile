FROM python:3-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt && flake8 .
CMD ["python", "notion_task_sync.py", "./notion_task_sync.conf"]