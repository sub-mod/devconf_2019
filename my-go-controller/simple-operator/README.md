

```
GO111MODULE=on
operator-sdk new simple-operator --repo github.com/sub-mod/simple-operator
cd simple-operator
operator-sdk add controller --kind=Pod --api-version=core/v1
```

```
operator-sdk build docker.io/submod/simple-operator
docker push docker.io/submod/simple-operator


oc create -f deploy/service_account.yaml
oc create -f deploy/role.yaml
oc create -f deploy/role_binding.yaml
oc create -f deploy/operator.yaml



oc delete -f deploy/operator.yaml
oc delete -f deploy/role.yaml
oc delete -f deploy/role_binding.yaml
oc delete -f deploy/service_account.yaml
 
 
oc login https://sde-ci-works06.3a2m.lab.eng.bos.redhat.com:8443/
oc project devconf

oc create -f pod.json
oc delete pod example
```