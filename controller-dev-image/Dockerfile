FROM registry.fedoraproject.org/f30/s2i-base
LABEL MAINTAINER="Subin Modeel smodeel@redhat.com"

COPY ./loop.sh /opt/app-root/

RUN dnf -y install git vim tree net-tools python36 python3-devel python3-setuptools python3-pip python3-virtualenv \
    && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python3.6 get-pip.py \
    && dnf -y install python-pip && dnf clean all && rm -rf /var/cache/dnf \
    && wget https://github.com/openshift/origin/releases/download/v3.11.0/openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz \
    && tar -xvf openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz \
    && cp openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit/oc /usr/local/bin/ \
    && cp openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit/kubectl /usr/local/bin/
RUN pip3.6 install --upgrade setuptools && pip3.6 install kubernetes~=9.0.0 openshift



