FROM python:3.10

COPY . /bewise
WORKDIR /bewise
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]