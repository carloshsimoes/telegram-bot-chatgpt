FROM ubuntu

ADD . /app
WORKDIR /app

RUN apt update \
 && apt upgrade -y \
 && apt install python3 pip python3.10-venv -y \
 && chmod +x /app/runAPP.sh

ENTRYPOINT [ "sh", "/app/runAPP.sh" ]
