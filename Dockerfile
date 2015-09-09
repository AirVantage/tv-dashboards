FROM debian:latest
MAINTAINER prieux@sierrawireless.com

# Install
RUN \
    apt-get update && \
    apt-get install -y python-pip wget git vim unzip python-dev openssl ca-certificates && \
    pip install --upgrade ipython python-dateutil pytz jira-python jinja2 tornado Flask requests && \
    cd /usr/local/share/ca-certificates/ && wget http://ca.anyware-tech.com/anyware-tech.crt && \
    update-ca-certificates && \
    useradd engtv -U -s /bin/false && \
    mkdir -p /home/engtv/static/ && \
    mkdir -p /home/engtv/www
#

COPY static  /home/engtv/static
COPY www     /home/engtv/www

ADD scripts/engtv.sh /home/engtv/
ADD scripts/engtv.py /home/engtv/

USER engtv

EXPOSE 8080

ENTRYPOINT ["/home/engtv/engtv.sh"]
