from kubernetes import client, config, watch
from kubernetes.client import ApiClient, Configuration
from openshift.dynamic import DynamicClient
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

NAMESPACE='devconf'
INSIDE_POD=False

def EventWatcher():
    if INSIDE_POD:
        #Inside a Pod
        config.load_incluster_config()
        k8s_client = ApiClient(configuration=client.Configuration())
    else:
        #Outside a Pod
        k8s_client = config.new_client_from_config()
    dyn_client = DynamicClient(k8s_client)
    v1_pod = dyn_client.resources.get(api_version='v1', kind='Pod')
    for event in v1_pod.watch(namespace=NAMESPACE):
        #print(event['object'])
        print("Event: %s %s %s" % (event['type'], event['object'].metadata.name, event['object'].metadata.resourceVersion))


def pod_for_all_namespaces():
    if INSIDE_POD:
        #Inside a Pod
        config.load_incluster_config()
        k8s_client = ApiClient(configuration=client.Configuration())
    else:
        #Outside a Pod
        k8s_client = config.new_client_from_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Usage: python " + sys.argv[0]  + " <INSIDE_POD|OUTSIDE_POD> ")
        exit()
    inpod = sys.argv[1]
    if inpod == "INSIDE_POD":
        INSIDE_POD = True
    EventWatcher()