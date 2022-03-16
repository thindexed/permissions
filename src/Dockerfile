FROM nginx:1.21.6

EXPOSE 80

COPY ./web/ /usr/share/nginx/html


CMD ["nginx-debug", '-g', 'daemon off;']