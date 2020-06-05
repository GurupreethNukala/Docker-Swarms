FROM ubuntu:16.04

WORKDIR /usr/local/apache2

# Create custom log directory
RUN mkdir -p /tmp/log/apache2

# Installing apache2 package
RUN apt-get update -y \
    && apt-get install apache2 -y

ADD envvars /etc/apache2/envvars

VOLUME /var/www /tmp/log/apache2 /etc/apache2

EXPOSE 80 443

CMD ["/usr/sbin/apachectl","-D","FOREGROUND"]
