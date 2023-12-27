FROM python:3.8.5
WORKDIR /sites_ativos
COPY . .
EXPOSE 8000
CMD [ "bash", "-c", "sudo", "apt", "install", "python3", "&&", "python3", "-m", "venv", ".venv", "&&", "source", "--", ".venv/bin/activate" ]
RUN pip install requests
RUN pip install pandas
RUN pip install beautifulsoup4
RUN pip install mysql-connector-python
COPY . .
ENTRYPOINT [ "python3", "src/app.py" ]