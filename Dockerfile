FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PATH=/opt/conda/bin:$PATH

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    mercurial \
    subversion \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN conda create -n lamini python=3.10 && \
    echo "conda activate lamini" >> ~/.bashrc

COPY requirements.txt /tmp/requirements.txt
RUN /bin/bash -c "source ~/.bashrc && conda activate lamini && pip install -r /tmp/requirements.txt"

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["/bin/bash", "-c", "source ~/.bashrc && conda activate lamini && uvicorn --host 0.0.0.0 main:app"]
