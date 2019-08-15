## Writing Kubernetes Controllers in Python.




```
docker build -t submod/controller_dev -f Dockerfile .
docker push submod/controller_dev


docker run -it -v $HOME/.kube/config:/opt/app-root/src/.kube/config:z submod/controller_dev /bin/bash
oc login https://10.16.208.3:8443
```


```
oc project devconf
oc create -f pod.json
```

Create controller dev environment in a pod. 
```
oc create -f template.yml
oc new-app my-controller-dev
```

Delete everything. 
```
oc delete pod example
oc delete all -l template=my-controller-dev
oc delete template my-controller-dev
oc delete configmaps my-controller-dev
oc delete sa my-controller-dev
oc delete rolebinding.authorization.openshift.io my-controller-dev_edit
```

```
python3.6
oc login
```