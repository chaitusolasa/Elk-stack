from kubernetes import client, config
import configdetails as cdet
import json
print(cdet.namespace)
nm=cdet.namespace

#print(cdet.v1.list_namespaced_pod(nm)) 
#print(cf.list_namespaced_pod(nm))

pods=cdet.v1.list_namespaced_pod(nm)
print(len(pods.items))
for i in pods.items:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(i.metadata.namespace)
    print(i.metadata.name)
