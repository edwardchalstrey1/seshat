import pulumi
from pulumi_azure import core, compute, network
from pulumi import Output
import pulumi_azuread as azuread
import pulumi_random as random
from pulumi_azure import storage

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("seshat-pulumi")

# Create a network with a single subnet
virtual_network = network.VirtualNetwork('virtualNetwork',
    resource_group_name=resource_group.name,
    address_spaces=['10.0.0.0/16'],
    subnets=[{
        'name': 'default',
        'address_prefix': '10.0.1.0/24',
    }]
)

# Create a public IP
public_ip = network.PublicIp('publicIp',
    resource_group_name=resource_group.name,
    allocation_method='Dynamic'
)

# Create a network interface
network_interface = network.NetworkInterface('networkInterface',
    resource_group_name=resource_group.name,
    ip_configurations=[{
        'name': 'webserver',
        'subnet_id': virtual_network.subnets[0].id,
        'private_ip_address_allocation': 'Dynamic',
        'public_ip_address_id': public_ip.id,
    }]
)

# Create a VM
vm = compute.LinuxVirtualMachine('vm',
    resource_group_name=resource_group.name,
    network_interface_id=network_interface.id,
    size='Standard_D4plds_v5',
    source_image_reference={
        'publisher': 'Canonical',
        'offer': 'UbuntuServer',
        'sku': '22.04-LTS',
        'version': 'latest',
    },
    os_disk={
        'caching': 'ReadWrite',
        'storage_account_type': 'Premium_LRS',
    },
    computer_name='webserver',
    admin_username='webadmin',
    disable_password_authentication=True,
    admin_ssh_key={
        'username': 'webadmin',
        'public_key': pulumi.Config().require('sshPublicKey'),
    },
    custom_data=base64.b64encode('#!/bin/bash\n\
        sudo apt-get update\n\
        sudo apt-get install -y python3 python3-pip postgresql postgresql-contrib gdal-bin libgdal-dev libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc\n\
        git clone https://github.com/edwardchalstrey1/seshat\n\
        cd seshat\n\
        pip3 install -r requirements.txt\n\
        python3 manage.py runserver 0.0.0.0:8000'.encode('ascii')).decode('ascii'),
)

# Export the public IP address of the VM
pulumi.export('publicIp', public_ip.ip_address)