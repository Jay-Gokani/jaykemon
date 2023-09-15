FROM python:3.10.5

RUN apt-get update && apt-get install -y \
  python3-pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

# docker build -t <image_name> .
# docker run -it <image_name>
# docker login -u <username>
# docker tag <image_name> <username>/<repo>:[tag]
# docker push <username>/<repo>:[tag]