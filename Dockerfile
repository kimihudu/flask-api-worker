FROM python:3.7
ADD . /
WORKDIR /
RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]