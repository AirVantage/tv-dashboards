FROM bitnami/minideb:jessie
MAINTAINER prieux@sierrawireless.com


# Install
RUN \
    install_packages wget python openssl ca-certificates && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python ./get-pip.py && \
    install_packages python-pip && \
    pip install python-dateutil pytz jira jinja2 tornado Flask requests && \
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
