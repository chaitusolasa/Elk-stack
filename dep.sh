#!/bin/bash

sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-elastic.yml -n elk
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-kibana.yml -n elk
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-log-config.yml -n elk
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-log.yml -n elk
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-file-config.yml
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-file.yml
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-metric-config.yml
sudo kubectl --kubeconfig=/root/.kube/config apply -f elk-metric.yml 
