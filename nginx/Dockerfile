FROM nginx:latest

RUN mkdir /etc/nginx/static/
RUN mkdir /etc/nginx/media/
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80 8000 768