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