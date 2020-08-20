FROM nginxinc/nginx-unprivileged:alpine



COPY ./index.html /usr/share/nginx/html/index.html
COPY ./nginx.conf /etc/nginx/nginx.conf



