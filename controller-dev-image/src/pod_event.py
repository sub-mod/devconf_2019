from kubernetes import client, config, watch
from kubernetes.client import ApiClient, Configuration
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
v1_pod = dyn_client.resources.get(api_version='v1', kind='Pod')
for event in v1_pod.watch(namespace=NAMESPACE):
    #print(event['object'])
    print("Event: %s %s %s" % (event['type'], event['object'].metadata.name, event['object'].metadata.resourceVersion))

