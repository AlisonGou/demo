# -*- coding: cp1252 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

#generate token
portal = 'https://myportal'
username = 'username'
password = 'pssword'
clientip = 'XXXXXXXXX'
parameter = ({'username':username, 'password':password,'referer':clientip,'f':'json'})

params = urllib.parse.urlencode(parameter).encode('utf-8')
request = portal +  '/webadaptorname/sharing/rest/generateToken'
ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen(request, params) as url:
    subrequest = url.read()
    response = json.loads(subrequest)
    print (response)
if "token" in response:
    token = response["token"]
    print (token)

#get input params
#input layer could be a feature layer or bigdatafileshare
inputLayer  = {"url":"https://myserver/webadaptorname/rest/services/DataStoreCatalogs/bigDataFileShares_mydata/BigDataCatalogServer/mydata"}
OutputName  =  "test"
context = {"dataStore":"relational","outSR":{"wkid":4326}}
inputdata   = {'inputLayer':inputLayer,'OutputName':OutputName,'context':context,'f':'json','token':token}

# GA gp tool
URL = 'https://mygeoanalyticsserver/webadaptorname/rest/services/System/GeoAnalyticsTools/GPServer/CopyToDataStore/submitJob'
#skip ssl cert verifying
ssl._create_default_https_context = ssl._create_unverified_context

params = urllib.parse.urlencode(inputdata).encode("utf-8")
#send request to GA gp
with urllib.request.urlopen(URL,params) as url:
    submitResponse = url.read()
print (submitResponse)

#check job results
submitjson = json.loads(submitResponse)
taskURL = 'https://mygeoanalyticsserver/webadaptorname/rest/services/System/GeoAnalyticsTools/GPServer/CopyToDataStore'

if 'jobId' in submitjson:
    jobID = submitjson['jobId']
    status = submitjson['jobStatus']
    jobURL = taskURL + "/jobs/" + jobID

    while status == "esriJobSubmitted" or status == "esriJobExecuting":
        print ("checking to see if job is completed...")
        #how often to check job status
        time.sleep(5)
        

        requestparams= {'f':'json','token':token}
        requestparamsencode = urllib.parse.urlencode(requestparams).encode('utf-8')
        with urllib.request.urlopen(jobURL, requestparamsencode) as url:
            subrequest = url.read()

        jobJson = json.loads(subrequest)
        print (jobJson)
        print ("going to check job status")
        if 'jobStatus' in jobJson:
            status = jobJson['jobStatus']

            if status == 'esriJobSucceeded':
                if 'results' in jobJson:
                    resultsUrl =  jobURL +  "/results/output"
                    requestparams1= {'f':'json','token':token}
                    requestparamsencode1 = urllib.parse.urlencode(requestparams1).encode('utf-8')
                    with urllib.request.urlopen(resultsUrl, requestparamsencode1) as url:
                        results = url.read()
                    resultparams=json.loads(results)
                    if 'value' in resultparams:
                        #this is the final result url which can be used as further
                        resultURL = resultparams['value']['url']
                        print ('this is the result url')
                        print (resultURL)

            if status == "esriJobFailed":
                if 'messages' in jobJson:
                    print (jobJson['messages'])

else:
    print ("no jobID found in the response")
                    
        









