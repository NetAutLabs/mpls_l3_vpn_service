---
tags:
  - nornir
  - python
  - intermediate
  - codespaces
---

# L3VPN Services with Nornir


|             |                                                                                                                      |
| ----------: | :--------------------------------------------------------------------------------------------------------------------|
| Level       | intermediate                                                                                                         |
| Repo        | [https://github.com/NetAutLabs/nornir_mpls_l3_vpn_service](https://github.com/NetAutLabs/nornir_mpls_l3_vpn_service) |
| Discussion  | [Discussion GitHub Repo](https://github.com/NetAutLabs/nornir_mpls_l3_vpn_service/discussions)                       |
| Codespaces  | :material-check: [GitHub Codespaces](https://codespaces.new/NetAutLabs/nornir_mpls_l3_vpn_service)                   |
| NOSs        | Arista cEOS                                                                                                          |


In this lab, you will automate the provisioning and deprovisioning of L3VPN services in an MPLS network based on the service definitions in `services.yaml`.

!!! tip "Fork"

    Fork the repository to be able to commit your changes.


!!! warning "cEOS"

    The topology uses the container `ceos:4.32.1F`. This container needs to be downloaded from Arista and accordingly imported with `docker import <file> ceos:4.32.1F`.



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
In general, you have to automate the following use case and implement it with [Nornir](https://nornir.readthedocs.io/en/stable/index.html).


### L3 Service

In this task, you will automate the deployment of new Layer 3 VPN (L3VPN) services by configuring Virtual Routing and Forwarding (VRF) instances on edge routers.

- **VRF Creation**: For each new L3 service defined in `services.yaml`, a corresponding VRF must be created on the relevant edge routers.
- **BGP Integration**: Once the VRF is created, it must be integrated into the BGP configuration by adding it to the appropriate BGP address family. This ensures that the VRF can exchange routing information with other routers in the MPLS network.
- **Access Interface Configuration**: Configure the appropriate access interfaces on the edge routers and assign them to the correct VRF.

By automating these steps, you will streamline the provisioning of L3VPN services, ensuring consistent and reliable configurations across your network.

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

For this lab, you don't need a deep MPLS understanding as the basic configuration is given already.

#### MPLS Edge

When discussing MPLS, the concepts of Provider Edge (PE) and Customer Edge (CE) routers often come to mind. CEs connect to a PE and exchange IPv4 and IPv6 prefixes within an L3 service, learning about available prefixes on other connected networks through the PE. Routing protocols facilitate this exchange, especially when PEs and CEs are managed by different parties, such as when an MPLS L3 service is provided by a service provider. However, if the same organization manages both devices, this added complexity is often unnecessary. In such cases, PEs and CEs can be combined into a single "edge" router.

**In this lab, we control all the hardware and can do the "MPLS to the Edge" approach.**

!!! info 

    Lab Configuration
    The lab is already preconfigured with the base config and MPLS (OSPF and BGP).
    Also the Service for  `CustA` is already configured as an example. This service should be part of your automation.
    **Base and MPLS configurations are static and do not need to be automated (The automation is done with `netlab` to spin up the topology).**


## Task

Automate this use case using Nornir. Services should be deployed or deprovisioned by modifying the `services.yaml` file.

To add a new service, include it in `services.yaml` and then execute the Python script (`python3 l3vpn/`). If a service is removed or changed in `services.yaml`, the corresponding changes should be applied to the network devices by running the same Python script again.

There isn't a single correct solution -- multiple approaches are valid. All four hosts can be assigned to different services or any combination of services. Note that the base configuration and MPLS/BGP/OSPF configurations do not need to be automated.


## Run your Automation

If you follow the provided project structure, you can start your Python script with the following command:

```bash
python3 l3vpn/ --help
```


!!! tip "Connect to a device"

    To connect to the devices using the shell, you can use `netlab`. Simply navigate to the "netlab" directory and run `netlab connect <device name>`.

    ```bash
    $ cd netlab
    $ netlab connect h1
    Connecting to container clab-netlab-h1, starting bash
    h1:/# ping 172.16.2.2
    PING 172.16.2.2 (172.16.2.2): 56 data bytes
    64 bytes from 172.16.2.2: seq=0 ttl=64 time=41.640 ms
    64 bytes from 172.16.2.2: seq=1 ttl=64 time=1.856 ms
    64 bytes from 172.16.2.2: seq=2 ttl=64 time=1.506 ms
    ```