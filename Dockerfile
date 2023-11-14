FROM python:3.8

WORKDIR /app

RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY api .
COPY forms_db.json .

EXPOSE 8080

CMD ["python", "app.py"]