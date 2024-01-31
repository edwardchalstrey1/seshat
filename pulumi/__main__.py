"""An Azure RM Python Pulumi program"""

from pulumi_azure_native import resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("seshat-pulumi")

