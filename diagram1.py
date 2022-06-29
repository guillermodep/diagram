from asyncio import Server
from termios import ISTRIP
from diagrams import Cluster, Diagram, Edge

#Kubernetes
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.group import Namespace
from diagrams.onprem.network import Nginx
from diagrams.azure.network import FrontDoors

#AZURE_DEVOPS
from diagrams.azure.devops import Devops, Pipelines, Artifacts, Repos

#AKAMAI
from diagrams.saas.cdn import Akamai

graph_attr = {
    "fontsize": "45"
#    "bgcolor": "none"
}

with Diagram("Banca Web", show=False, graph_attr=graph_attr):
    net = Akamai("CDN+WAF+ANTIBOT") >> FrontDoors("bancaweb.pichincha.com") >> Nginx("sp001.pichincha.com") 
    
    with Cluster("Namespaces"):
         ns_group = [Namespace("Banca Web Blue"),Namespace("Banca Wevb Green")] 

    with Cluster("Workload"):
        ns_wl = [Service("edge"),
        Service("auth"),
#        Service("backbase-env-activemq"),
#        Service("bancaweb-edge-empty"),
#        Service("bank-presentation-service"),
#        Service("contact-presentation-service"),
#        Service("contentservices"),
#        Service("credit-card-presentation-service"),
#        Service("document-presentation-service"),
#        Service("investment-service"),
#        Service("parameters-service"),
#        Service("payment-order-presentation-service"),
#        Service("payment-presentation-service"),
        Service("portal"),
#        Service("product-summary"),
#        Service("provisioning"),
        Service("redis-rest"),
#        Service("token-converter"),
#        Service("transaction-presentation-service"),
        Service("etc, etc")
        ]
    
        workload = net >> ns_group >> Ingress("Ingress") >> ns_wl >> Pod("POD")  << HPA("hpa") << Deployment("Deployment")

    with Cluster("Build"):
        ns_devops = [Artifacts("Artefactos"),Repos("Código")]

    workload << Devops("Pipeline") << Pipelines("Pipelines" ) << Edge(color="firebrick", style="dashed") << ns_devops
        

