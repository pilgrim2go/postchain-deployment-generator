FROM openjdk:11.0.5-jre
RUN apt-get install -y curl
RUN curl -sL https://www.chromia.dev/rellr/rellr-0.10.4-dist.tar.gz | tar xvz -C /opt
RUN chmod +x /opt/postchain-node/*

COPY ./rell/src /usr/src/rell/src
COPY config{{inode}}/ /usr/src/rell/config/
COPY run{{inode}}.sh /run.sh
RUN chmod +x /run.sh
WORKDIR /usr/src/rell
CMD /run.sh
