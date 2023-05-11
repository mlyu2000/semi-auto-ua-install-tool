#pip install selenium

# Download web driver from https://sites.google.com/chromium.org/driver/?pli=1
# This program will use self-signed certificate, no HA, non-air gap and local AD authen
# Run this program will open a new Chrome browser and stop before clicking submit
# Don't terminate the program during installation or it will close the browser
# If need to rerun, terminate this program and run again.
# adjust the timeout if the network is slow
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

with open("ua-config.json") as f:
    config = json.load(f)

timeout = 10

class UAinputconfig():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def input_config(self):
        # Test name: UA input config
        # Step # | name | target | value
        # 1 | open | http://10.85.236.99:8080/ |
        self.driver.get(config['UA_URL'])
        # 2 | setWindowSize | 1679x1297 |
        self.driver.set_window_size(1679, 1297)
        # 3 | waitForElementVisible | css=.caUcER:nth-child(2) .StyledButtonKind-sc-1vhfpnt-0 | 0
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, ".caUcER:nth-child(2) .StyledButtonKind-sc-1vhfpnt-0")))
        # 4 | click | css=.caUcER:nth-child(2) .StyledButtonKind-sc-1vhfpnt-0 |
        self.driver.find_element(By.CSS_SELECTOR, ".caUcER:nth-child(2) .StyledButtonKind-sc-1vhfpnt-0").click()
        # 5 | waitForElementVisible | name=deployname | 0
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located((By.NAME, "deployname")))
        # 6 | click | name=deployname |
        self.driver.find_element(By.NAME, "deployname").click()
        # 7 | type | name=deployname | uacluster
        self.driver.find_element(By.NAME, "deployname").send_keys(config["Installation_Name"])
        # 8 | click | name=domainname |
        self.driver.find_element(By.NAME, "domainname").click()
        # 9 | type | name=domainname | ezmeral.sg
        self.driver.find_element(By.NAME, "domainname").send_keys(config["Domain_Name"])
        # 10 | click | name=proxy.httpProxy |
        self.driver.find_element(By.NAME, "proxy.httpProxy").click()
        self.driver.find_element(By.NAME, "proxy.httpProxy").send_keys(config["HTTP_Proxy"])
        # 11 | click | name=proxy.httpsProxy |
        self.driver.find_element(By.NAME, "proxy.httpsProxy").click()
        self.driver.find_element(By.NAME, "proxy.httpsProxy").send_keys(config["HTTPS_Proxy"])
        # 12 | click | name=proxy.noProxy |
        self.driver.find_element(By.NAME, "proxy.noProxy").click()
        # 13 | type | name=proxy.noProxy | 127.0.0.1
        self.driver.find_element(By.NAME, "proxy.noProxy").send_keys(config["No_Proxy"])
        # 14 | click | css=.ewwyzz |
        self.driver.find_element(By.CSS_SELECTOR, ".ewwyzz").click()
        # 15 | waitForElementVisible | css=.StyledHeading-sc-1rdh4aw-0 | 0
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".StyledHeading-sc-1rdh4aw-0")))
        # 16 | click | name=onpremconfig.vsphere_server |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_server").click()
        # 17 | type | name=onpremconfig.vsphere_server | 10.85.235.77
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_server").send_keys(config["vSphere_Server"])
        # 18 | click | name=onpremconfig.vsphere_user |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_user").click()
        # 19 | type | name=onpremconfig.vsphere_user | administrator@vsphere.local
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_user").send_keys(config["vSphere_User"])
        # 20 | click | name=onpremconfig.vsphere_password |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_password").click()
        # 21 | type | name=onpremconfig.vsphere_password |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_password").send_keys(config["vSphere_Password"])
        # 22 | click | name=onpremconfig.vsphere_cluster_mgmt |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_cluster_mgmt").click()
        # 23 | type | name=onpremconfig.vsphere_cluster_mgmt | EZAF-MGMT-CLUSTER
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_cluster_mgmt").send_keys(
            config["vSphere_Cluster_Management"])
        # 24 | click | name=onpremconfig.vsphere_cluster_compute |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_cluster_compute").click()
        # 25 | type | name=onpremconfig.vsphere_cluster_compute | EZAF-WORKER-CLUSTER
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_cluster_compute").send_keys(
            config["vSphere_Cluster_Compute"])
        # 26 | click | name=onpremconfig.vsphere_datacenter |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datacenter").click()
        # 27 | type | name=onpremconfig.vsphere_datacenter | Datacenter
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datacenter").send_keys(config['vSphere_Data_Center'])
        # 28 | click | name=onpremconfig.vsphere_datastore_mgmt |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datastore_mgmt").click()
        # 29 | type | name=onpremconfig.vsphere_datastore_mgmt | datastore-76
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datastore_mgmt").send_keys(
            config["vSphere_Datastore_Management"])
        # 30 | click | name=onpremconfig.vsphere_datastore |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datastore").click()
        # 31 | type | name=onpremconfig.vsphere_datastore | datastore-72
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_datastore").send_keys(config["vSphere_Datastore"])
        # 32 | click | name=onpremconfig.vsphere_network |
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_network").click()
        # 33 | type | name=onpremconfig.vsphere_network | VM Network
        self.driver.find_element(By.NAME, "onpremconfig.vsphere_network").send_keys(config["vSphere_Network"])
        # 34 | click | name=onpremconfig.vm_name |
        self.driver.find_element(By.NAME, "onpremconfig.vm_name").click()
        self.driver.find_element(By.NAME, "onpremconfig.vm_name").send_keys(config["VM_Name"])
        # 35 | click | name=onpremconfig.vm_dns_server_list |
        self.driver.find_element(By.NAME, "onpremconfig.vm_dns_server_list").click()
        # 36 | type | name=onpremconfig.vm_dns_server_list | 10.85.235.100
        self.driver.find_element(By.NAME, "onpremconfig.vm_dns_server_list").send_keys(config["VM_DNS_Server_List"])
        # 38 | type | name=onpremconfig.k8s_tmp_name | ezua_k8s_q2_airgapped_testing
        self.driver.find_element(By.NAME, "onpremconfig.k8s_tmp_name").send_keys(config["Kubernetes_Template_Name"])
        # 39 | click | name=onpremconfig.vm_folder |
        self.driver.find_element(By.NAME, "onpremconfig.vm_folder").click()
        # 40 | type | name=onpremconfig.vm_folder | EZUA-SG
        self.driver.find_element(By.NAME, "onpremconfig.vm_folder").send_keys(config["VM_Folder"])
        # 45 | click | name=onpremconfig.vm_ipv4_netmask |
        self.driver.find_element(By.NAME, "onpremconfig.vm_ipv4_netmask").click()
        # 47 | type | name=onpremconfig.vm_ipv4_netmask | 21
        self.driver.find_element(By.NAME, "onpremconfig.vm_ipv4_netmask").send_keys(config["VM_IPV4_Netmask"])
        # 41 | click | name=onpremconfig.vm_default_gateway |
        self.driver.find_element(By.NAME, "onpremconfig.vm_default_gateway").click()
        # 44 | type | name=onpremconfig.vm_default_gateway | 10.85.236.254
        self.driver.find_element(By.NAME, "onpremconfig.vm_default_gateway").send_keys(["VM_Default_Gateway"])
        # 48 | click | name=onpremconfig.masters_node_name |
        self.driver.find_element(By.NAME, "onpremconfig.masters_node_name").click()
        # 49 | type | name=onpremconfig.masters_node_name | UAcontrol
        self.driver.find_element(By.NAME, "onpremconfig.masters_node_name").send_keys(config["Control_Plane_Hostnames"])
        # 50 | click | name=onpremconfig.masters_node_ip |
        self.driver.find_element(By.NAME, "onpremconfig.masters_node_ip").click()
        # 51 | type | name=onpremconfig.masters_node_ip | 10.85.235.95
        self.driver.find_element(By.NAME, "onpremconfig.masters_node_ip").send_keys(config["Control_Plane_IPs"])
        # 52 | click | name=onpremconfig.workers_node_name |
        self.driver.find_element(By.NAME, "onpremconfig.workers_node_name").click()
        # 53 | type | name=onpremconfig.workers_node_name | UAworker1,UAworker2,UAworker3
        self.driver.find_element(By.NAME, "onpremconfig.workers_node_name").send_keys(config["Workers_Hostnames"])
        # 54 | click | name=onpremconfig.workers_datastore |
        self.driver.find_element(By.NAME, "onpremconfig.workers_datastore").click()
        # 55 | type | name=onpremconfig.workers_datastore | datastore-72
        self.driver.find_element(By.NAME, "onpremconfig.workers_datastore").send_keys(config["Workers_Datastore"])
        # 56 | click | name=onpremconfig.workers_node_ip |
        self.driver.find_element(By.NAME, "onpremconfig.workers_node_ip").click()
        # 57 | type | name=onpremconfig.workers_node_ip | 10.85.235.96,10.85.235.97,10.85.235.98
        self.driver.find_element(By.NAME, "onpremconfig.workers_node_ip").send_keys(config["Workers_IPs"])
        # 58 | click | css=.gBDKVT |
        self.driver.find_element(By.CSS_SELECTOR, ".gBDKVT").click()
        # 59 | waitForElementVisible | css=.mDTsJ | 0
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".mDTsJ")))
        # 60 | click | name=authconfig.internal.admin_user.username |
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.username").click()
        # 61 | type | name=authconfig.internal.admin_user.username | admin
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.username").send_keys(config["LDAP_Username"])
        # 62 | click | name=authconfig.internal.admin_user.fullname |
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.fullname").click()
        # 63 | type | name=authconfig.internal.admin_user.fullname | admin
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.fullname").send_keys(config["LDAP_Full_Name"])
        # 64 | click | name=authconfig.internal.admin_user.email |
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.email").click()
        # 65 | type | name=authconfig.internal.admin_user.email | admin@ezmeral.sg
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.email").send_keys(config["LDAP_Email"])
        # 66 | click | name=authconfig.internal.admin_user.password |
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.password").click()
        # 67 | type | name=authconfig.internal.admin_user.password | Admin123!
        self.driver.find_element(By.NAME, "authconfig.internal.admin_user.password").send_keys(config["LDAP_Password"])
        # 68 | click | css=.gBDKVT > .StyledBox-sc-13pk1d4-0 |
        self.driver.find_element(By.CSS_SELECTOR, ".gBDKVT > .StyledBox-sc-13pk1d4-0").click()

def main():
    auto = UAinputconfig()
    auto.setup_method()
    auto.input_config()
    while True:
        time.sleep(600)
    return

if __name__ == '__main__':
    main()