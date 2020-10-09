#import usertest
#import configtest # first test
import unittest   # second test
import time
from kubernetes import client, config
import configdetails as cdet
import json
nm=cdet.namespace
class Test_pods(unittest.TestCase):
    def test_elk_pods(self):
        podcoll=[]
        elk_pods=cdet.v1.list_namespaced_pod(nm)
        print(len(elk_pods.items))
        for i in elk_pods.items:
            print(i.metadata.name)
            meta=['elastic','kibana','logstash']
            for k in meta:
                if k in i.metadata.name:
                     podcoll.append(i.metadata.name)
     
           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(podcoll)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(podcoll),3)
    def test_kube_pods(self):
        kubepodcoll=[]
        kube_pods=cdet.v1.list_namespaced_pod('kube-system')
        print(len(kube_pods.items))
        for i in kube_pods.items:
            print(i.metadata.name)
            kubemeta=['file','metric']
            for k in kubemeta:
                if k in i.metadata.name:
                     kubepodcoll.append(i.metadata.name)

           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(kubepodcoll)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(kubepodcoll),2)
   
        

 

class Test_services(unittest.TestCase):
    def test_elk_services(self):
        elksercol=[]
        elk_ser=cdet.v1.list_namespaced_service("elk")
        print(len(elk_ser.items))
        for i in elk_ser.items:
            print(i.metadata.name)
            elkmeta=['elastic','logstash','kibana']
            for k in elkmeta:
                if k in i.metadata.name:
                     elksercol.append(i.metadata.name)

           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(elksercol)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(elksercol),3)

     


class Test_deployment(unittest.TestCase):
    def test_elk_deployment(self):
        elkdeploycol=[]
        elk_deploy=cdet.v2.list_namespaced_deployment("elk")
        print(len(elk_deploy.items))
        for i in elk_deploy.items:
            print(i.metadata.name)
            elkdepmeta=['elastic','logstash','kibana']
            for k in elkdepmeta:
                if k in i.metadata.name:
                     elkdeploycol.append(i.metadata.name)

           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(elkdeploycol)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(elkdeploycol),3)

    def test_kube_deployment(self):
        kubedeploycol=[]
        kube_deploy=cdet.v2.list_namespaced_deployment("kube-system")
        print(len(kube_deploy.items))
        for i in kube_deploy.items:
            print(i.metadata.name)
            kubedepmeta=['metric']
            for k in kubedepmeta:
                if k in i.metadata.name:
                     kubedeploycol.append(i.metadata.name)

           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(kubedeploycol)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(kubedeploycol),1)




class Test_daemon(unittest.TestCase):
    def test_daemon_set(self):
        daemoncol=[]
        fm_daemon=cdet.v2.list_namespaced_daemon_set("kube-system")
        print(len(fm_daemon.items))
        for i in fm_daemon.items:
            print(i.metadata.name)
            fmmeta=['filebeat','metricbeat']
            for k in fmmeta:
                if k in i.metadata.name:
                     daemoncol.append(i.metadata.name)

           # if i.metadata.name in ['elastic','kibana','logstash']:
                print(".........")
                print(daemoncol)
               # podcoll.append(i.metadata.name)
        self.assertGreaterEqual(len(daemoncol),2)



class Test_namespace(unittest.TestCase):
    def test_namespace(self):
        namespace=cdet.v1.read_namespace("elk")
        print(namespace)
        if (namespace.metadata.name=="elk"):
            self.assertEqual(namespace.metadata.name,"elk")
'''
if __name__ == '__main__':
    unittest.main()


'''

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    time.sleep(20)
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test_namespace))
    test_suite.addTest(unittest.makeSuite(Test_pods))
    test_suite.addTest(unittest.makeSuite(Test_services))
    test_suite.addTest(unittest.makeSuite(Test_deployment))
    test_suite.addTest(unittest.makeSuite(Test_daemon))
    return test_suite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)

