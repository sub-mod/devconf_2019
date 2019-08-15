## Writing Kubernetes Controllers in Python.

## controller in a pod

build the controller image. 
```
docker build -t submod/my-controller -f Dockerfile .
docker push submod/my-controller:latest
```

To test the controller locally. 
```
docker pull submod/my-controller:latest
docker run -it -u 0 -v $HOME/.kube/config:/opt/app-root/src/.kube/config:z submod/my-controller:latest /bin/bash
(app-root) python3.6 /opt/my-controller/pod_watch.py
(app-root) python3.6 /opt/my-controller/all_pods.py
```

Create controller in a pod. 
```
oc cluster up
oc login -u abc -p abc123
oc new-project devconf

oc create -f template.yml
oc new-app my-controller --param=FILE_NAME=pod_watch.py

oc create 
oc new-app my-controller --param=FILE_NAME=crd_watch.py
oc new-app my-controller --param=FILE_NAME=all_pods.py
```

Test pod creation. 
```
oc project devconf
oc create -f pod.json
oc delete pod example
```

Delete everything. 
```
oc delete pod example
oc delete all -l template=my-controller
oc delete template my-controller
oc delete configmaps my-controller
oc delete sa my-controller
oc delete rolebinding.authorization.openshift.io my-controller_edit
```