FROM fedora
ENV MBSE_ROOT=/opt/mbse

RUN dnf -y install \
	findutils \
	gcc \
	git \
	iproute \
	make \
	ncurses-devel \
	procps-ng \
	unzip \
	vim \
	zip \
	zlib-devel

RUN mkdir -p /src
WORKDIR /src
RUN git clone https://git.code.sf.net/p/mbsebbs/code mbsebbs-code
WORKDIR /src/mbsebbs-code
RUN make clean; ./configure
RUN make
RUN rm -f checkbasic; ln -s /bin/true checkbasic
RUN groupadd -r bbs
RUN useradd -c "MBSE BBS Admin" -d /opt/mbse -g bbs mbse
RUN useradd -c "MBSE BBS Login" -d /opt/mbse/home/bbs -g bbs -s /opt/mbse/bin/mbnewusr bbs
RUN make install

RUN dnf -y install \
	mgetty \
	net-tools \
	telnet-server
