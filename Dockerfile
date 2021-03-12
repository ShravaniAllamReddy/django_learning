FROM python:3
WORKDIR /usr/src/app
COPY . .
# this changes with respect to file name you want to run
CMD ["functions_example.py"] 
ENTRYPOINT ["python3"]