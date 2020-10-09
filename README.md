# Elk-stack
In this particular project I tried to solve a
usecase which is presented to me where I need to use a 
Jenkins pipeline which triggers on a change in 
the git/master and the all the config maps and 
the pods need to be redeployed if there is a change
and a series of infra , integration,functional,
Performance tests need to be performed on it.


Tools which I used 

1.minikube
2.aws or any cloud service.
3.nginx for reverse proxing.
4.Jenkins for deployment.
5.Gitlab for source code Management.
6.python libraries for the testcases
7.A windows or Unix machine(A UI based) with
java loaded in it for running functional testcases.

So now I'm going to explain the flow of the
implementation in a brief manner.

Setting up minikube:
____________________

So over here I have installed minikube to recreate 
a k8s on a single cloud machine.

Setting up elk stack:
____________________
 
So after the minikube setup has been done I have
created yaml files of each elastic component and 
I have connected both kibana and logstash to our
elastic search using the services.


So now whenever data is populated to elasticsearch you
will be able to view it kibana as both of them are
connected .Let's tell if I want to send data to 
elasticsearch using beats via logstash so I have exposed
the logstash pipeline for the beats , beats will use
the pipeline endpoint to send data to logstash which 
will index it to elastic search.

Beats -> pipeline -> logstash -> elastic (can be viewed on 
Kibana after indexing to elastic)


Setting up beats 
________________
So as we know beats is a lightweight shipper 
which can be used for shipping data I have deployed it 
on daemonset so that it will configured on all the
machines in the kubernetes cluster on one go.So after 
Deploying both filebeats and metricbeats you will be
able to see the filebeat data and metric beat data on 
Kibana.

Setting up Nginx:
__________________
I have used Nginx to reverse proxy all the
elastic and kibana urls which are accessible only on
local network to do functional testing from a different
servers and also make it available on the same network
with a port range limit as NodePorts will be always 
Greater than 30000


So once this done I decided to test the deployment so
To tests I have used different type of tests. These 
are the following one

1. Infrastructure testing

2. Integration testing

3. Functional testing

4. Performance testing

This will be the flow of running the testcases because
whenever we do a deployment of an infrastructure based 
application like elk we need check whether all the
services , pods , deployments are available or not 
Before accesing the endpoints.


The flow of testcases is as follows :

Infrastructure -> integration -> functional ->Performance


Infrastructure tests:
_____________________

So coming to the infrastructure tests I checked whether
all the services,pods,daemonset,configmaps and deployments
are existing or not using python kubernetes library.


Integration tests:
___________________


Once we see elk and beats related infrastructure is
existing we tried to run a integration test which will
Do certain operations on the the elastic search and 
If the operations are successful it will mark it as success
Or else as a failure.


Mockdata entry:
______________


So over here I have dumped mock data to the elastic search 
which will be useful in Functional testing


Functional testcases:
______________________


So in this functionality testing I have used java and
Selenium and I have created a customised test suite
Which will run three times before confirming a failure 
And this test suite check whether all the data I have dumped
Is available or not including the filebeat, metricbeat and
also the mock data which I dumped by creating a index to it

So for my case I have used Nginx make the end points
available on a different network for doing the functionality
testing but in the code which I had put in this repository
This will be done in the local machine itself if u deploy
it in ur PC.
______________________



IAC Implementation
_________________________

Now this whole process is done manually so now I wan
to deploy this whole infrastructure on IaC way so that 
it will remove the whole manual effort and 
everything will be done on single git push

Gitlab
________
I used Gitlab(if u want GitHub u can use it) for 
source code Management with allowing Local networks
on it for making the webhooks work.I have configured 
the webhook so that it will notify the Jenkins
on a new commit. 

I used the Jenkins pipeline which triggers on a push event
call from the Gitlab 

I have created the Jenkinsfile with all the required 
deployment commands on it.


And hurray it's done so wheneveru deploy a change 
In git it will do this whole process without any manual
intervention .


Thank you :)









