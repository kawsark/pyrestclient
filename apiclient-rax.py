#Rackspace Cloud REST API V2.0 Client in Python
import requests
import json, re

#Specify a Rackspace cloud region you want to work with: IAD, DFW, ORD, HKG
REGION="iad"

#Specify a credential file with your API key. This information can be obtained from the Account page of Rackspace Cloud Control Panel
#Note: Always protect credential files by storing them in a secure encrypted location.
#It should be of the format below (without the '#'):
# [rackspace_cloud]
# username = my_username
# api_key = 01234567890abcdef
credentials_file="/path/to/credentials_file/pyrax.creds"

#Uses Rackspace Cloud Identity API 2.0: https://developer.rackspace.com/docs/cloud-identity/v2/
def getAuthToken():

	#Load credentials from credentials_file variable
	f = open(credentials_file, 'r')
	pattern = re.compile("\s*\[rackspace_cloud\]\s*username\s*=\s*(\S*)\s*api_key\s*=\s*(\S*)")
	match = pattern.search(f.read())
	if match:
		username = match.group(1) #Extract username
		api_key = match.group(2) #Extract API key

		#Authentication endpoint for API V2
		url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
		#Define Authentication request parameters and authentication token endpoint
		data= {"auth": {"RAX-KSKEY:apiKeyCredentials":{"username": username, "apiKey": api_key}}}
		headers = {'Content-Type': 'application/json', 'Accept': 'application/json', }

		#Make authentication request and return token
		r = requests.post(url, json.dumps(data), headers=headers)

		if(r.status_code == 200):

			#Extract token from response:
			p1 = re.compile("token.*\"id\":\"(.*?)\",")
			m1 = p1.search(r.text)
			token = m1.group(1)

			#Extract tenantId from response:
			p2 = re.compile("\"tenantId\":\"(\d*?)\",")
			m2 = p2.search(r.text)
			tenantId = m2.group(1)

			print "token =", token, ", tenant =", tenantId

			return token, tenantId

		else:

			#Did not get a valid response
			print "Did not get a successful authentication response:", r.json()

			return None

	else:
		print "Could not extract username and api_Key from credentials file. Please adjust credentials_file variable to a valid pyrax credentials: https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating "

		return None

#Using Rackspace Cloud Servers API v2.0 https://developer.rackspace.com/docs/cloud-servers/v2/
def listCloudServers(token,tenantId):

	url  = "https://"+REGION+".servers.api.rackspacecloud.com/v2/"+tenantId+"/servers"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)

	print r.text

#Using Cloud Networks - Neutron API v2.0 https://developer.rackspace.com/docs/cloud-networks/v2/
def listCloudNetworks(token,tenantId):

	url  = "https://"+REGION+".networks.api.rackspacecloud.com/v2.0/networks"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)

	print r.text

#Using Cloud Networks - Neutron API v2.0 https://developer.rackspace.com/docs/cloud-networks/v2/
def listCloudSecurityGroups(token,tenantId):

	url  = "https://"+REGION+".networks.api.rackspacecloud.com/v2.0/security-groups"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)


#	data = {   "security_group":{ "name":"new-webservers", "description":"security group for webservers"} }
#	r = requests.post(url, json.dumps(data), headers=headers)

	print r.text


#Using Rackspace Cloud Backup API 1.0 https://developer.rackspace.com/docs/cloud-backup/v1/
def listCloudBackups(token,tenantId):

	url  = "https://"+REGION+".backup.api.rackspacecloud.com/v1.0/"+tenantId+"/backup-configuration"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)

	print r.text

#Using Rackspace Cloud Block Storage API 1.0 https://developer.rackspace.com/docs/cloud-block-storage/v1/
def listCloudBlockStorage(token,tenantId):

	url  = "https://"+REGION+".blockstorage.api.rackspacecloud.com/v1/"+tenantId+"/volumes"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)

	print r.text


#Using Rackspace Cloud DNS API 1.0 https://developer.rackspace.com/docs/cloud-dns/v1/
def listCloudDNS(token,tenantId):

	url  = "https://dns.api.rackspacecloud.com/v1.0/"+tenantId+"/domains"
	#Define Authentication request parameters and authentication token endpoint
	headers = {'Content-Type': 'application/json',
				'Accept': 'application/json',
				'X-Auth-Token': token}

	r = requests.get(url, headers=headers)

	print r.text

def main():
        #Obtain authentication token
        token, tenantId = getAuthToken()

        #Make calls to view service catalog
        if token:

                print "Listing servers:"
                listCloudServers(token, tenantId)

                print "Listing networks"
                listCloudNetworks(token, tenantId)

                print "Listing Security groups:"
                listCloudSecurityGroups(token, tenantId)

                print "Listing backups:"
                listCloudBackups(token, tenantId)

                print "Listing Cloud Block Storage volumes:"
                listCloudBlockStorage(token, tenantId)

                print "Listing DNS:"
                listCloudDNS(token, tenantId)

        else:
                print "Could not obtain authentication token, please check API credentials"


if __name__ == "__main__":
        main()
