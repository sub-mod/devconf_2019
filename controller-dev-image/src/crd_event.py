import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


NAMESPACE='devconf'
#Outside a Pod
k8s_client = config.new_client_from_config()

#Inside a Pod
config.load_incluster_config()
k8s_client = ApiClient(configuration=client.Configuration())

dyn_client = DynamicClient(k8s_client)
custom_resources = dyn_client.resources.get(
  api_version='apiextensions.k8s.io/v1beta1',
  kind='CustomResourceDefinition'
)
foos = dyn_client.resources.get(api_version='bar.com/v1beta1', kind='Foo')
for event in foos.watch(namespace=NAMESPACE):
    print("Event: %s %s %s" % (event['type'], event['object'].metadata.name, event['object'].metadata.resourceVersion))

