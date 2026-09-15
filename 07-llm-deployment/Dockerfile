# Build this from the REPO ROOT, not from inside 07-llm-deployment/, so it can
# see the 05-rag module and requirements.txt:
#   docker build -f 07-llm-deployment/Dockerfile -t genai-rag-service .
#   docker run -p 8000:8000 --env-file .env genai-rag-service

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "07-llm-deployment.deploy_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
