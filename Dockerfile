FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "-c", "print('SE1EndtermExamSpring2026 - Student 40231035 Docker image created successfully')"]