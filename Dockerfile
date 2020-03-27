FROM python:3-slim
WORKDIR /app
COPY requirements.txt notion_task_sync.py ./
COPY integrations/*.py ./integrations/
RUN pip install -r requirements.txt && flake8 .
CMD ["python", "notion_task_sync.py", "/app/notion_task_sync.conf"]