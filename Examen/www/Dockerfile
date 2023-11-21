FROM php:7.4-apache
COPY --chown=www-data:www-data . /var/www/html
EXPOSE 80
RUN a2enmod rewrite
