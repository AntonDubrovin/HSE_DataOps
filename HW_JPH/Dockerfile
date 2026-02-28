FROM python:3.14-slim

RUN apt-get update && apt-get install -y nodejs npm && \
    npm install -g configurable-http-proxy && \
    pip install jupyterhub jupyterlab && \
    apt-get clean

EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
