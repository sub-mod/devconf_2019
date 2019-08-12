FROM centos/python-36-centos7
LABEL MAINTAINER="Subin Modeel smodeel@redhat.com"
USER root

ENV PATH=/opt/app-root/bin:/opt/rh/rh-python36/root/usr/bin:/opt/app-root/src/.local/bin/:/opt/app-root/src/bin:/opt/app-root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LD_LIBRARY_PATH=/opt/rh/rh-python36/root/usr/lib64

RUN yum -y install libffi-devel; \
  pip install --upgrade pip; \
  pip install requests pkiutils pyopenssl; \
  yum clean all;
RUN pip install kubernetes~=9.0.0 openshift
RUN mkdir -p /opt/my-controller
COPY ./src/ /opt/my-controller/
COPY ./bin/ /opt/my-controller/bin
RUN chown -R 1001:1001 /opt/my-controller
USER 1001
#ENTRYPOINT ["/opt/my-controller/bin/start.sh"]
