from kubernetes import client, config


try:
    config.load_incluster_config()
except config.ConfigException:
    try:
        config.load_kube_config()
    except config.ConfigException:
        raise Exception("Could not configure kubernetes python client")


v2= client.AppsV1Api()
v1=client.CoreV1Api()
appsv1=client.AppsV1Api()
proxturl="http://localhost:8095"
namespace="elk"
