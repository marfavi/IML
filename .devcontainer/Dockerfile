FROM continuumio/miniconda3

COPY iml_env.yml /usr/share/iml_env.yml

SHELL ["/bin/bash", "--login" , "-c"]
RUN useradd -ms /bin/bash programmer

# create conda environment
RUN conda init bash \
    && . ~/.bashrc \
    && conda env create -f /usr/share/iml_env.yml \
    && conda activate iml

WORKDIR /workdir
USER programmer
ENTRYPOINT ["/bin/bash"]
