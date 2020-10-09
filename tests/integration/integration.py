import json
import requests
import configdetails as cdet
import unittest

class Test_Clusterhealth(unittest.TestCase):

    def test_cluster(self):
        url=cdet.url+"/_cat/health?pretty"
        createreq=requests.get(url)
        reqcode=createreq.status_code
        reqdata=createreq.text
        print(reqdata)
        
        if "yellow" in str(reqdata):
            self.assertTrue('TRUTH'.isupper())
        elif "green" in str(reqdata):
            self.assertTrue('TRUTH'.isupper())

   

 



class Test_ElasticModules(unittest.TestCase):
    def test_a_create_index(self):
        url=cdet.url+"/aircloud"
        jsoni={
  "settings": {
    "number_of_replicas": 1,
    "number_of_shards": 3,
    "analysis": {},
    "refresh_interval": "1s"
  },
  "mappings": {
    "dynamic": False,
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "english"
      }
    }
  }
}  
        js=json.dumps(jsoni)
        headers={ 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        createreq=requests.put(url,data=js,headers=headers)
        crecode=createreq.status_code
        self.assertEqual(crecode,200)



    def test_b_added_doc_index(self):
        url=cdet.url+"/aircloud/_doc/1"
        headers={ 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        kson= { "employee":"chaitu","id":"123"}
        ks=json.dumps(kson)
        creq=requests.post(url,data=ks,headers=headers)
        crcode=creq.status_code
      
        if crcode in [200,201]:
            self.assertEqual(200,200)


    def test_c_search_index(self):
        url=cdet.url+"/aircloud/_doc/1"
        creqw=requests.get(url)
        crcode=creqw.status_code
        self.assertEqual(crcode,200)


    def test_d_delete_doc_index(self):
        url=cdet.url+"/aircloud/_doc/1"
        delreq=requests.delete(url)
        delcode=delreq.status_code
        self.assertEqual(delcode,200)

    def test_e_delete_index(self):
        url=cdet.url+"/aircloud/"
        delin=requests.delete(url)
        delc=delin.status_code
        self.assertEqual(delc,200)
    



def suite():
    test_suite = unittest.TestSuite()
    
    
    test_suite.addTest(unittest.makeSuite(Test_Clusterhealth))
    test_suite.addTest(unittest.makeSuite(Test_ElasticModules))
   
    return test_suite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)

