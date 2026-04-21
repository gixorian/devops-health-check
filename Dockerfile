FROM python:3.11-slim
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
WORKDIR /app
COPY health_check.py .
RUN chown -R appuser:appgroup /app
USER appuser
CMD ["python", "health_check.py"]
