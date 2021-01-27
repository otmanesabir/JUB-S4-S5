FROM gcr.io/deepnote-200602/templates/deepnote
RUN sudo apt-get update
RUN sudo mkdir -p /usr/share/man/man1
RUN sudo apt-get install -y openjdk-11-jdk-headless
RUN sudo apt-get install openssh-server openssh-client -y
RUN wget https://ftp.fau.de/apache/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
RUN tar xvzf hadoop-3.2.1.tar.gz
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV HADOOP_HOME=/home/jovyan/hadoop-3.2.1
RUN echo "export PATH=$PATH:$HADOOP_HOME/bin" >> $HOME/.bashrc
RUN pip install mrjob