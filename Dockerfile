# Main app
FROM python:3.13.13-bookworm as python_app

WORKDIR /application/src

COPY ./requirements.txt /application/src

RUN pip install --no-cache-dir --upgrade  -r requirements.txt

COPY ./src ./application/src

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
