import json

import requests
import time

import urllib
start_time = time.time()

elasticurl="http://10.177.60.134:31243"
index="airbuscloud"
def create_index():
    try:
        headers={ 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        createurlindex=elasticurl+"/"+index
        createjson={
                "settings": {
                "number_of_replicas": 1,
                "number_of_shards": 3,
                "analysis": {},
                "refresh_interval": "1s"
                            },
                "mappings": {
                "dynamic": "false",
                "properties": {
                "title": {
                "type": "text",
                "analyzer": "english"
                         }
                              }
                            }
                 }
        js= json.dumps(createjson)
        createreq=requests.put(createurlindex, data=js, headers=headers)
        createstcode=createreq.status_code
        createreqdata=createreq.text
        response={"responsecode":createstcode,"responsedata":createreqdata}
        return json.dumps(response)
    except Exception as e:
        failres={"responsedata":e,"responsecode":"900"}
        return json.dumps(failres)
      


def delete_index():
    try:
        deleteindex=elasticurl+"/"+index
        deletereq=requests.delete(deleteindex)
        deletecode=deletereq.status_code
        response={"responsecode":deletecode,"responsedata":deletereq.text}
        return json.dumps(response)
    except Exception as e:
        faildel={"responsedata":e,"responsecode":"900"}
        return json.dumps(faildel)

def bulk_upload():
    try:   
        bulkapi=elasticurl+"/"+index+"/"+"_bulk"
        headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        bulkreq = requests.post(bulkapi, data=open('tests/airbus.json', 'rb'), headers=headers)
        bulkcode=bulkreq.status_code
        response={"responsecode":bulkcode,"responsedata":bulkreq.text}
        print(response)
        return json.dumps(response)
    except Exception as e:
        failbulk={"responsedata":e,"responsecode":900}




createdata=create_index()
bulkdata=bulk_upload()
deletedata=delete_index()
print(createdata)
print(bulkdata)
print(deletedata)
end_time = time.time()
print("exec time"+str(start_time-end_time))
print("============================================================================================================================")
print(json.loads(createdata)["responsecode"])
print(json.loads(bulkdata)["responsecode"])
print(json.loads(deletedata)["responsecode"])
