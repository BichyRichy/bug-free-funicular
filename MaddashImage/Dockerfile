FROM opensciencegrid/software-base:fresh

RUN yum -y install httpd; yum clean all; systemctl enable httpd.service
EXPOSE 80

RUN yum -y install epel-release; yum -y install http://software.internet2.edu/rpms/el7/x86_64/latest/packages/perfSONAR-repo-0.9-1.noarch.rpm; yum -y clean all
RUN yum -y install perfsonar-centralmanagement; yum -y install perfsonar-toolkit; yum -y install supervisor; yum clean all;
RUN mkdir -p /var/run/sshd /var/log/supervisor

ADD maddash.yaml /etc/maddash/maddash-server/
## ADD su /etc/pam.d/
ADD esmondAPI /home/esmondAPI
ADD psconfig.json /home
ADD supervisord.conf /etc/supervisord.d/10-maddash-server.conf

CMD ["/usr/sbin/init"]