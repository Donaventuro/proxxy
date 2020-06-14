FROM python:3.6-alpine

RUN adduser -D microuser

WORKDIR /home/microuser

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY myserver.py myserver.py

RUN chmod +x myserver.py

ENV PROXXY_APP myserver.py

RUN chown -R microuser:microuser ./
USER microuser

EXPOSE 9000

ENTRYPOINT ["python", "myserver.py", "--host"]