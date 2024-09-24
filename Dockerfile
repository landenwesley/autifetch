# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

WORKDIR /home/usr/

COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "./fetch.py"]
