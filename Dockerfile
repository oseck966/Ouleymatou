FROM python:3.7-alpine
WORKDIR /code
COPY * /code/
RUN pip install -r requirements.txt
EXPOSE 5551
CMD ["python", "./application.py"]