---
tags:
  - topic
  - intermediate
  - codespaces
---

# Lab Name


|             |                                                                                                         |
| ----------: | :-------------------------------------------------------------------------------------------------------|
| Level       | intermediate                                                                                            |
| Repo        | [https://github.com/NetAutLabs/mpls_l3_vpn_service](https://github.com/NetAutLabs/mpls_l3_vpn_service)  |
| Discussion  | [Discussion GitHub Repo](https://github.com/NetAutLabs/mpls_l3_vpn_service/discussions)                 |
| Codespaces  | :material-check: [GitHub Codespaces](https://codespaces.new/NetAutLabs/mpls_l3_vpn_service)             |


In this lab, you will ...

## Setup

``` mermaid
flowchart LR
    h1{h1}
    h2{h2}
    h3{h3}
    h4{h4}
    edge1(edge1)
    edge2(edge2)
    core1
    
    edge1 ---|MPLS| core1 ---|MPLS| edge2
    
    h1 ---- edge1
    edge2 ---- h3
    h2 ---- edge1
    edge2 ---- h4

    subgraph CustX
        h2
        h4
    end
    subgraph CustA
        h1
        h3
    end

```

To interact with the virtual devices, you need to start the topology located in the "netlab" directory. From the main directory, you can use the shortcut command `make setup` to initiate it. To tear down the lab, use `make destroy`. If you have the necessary expertise, you can edit the [netlab](https://netlab.tools) topology, such as changing the Network Operating Systems (NOSs).


## Lab
In general, you have to automate the following use case and implement it with Ansible.
The labs go hand in hand with the lecture. Self-research and finding a solution are part of the lab
but do not hesitate to ask for advice if you are stuck.


### L3 Service

Automate the deployment of new L3 Services (VRFs) on edge routers.


For every L3 service on an edge router, the VRF must be created and added to the BGP address family.
As you know from CN2 for L3 MPLS, BGP must be configured in a full mash or using a route reflector.
Also, LDP must be enabled on the interfaces and IP connectivity between BGP peers.


Some of the involved technologies:

- VRFs
- MPLS
- LDP
- BGP
- OSPF

### How to start


It can be overwhelming and hard to find a good strategy how to start this lab.
For the kickstart, a project template is provided.
Part of the lab is to be able to get an abstract requirement and be able to analyze what is needed.


The following is a possible approach to reach the goal as efficiently as possible.


- Configure it manually (Bevor you can automate something you should understand what you need to do)
- Document in a text file what steps need to be done and how they depend on each other
- Try to separate the base setup (for all services the same and needed once) and the service individual configuration.
- Spot variables in your service configuration. What values are changing for different deployments?
- Create Templates where it makes sense
- Automate the workflow



### MPLS Refresh

In the module Bachelor studies, you learned about MPLS and also had a practical lab. If you don't remember all the details don't worry.
For this lab, you don't need a deep MPLS understanding as the basic configuration is given already.

#### MPLS Edge

Talking about MPLS the construct of Provider Edge (PE) and Customer Edge (CE) routers is coming up in our minds. CEs connect to a PE and exchange in an L3 Service
the IPv4 and IPv6 prefixes and learn from the PE the available prefixes on other connection exchanged networks. For the exchange of these prefixes routing protocols are used.
This is necessary if the PEs and the CEs are not managed by the same party for example if the MPLS L3Service is bought by a service provider.
If the same organization is managing both devices there is most cases no need to add this additional complexity. So, what we can do is combine the PEs and CEs into an edge router.

**In this lab, we control all the hardware and can do the "MPLS to the Edge" approach.**

!!! info 

    Lab Configuration
    The lab is already preconfigured with the base config and MPLS (OSPF and BGP).
    Also the Service for  `CustA` is already configured as an example. This service should be part of your automation.
    Base and MPLS configurations are static and do not need to be automated (The automation is done with `netlab` to spin up the topology).


## Task

Automate the use case with Ansible. Services need to be deployed or de-provisioned by editing the file `services.yaml`.
To add a new service, it needs to be added to `services.yaml` and the playbook needs to be executed.
If a service is removed in `services.yaml`, the service needs to be removed on the network devices after running the same playbook again.
There are not a lot of requirements; Therefore you have a lot of freedom but also makes this exercise more challenging.

