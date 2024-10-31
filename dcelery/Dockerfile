FROM python:3.11.4-alpine

WORKDIR /usr/src/app


# prevent python from from writning .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensure python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# an entering point file(files which will be run everytime we run the container eg collectstatic, migrate )
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh


COPY . /usr/src/app/


ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]