#pip install pyvmomi first

import ssl
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from pyVim.task import WaitForTask

# Authenticate with vCenter Server
server = '10.85.235.77'
username = "administrator@vsphere.local"
password = "P@ssw0rd"
vm_name_list = ['UAcontrol','UAworker1','UAworker2','UAworker3']

def delete_vm(vm_name: str):
    # Find the virtual machine to delete
    content = si.RetrieveContent()
    vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vm = next((vm for vm in vm_view.view if vm.name == vm_name), None)
    if not vm:
        print(f'VM {vm_name} not found')
        # Disconnect(si)
        # return

    # Delete the virtual machine from disk
    elif vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
        WaitForTask(vm.PowerOffVM_Task())
        print(f'VM {vm_name} powered off')
        WaitForTask(vm.Destroy_Task())
        print(f'VM {vm_name} deleted from disk')


# Disable SSL certificate verification
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_NONE

# Connect to vCenter Server
si = SmartConnect(host=server, user=username, pwd=password, sslContext=context)

for vm in vm_name_list:
    delete_vm(vm)

# Disconnect from vCenter Server
Disconnect(si)
