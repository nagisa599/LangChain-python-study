# python version number:3.9.16
FROM python:3.9.16

# code ... directory for python codes.
ENV ROOT=/app/src/
WORKDIR ${ROOT}

# copy localcode to container image.
COPY . .

EXPOSE 3002

# upgrade pip command
RUN pip install --upgrade pip 

# install python lib 
RUN pip install -r requirements.txt

# Command to run main.py every time the container starts
CMD ["python", "main.py"]