FROM continuumio/miniconda3

COPY iml_env.yml /usr/share/iml_env.yml

SHELL ["/bin/bash", "--login" , "-c"]
RUN useradd -ms /bin/bash programmer
RUN conda env create -f /usr/share/iml_env.yml
RUN conda init

WORKDIR /workdir
USER programmer
ENTRYPOINT ["/bin/bash"]
