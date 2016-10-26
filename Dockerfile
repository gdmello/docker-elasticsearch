FROM elasticsearch:1.7.5

MAINTAINER gdmello

ADD plugins/ /tmp/plugins/

#Install marvel for a nice dashboard.
RUN cd /usr/share/elasticsearch && bin/plugin --install elasticsearch/marvel/latest

#Install python
RUN apt-get update && \
    apt-get install -y python python-dev

CMD ["/entrypoint.sh"]