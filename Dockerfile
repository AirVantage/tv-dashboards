FROM debian:latest
MAINTAINER prieux@sierrawireless.com

RUN apt-get update

RUN apt-get install -y python-pip wget git vim unzip python-dev openssl ca-certificates
RUN pip install --upgrade ipython python-dateutil pytz jira-python jinja2 tornado Flask

# anyware certificate
RUN cd /usr/local/share/ca-certificates/ && wget http://ca.anyware-tech.com/anyware-tech.crt
RUN update-ca-certificates

RUN useradd engtv -U -s /bin/false 

RUN mkdir -p /home/engtv/static/
RUN mkdir -p /home/engtv/www

COPY static  /home/engtv/static
COPY www     /home/engtv/www

ADD scripts/engtv.sh /home/engtv/
ADD scripts/engtv.py /home/engtv/

USER engtv

EXPOSE 8080

ENTRYPOINT ["/home/engtv/engtv.sh"]
