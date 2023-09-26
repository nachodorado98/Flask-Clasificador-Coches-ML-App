FROM python:3.10-buster

# Solventa error de tensorflow (ademas se debe eliminar el paquete de intel)
RUN echo \
   && apt-get update \
   && apt-get --yes install apt-file \
   && apt-file update
RUN echo \
   && apt-get --yes install build-essential
ARG USER=nobody
RUN usermod -aG sudo $USER

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "run:app","run", "--host=0.0.0.0", "--reload"]
