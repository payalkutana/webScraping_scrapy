FROM python:3

ENV MONGO_INITDB_ROOT_USERNAME=root \
    MONGO_INITDB_ROOT_PASSWORD=password

#RUN mkdir -p /home/app

WORKDIR /usr/src/app

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
COPY . /usr/src/app

# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","./go-spider.py"]