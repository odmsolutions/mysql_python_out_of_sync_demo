FROM library/mysql:latest
RUN apt-get -y update && apt-get install -qq -y \
    python-pip
RUN apt-get install -qq -y python-mysqldb
VOLUME /test/

