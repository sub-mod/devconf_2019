from kubernetes import client, config, watch
from kubernetes.client import ApiClient, Configuration
from openshift.dynamic import DynamicClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Outside a Pod
k8s_client = config.new_client_from_config()

#Inside a Pod
config.load_incluster_config()
k8s_client = ApiClient(configuration=client.Configuration())

dyn_client = DynamicClient(k8s_client)
v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')
project_list = v1_projects.get()
for project in project_list.items:
    print(project.metadata.name)
