FROM gcr.io/deepnote-200602/templates/deepnote

# get Java
RUN sudo apt-get update && \
    sudo mkdir -p /usr/share/man/man1 && \
    sudo apt-get install -y openjdk-11-jdk-headless

# install hadoop
RUN wget https://ftp.fau.de/apache/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz && \
    tar xvzf hadoop-3.3.0.tar.gz && \
    rm hadoop-3.3.0.tar.gz

# set paths
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV HADOOP_HOME=/home/jovyan/hadoop-3.3.0
RUN echo "export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin" >> $HOME/.bashrc

# get mrjob
RUN pip install mrjob

# set config for hadoop
RUN echo "<configuration><property><name>fs.defaultFS</name><value>hdfs://localhost:9000</value></property></configuration>" > $HADOOP_HOME/etc/hadoop/core-site.xml && \
    echo "<configuration><property><name>dfs.replication</name><value>1</value></property><property><name>dfs.namenode.name.dir</name><value>/home/jovyan/hadoop-3.3.0/namenode</value></property><property><name>dfs.datanode.data.dir</name><value>/home/jovyan/hadoop-3.3.0/datanode</value></property></configuration>" > $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \
    echo "<configuration><property><name>mapreduce.framework.name</name><value>yarn</value></property><property><name>mapreduce.application.classpath</name><value>$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*</value></property></configuration>" > $HADOOP_HOME/etc/hadoop/mapred-site.xml && \
    echo "<configuration><property><name>yarn.nodemanager.aux-services</name><value>mapreduce_shuffle</value></property><property><name>yarn.nodemanager.env-whitelist</name><value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value></property></configuration>" > $HADOOP_HOME/etc/hadoop/yarn-site.xml

# magic line to get rid of ssh
RUN sed -i 's+ssh ${HADOOP_SSH_OPTS} ${worker} \$"\${@// /\\\\ }"+command=$"${@// /\\\\ }" ; ${command#"-- "}+g' $HADOOP_HOME/libexec/hadoop-functions.sh

# make directories for namenode and datanode data
RUN mkdir $HADOOP_HOME/datanode && mkdir $HADOOP_HOME/namenode

# formatting HDFS file system
RUN $HADOOP_HOME/bin/hdfs namenode -format

# initializing home directory on HDFS file system
# done in script to get around "connection refused" issue
RUN echo "$HADOOP_HOME/sbin/start-dfs.sh" > init_home.sh && \
    echo "$HADOOP_HOME/bin/hdfs dfs -mkdir /user" >> init_home.sh && \
    echo "$HADOOP_HOME/bin/hdfs dfs -mkdir /user/jovyan" >> init_home.sh && \
    echo "$HADOOP_HOME/sbin/stop-dfs.sh" >> init_home.sh && \
    sh init_home.sh

# installing libhdfs3
RUN sudo apt install -y libxml2-dev libprotobuf-dev libkrb5-dev libgsasl7-dev libgmock-dev openssl libssl-dev libcurl4-openssl-dev protobuf-compiler libboost-dev && \
    git clone https://github.com/ContinuumIO/libhdfs3-downstream.git && \
    cd libhdfs3-downstream/libhdfs3 && mkdir build && cd build && ../bootstrap && make && make install && cd ../dist/lib/ && sudo cp -R * /usr/lib && cd

# installing hdfs3 Python module
RUN pip install hdfs3

# installing Pig
RUN cd /home/jovyan && \
    wget http://ftp.halifax.rwth-aachen.de/apache/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar xvzf pig-0.17.0.tar.gz && \
    rm pig-0.17.0.tar.gz
ENV PIG_HOME=/home/jovyan/pig-0.17.0
RUN echo "export PATH=$PATH:$PIG_HOME/bin" >> $HOME/.bashrc


# installing Spark
RUN wget https://ftp.fau.de/apache/spark/spark-3.0.1/spark-3.0.1-bin-without-hadoop.tgz && \
    tar xvzf spark-3.0.1-bin-without-hadoop.tgz && \
    rm spark-3.0.1-bin-without-hadoop.tgz
ENV SPARK_HOME=/home/jovyan/spark-3.0.1-bin-without-hadoop
ENV SPARK_DIST_CLASSPATH=/home/jovyan/hadoop-3.3.0/etc/hadoop:/home/jovyan/hadoop-3.3.0/share/hadoop/common/lib/*:/home/jovyan/hadoop-3.3.0/share/hadoop/common/*:/home/jovyan/hadoop-3.3.0/share/hadoop/hdfs:/home/jovyan/hadoop-3.3.0/share/hadoop/hdfs/lib/*:/home/jovyan/hadoop-3.3.0/share/hadoop/hdfs/*:/home/jovyan/hadoop-3.3.0/share/hadoop/mapreduce/*:/home/jovyan/hadoop-3.3.0/share/hadoop/yarn:/home/jovyan/hadoop-3.3.0/share/hadoop/yarn/lib/*:/home/jovyan/hadoop-3.3.0/share/hadoop/yarn/*
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PYSPARK_PYTHON=/opt/venv/bin/python
RUN echo "export PATH=$PATH:$SPARK_HOME/bin" >> $HOME/.bashrc
