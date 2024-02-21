#pip install selenium

# Download web driver from https://sites.google.com/chromium.org/driver/?pli=1
# This program will use self-signed certificate, no HA, non-air gap and local AD authen
# Run this program will open a new Chrome browser and stop before clicking submit
# Don't terminate the program during installation or it will close the browser
# If need to rerun, terminate this program and run again.
# adjust the timeout if the network is slow
# Deploy Target values allow "Bare Metal","VM","Openshift"

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

timeout = 300

class UAinputconfig():
    def setup_method(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def input_config(self):
        # Test name: UA input config
        # Step # | name | target | value
        # 1 | open | config['UA_URL'] = "http://localhost:8080/" |
        self.driver.get(config['UA_URL'])
        # 2 | setWindowSize | 1679x1297 |
        self.driver.set_window_size(1679, 1297)
        # 3 | waitForElementVisible | css=.caUcER:nth-child(2) .StyledButtonKind-sc-1vhfpnt-0 | 0
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, ".dYiJaI:nth-child(5)")))
        # 4 | New install or Using Existing kubeconfig file

        if config['Kubeconfig_Path'] == '':
            self.driver.find_element(By.CSS_SELECTOR, ".dYiJaI:nth-child(5)").click()
        else:
            self.driver.find_element(By.ID, "ezua-upload-kubeconfig-form-configfile").send_keys(config['Kubeconfig_Path'])
            self.driver.find_element(By.ID, "ezua-upload-kubeconfig-form-submit").click()

        # 5 | waitForElementVisible | name=deployname | 0
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".StyledBox-sc-13pk1d4-0:nth-child(2) > .StyledBox-sc-13pk1d4-0 > .keMOfF")))

        # 6 | click | name=deployname |
        if config['Deploy_Target'] == "Bare Metal":
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  ".StyledGrid-sc-1wofa1l-0:nth-child(1) > .StyledBox-sc-13pk1d4-0:nth-child(1) .StyledButtonKind-sc-1vhfpnt-0"))).click()
        elif config['Deploy_Target'] == "VM":
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ".StyledBox-sc-13pk1d4-0:nth-child(2) > .StyledBox-sc-13pk1d4-0 > .keMOfF"))).click()
        elif config['Deploy_Target'] == "Openshift":
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ".StyledGrid-sc-1wofa1l-0:nth-child(3) .keMOfF"))).click()
            input("To be developed. Press Enter to close the browser...")
            self.teardown_method()
        else:
            input("Deploy_Target invalid. Values allow 'Bare Metal','VM' and 'Openshift'. Press Enter to close the browser...")
            self.teardown_method()
        #Node Setup
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(.,\'Manual Configuration\')]"))).click()
        self.driver.find_element(By.NAME, "pphconfig.ssh_username").send_keys(Keys.SHIFT, Keys.ARROW_UP)
        self.driver.find_element(By.NAME, "pphconfig.ssh_username").send_keys(config["Node_Setup_Username"])
        self.driver.find_element(By.NAME, "credentialType").click()
        if config['Node_Setup_Credntials_Type'] == "Password":
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Password\')]").click()
            self.driver.find_element(By.NAME, "pphconfig.ssh_password").send_keys(config["Node_Setup_Password"])
        elif config['Node_Setup_Credntials_Type'] == "SSH Key":
            self.driver.find_element(By.XPATH, "//button[contains(.,\'SSH Key\')]").click()
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Select File\')]").send_keys(config['Node_Setup_SSH_Key_Path'])

        self.driver.find_element(By.NAME, "pphconfig.controlplanes").send_keys(config["Coordinator_IPs"]+","+config["Control_Plane_IPs"])
        self.driver.find_element(By.NAME, "pphconfig.workers").send_keys(config["Workers_IPs"])
        self.driver.find_element(By.NAME, "pphconfig.external_url").send_keys(config["External_Cluster_Endpoint"])
        self.driver.find_element(By.CSS_SELECTOR, ".eQEJTX > .StyledBox-sc-13pk1d4-0").click()

        #Installation Details
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(
            (By.NAME, "deployname"))).send_keys(config["Installation_Name"])
        self.driver.find_element(By.NAME, "domainname").send_keys(config["Domain_Name"])
        self.driver.find_element(By.NAME, "infraconfig.vcpu").send_keys(Keys.BACKSPACE*5)
        self.driver.find_element(By.NAME, "infraconfig.vcpu").send_keys(config["VCPU"])

        if config['Is_HA'] == "true":
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".StyledBox-sc-13pk1d4-0:nth-child(4) > .StyledBox-sc-13pk1d4-0 > .StyledBox-sc-13pk1d4-0 > .StyledCheckBox__StyledCheckBoxContainer-sc-1dbk5ju-1 > .StyledBox-sc-13pk1d4-0 > .StyledBox-sc-13pk1d4-0").click()
        if config['Is_GPU'] =='true':
            self.driver.find_element(By.CSS_SELECTOR,
                                 ".StyledBox-sc-13pk1d4-0:nth-child(5) > .StyledBox-sc-13pk1d4-0 .StyledBox-sc-13pk1d4-0 > .StyledBox-sc-13pk1d4-0").click()
            self.driver.find_element(By.NAME, "infraconfig.vgpu").send_keys(config['VGPU'])
            self.driver.find_element(By.NAME, "infraconfig.gpu_partition_size").click()
            if config['GPU_Size']=='whole':
                self.driver.find_element(By.XPATH, "//button[contains(.,\'whole\')]").click()
            elif config['GPU_Size']=='large':
                self.driver.find_element(By.XPATH, "//button[contains(.,\'large\')]").click()
            elif config['GPU_Size'] == 'medium':
                self.driver.find_element(By.XPATH, "//button[contains(.,\'medium\')]").click()
            elif config['GPU_Size'] == 'small':
                self.driver.find_element(By.XPATH, "//button[contains(.,\'small\')]").click()

        if config['Is_airgap'] == "true":
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Air Gap Environment?\')]").click()
        self.driver.find_element(By.NAME, "airgap.registryUrl").send_keys(config["Registry_URL"])
        self.driver.find_element(By.NAME, "airgap.username").send_keys(config["Registry_Username"])
        self.driver.find_element(By.NAME, "airgap.password").send_keys(config["Registry_Password"])

        if config['Is_Registry_Insecure'] == "true":
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Registry Insecure\')]").click()
        #CA cert
        if config['Registry_CA_Cert_Path'] !='':
            self.driver.find_element(By.ID, "airgap.registryCaFile").send_keys(config['Registry_CA_Cert_Path'])

        if config['Is_Self_Signed_Cert'] == 'true':
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Use Self Signed Certificate\')]").click()
        else:
            self.driver.find_element(By.ID, "tlsconfig.ca").send_keys(config['TLS_CA_cert_Path'])
            self.driver.find_element(By.ID, "tlsconfig.key").send_keys(config['TLS_Prviate_Key_Path'])
            self.driver.find_element(By.ID, "tlsconfig.cert").send_keys(config['TLS_Cert_Path'])

        self.driver.find_element(By.NAME, "proxy.httpProxy").send_keys(config["HTTP_Proxy"])
        self.driver.find_element(By.NAME, "proxy.httpsProxy").send_keys(config["HTTPS_Proxy"])
        self.driver.find_element(By.NAME, "proxy.noProxy").send_keys(config["No_Proxy"])
        self.driver.find_element(By.XPATH, "//footer/button").click()

        #User Authen Details
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,\'Use External LDAP Server\')]")))
        if config['Is_External_LDAP']=="true":
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Use External LDAP Server\')]").click()
            if config['Is_Active_Directory']=="true":
                self.driver.find_element(By.XPATH, "//span[contains(.,\'Active Directory?\')]").click()
            self.driver.find_element(By.NAME, "authconfig.external.security_protocol").click()
            if config['External_LDAP_Security_Protocol']=="StartTLS":
                self.driver.find_element(By.XPATH, "//button[contains(.,\'StartTLS\')]").click()
            elif config['External_LDAP_Security_Protocol']=="LDAPS":
                self.driver.find_element(By.XPATH, "//button[contains(.,\'LDAPS\')]").click()
            elif config['External_LDAP_Security_Protocol']=="None":
                self.driver.find_element(By.XPATH, "//button[contains(.,\'None\')]").click()
            self.driver.find_element(By.NAME, "authconfig.external.server_address").send_keys(config['External_LDAP_Server_Address'])
            self.driver.find_element(By.NAME, "authconfig.external.server_port").send_keys(config['External_LDAP_Server_Port'])
            self.driver.find_element(By.NAME, "authconfig.external.bind_dn").send_keys(config['External_LDAP_Bind_DN'])
            self.driver.find_element(By.NAME, "authconfig.external.bind_password").send_keys(config['External_LDAP_Bind_Password'])
            self.driver.find_element(By.NAME, "authconfig.external.search_base_dn").send_keys(config['External_LDAP_Search_Base_DN'])
            if config['External_LDAP_Trust_Store_File_Path']!='':
                self.driver.find_element(By.NAME, "authconfig.external.truststore_file").send_keys(config['External_LDAP_Trust_Store_File_Path'])
            self.driver.find_element(By.NAME, "authconfig.external.truststore_pass").send_keys(config['External_LDAP_Trust_Store_Password'])
            self.driver.find_element(By.NAME, "authconfig.external.user_attribute.username").send_keys(config['External_LDAP_Username_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.user_attribute.fullname").send_keys(config['External_LDAP_Fullname_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.user_attribute.email").send_keys(config['External_LDAP_Email_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.user_attribute.uid").send_keys(config['External_LDAP_UID_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.user_attribute.gid").send_keys(config['External_LDAP_GID_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.group_attribute.group_gid").send_keys(config['External_LDAP_GID_Attribute'])
            self.driver.find_element(By.NAME, "authconfig.external.admin_user.username").send_keys(config['External_LDAP_Default_Admin_User'])
            if config['Is_External_LDAP_Validation']=='false':
                self.driver.find_element(By.XPATH,
                                         "//span[contains(.,\'Locally test AD/LDAP settings and connection before starting install\')]").click()
                self.driver.find_element(By.XPATH,
                                         "//span[contains(.,\'Test AD/LDAP connection from UA cluster during install\')]").click()

        else:
            self.driver.find_element(By.NAME, "authconfig.internal.admin_user.username").send_keys(config['Internal_LDAP_Username'])
            self.driver.find_element(By.NAME, "authconfig.internal.admin_user.fullname").send_keys(config['Internal_LDAP_Full_Name'])
            self.driver.find_element(By.NAME, "authconfig.internal.admin_user.email").send_keys(config['Internal_LDAP_Email'])
            self.driver.find_element(By.NAME, "authconfig.internal.admin_user.password").send_keys(config['Internal_LDAP_Password'])

        # self.driver.find_element(By.XPATH, "//button[contains(.,\'Submit\')]").click()
def main():
    auto = UAinputconfig()
    auto.setup_method()
    auto.input_config()
    while True:
        time.sleep(600)
    return

if __name__ == '__main__':
    main()