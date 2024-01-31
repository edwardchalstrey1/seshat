import base64
import pulumi
from pulumi_azure import core, compute, network

# Create an Azure Resource Group
resource_group = core.ResourceGroup('seshat-pulumi', location='UKSouth')

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

# Create a network security group
network_security_group = network.NetworkSecurityGroup('networkSecurityGroup',
    resource_group_name=resource_group.name,
    security_rules=[
        {'name': 'ssh', 'priority': 1001, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '22', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'http', 'priority': 1002, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '80', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'https', 'priority': 1003, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '443', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'django', 'priority': 1004, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '8000', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
    ]
)

# Create a subnet
subnet = network.Subnet('subnet',
    resource_group_name=resource_group.name,
    virtual_network_name=virtual_network.name,
    address_prefixes=['10.0.2.0/24'],
)

# Associate the network security group with the subnet
association = network.SubnetNetworkSecurityGroupAssociation('association',
    subnet_id=subnet.id,
    network_security_group_id=network_security_group.id,
)

# Create a network interface and associate it with the subnet
network_interface = network.NetworkInterface('networkInterface',
    resource_group_name=resource_group.name,
    ip_configurations=[{
        'name': 'webserver',
        'subnet_id': subnet.id,  # Use the new subnet
        'private_ip_address_allocation': 'Dynamic',
        'public_ip_address_id': public_ip.id,
    }]
)

# Create a data script for the VM
custom_data_script = '''#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip postgresql postgresql-contrib gdal-bin libgdal-dev libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc
sudo apt-get install -y gunicorn
git clone https://github.com/edwardchalstrey1/seshat
cd seshat
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo "export DJANGO_SETTINGS_MODULE=seshat.settings.local" >> venv/bin/activate
gunicorn seshat.wsgi:application --config gunicorn.conf.py &
'''

# Create a VM
vm = compute.LinuxVirtualMachine('vm',
    resource_group_name=resource_group.name,
    network_interface_ids=[network_interface.id],
    size='Standard_D2s_v3',
    source_image_reference={
        'publisher': 'Canonical',
        'offer': '0001-com-ubuntu-server-jammy',
        'sku': '22_04-lts',
        'version': 'latest',
    },
    os_disk={
        'caching': 'ReadWrite',
        'storage_account_type': 'Premium_LRS',
    },
    computer_name='webserver',
    admin_username='webadmin',
    disable_password_authentication=True,
    admin_ssh_keys=[{
        'username': 'webadmin',
        'public_key': pulumi.Config().require_secret('sshPublicKey'),
    }],
    custom_data=base64.b64encode(custom_data_script.encode('ascii')).decode('ascii'),
)

# Export the public IP address of the VM
pulumi.export('publicIp', public_ip.ip_address)