#!/usr/bin/env python3
# Make requests to Elasticsearch API v0.3
# For SAS(R) Viya (R) - gonzalo.navarro@sas.com 
# Buenos Aires, Argentina 2019 ~ 2020 
# More information: 
# https://documentation.sas.com/?docsetId=dplyml0phy0lax&docsetTarget=n0s1g2zrw0jfbln1kd0r88zg6nlx.htm&docsetVersion=3.5&locale=en

# Python Modules - If Missing, install them with pip
import ssl
import requests
import json
import sys

# SAS Viya Certificates
vault_token='/opt/sas/viya/config/etc/SASSecurityCertificateFramework/tokens/elasticsearch-secure/default/vault.token'
es_ca_cert='/opt/sas/viya/config/etc/SASSecurityCertificateFramework/cacerts/trustedcerts.pem'
es_key_file='/opt/sas/viya/config/etc/elasticsearch/default/keys/searchguard/sghealthcheck-key.pem'
es_cert_file='/opt/sas/viya/config/etc/elasticsearch/default/certs/searchguard/sghealthcheck-cert.pem'

# End Point / URL
print("## SAS Viya ElasticSearch API Tool ##")
server=input("# Input Server FQDN (localhost): ")
while not server:
    server="localhost"
serverport=input("# Input Server Port, for Default press ENTER (9200): ")
while not serverport:
	serverport="9200"

# Loop to api endpoint, for doing n* requests.
while True :

    # Print Options
    print("""
    ################# Useful API Endpoints ##################
    # Cluster Health: GET _cluster/health?pretty=true
    # Index Status: GET _status
    # Available Indexes: GET _cat/indices?v
    # Get Mapping: GET _all/_mapping
    # Index allocation details: GET _cat/shards?h=index,shard,prirep,state,unassigned.reason
    # Reindex: POST _reindex
    # Delete: DELETE <index id>
    #
    # Files: elasticsearch_{get, put, post, delete}.json are written after request
    """)

    
    # Select method or quit
    
    method_select = input("# Select API method: (get, put, post, delete or quit): ")
    while method_select == "quit":
        print("# Goodbye JEDI!")
        sys.exit()
        
    api=input("# Input Elasticsearch API Endpoint: ")

    # Connect
    url="https://"+server+":"+serverport+"/"+api
    print("# Selected Server, Port & API:",url)
    
    # API Method -> Persist to file -> Read that file
    if method_select == 'get':
        get = requests.get(url,
                	     	  verify=es_ca_cert,
                        	  cert=(es_cert_file,es_key_file)
                                  )
        file = open('elasticsearch_get.json' ,'w+')
        file.write(get.text)
        file.close
        print("# elasticsearch_get.json file created")
        f = open('elasticsearch_get.json', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
    elif method_select == 'put':
        put = requests.put(url,
                    verify=es_ca_cert,
                            cert=(es_cert_file,es_key_file)
                                   )                   
        file = open('elasticsearch_put.json' ,'w+')
        file.write(put.text)
        file.close
        print("# elasticsearch_put.json file created")
        f = open('elasticsearch_put.json', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
    elif method_select == 'post':
        put = requests.post(url,
                    verify=es_ca_cert,
                            cert=(es_cert_file,es_key_file)
                                   )                   
        file = open('elasticsearch_post.json' ,'w+')
        file.write(put.text)
        file.close
        print("# elasticsearch_post.json file created")
        f = open('elasticsearch_post.json', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()       
    elif method_select == 'delete':
        put = requests.delete(url,
                    verify=es_ca_cert,
                            cert=(es_cert_file,es_key_file)
                                   )                   
        file = open('elasticsearch_delete.json' ,'w+')
        file.write(put.text)
        file.close
        print("# elasticsearch_delete.json file created")
        f = open('elasticsearch_delete.json', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()        
    else:
        if method_select == 'quit':
            print("# Goodbye JEDI!")
            sys.exit()
