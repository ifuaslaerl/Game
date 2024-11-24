# Imagem base com Ubuntu
FROM ubuntu:22.04

# Atualizar pacotes e instalar dependências básicas
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    && apt-get clean

# Instalar Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/miniconda && \
    rm /miniconda.sh

# Configurar PATH para usar conda diretamente
ENV PATH="/opt/miniconda/bin:$PATH"

# Copiar script de personalização (setup.sh)
COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

# Executar o script de personalização
RUN /setup.sh

# Diretório de trabalho padrão
WORKDIR /workspace

# Comando padrão
CMD ["/bin/bash"]
