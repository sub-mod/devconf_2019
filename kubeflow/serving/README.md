## Deploying the model in the Notebook

```
kustomize edit add configmap inference-configmap --from-literal=name=tf-test
kustomize edit add configmap inference-configmap --from-literal=pvcName=test
kustomize edit add configmap inference-configmap --from-literal=pvcMountPath=/home/jovyan
kustomize edit add configmap inference-configmap --from-literal=modelBasePath=/home/jovyan
kustomize edit add configmap inference-configmap --from-literal=modelName=default
kustomize edit add configmap inference-configmap --from-literal=servingImage=tensorflow/serving:1.11.1


kustomize build . |kubectl apply -f -
```



### Set a different name for the tf-serving.
```
kustomize edit add configmap inference-configmap --from-literal=name=tf-test
```
### Set a different name for the tf-serving.
```
Mount the PVC, by default the pvc will be mounted to the /home/jovyan of the Notebook pod.
kustomize edit add configmap inference-configmap --from-literal=pvcName=test
kustomize edit add configmap inference-configmap --from-literal=pvcMountPath=/home/jovyan
```

### Configure a filepath for the exported model and set the name of the model
```
kustomize edit add configmap inference-configmap --from-literal=modelBasePath=/home/jovyan
kustomize edit add configmap inference-configmap --from-literal=modelName=default
```
### Deploy it, and run a service to make the deployment accessible to other pods in the cluster.
```
kustomize build . |kubectl apply -f -
```

### You can check the deployment by running
```
kubectl describe deployments tf-test
```
### The service should make the tf-test deployment accessible over port 9000.
```
kubectl describe service tf-test
```

### debug commands
```
kustomize build .
oc get configmap inference-configmap -o yaml
```
### Delete everything
```
oc delete all -l appName=tf-test
oc delete all -l app=inference-configmap
oc delete configmap inference-configmap
```