FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN groupadd -r webservice && useradd --no-log-init -r -g webservice webservice
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

USER webservice:webservice
EXPOSE 8050

CMD ["python", "app.py"]