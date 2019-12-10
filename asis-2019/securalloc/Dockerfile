FROM ubuntu:16.04

WORKDIR /securalloc

# install ncat
RUN apt update && apt -y install nmap \
    && rm -rf /var/lib/apt/lists/*

# copy files
COPY libc.so.6 ./
COPY libsalloc.so ./
COPY securalloc.elf ./

WORKDIR /lib/x86_64-linux-gnu
RUN ln -s /securalloc/libsalloc.so libsalloc.so

WORKDIR /securalloc

# RUN echo "#!/bin/bash\n\
# LD_LIBRARY_PATH=/securalloc/ ./securalloc.elf" >> securalloc.sh
RUN echo "#!/bin/bash\n\
exec 2>&1 \n\
./securalloc.elf" > securalloc.sh

RUN echo "ASIS{l3ft0v3r_ru1n3d_3v3ryth1ng}" > flag

RUN chmod u+x securalloc.sh

EXPOSE 9876/tcp

CMD ["ncat", "-l", "-p", "9876", "-k", "-e", "securalloc.sh"]
