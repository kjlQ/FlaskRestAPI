FROM python:3.11.3
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--reload"]
