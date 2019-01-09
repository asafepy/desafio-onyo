FROM node:alpine

LABEL maintainer="open-source@6go.it" \
      vendor="6go.it" \
      version=1.1.1

ENV WEBAPP_DIR=/funcionarios
ENV USER node

WORKDIR ${WEBAPP_DIR}

EXPOSE 9000

USER ${USER}

WORKDIR app

CMD ["tail", "-f", "/dev/null"]