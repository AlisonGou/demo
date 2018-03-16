# -*- coding: cp1252 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

#generate token
portal = 'https://myportal'
username = 'username'
password = 'password'
clientip = 'client ip to send the request'
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
#get the service to interpolate
inputPointFeatures =  {"url":"https://myserver/webdaptorname/rest/services/Hosted/myservice/FeatureServer/0"}
interpolateField =  'col_13'
optimizeFor = 'BALANCE'
transformData = 'false'
sizeOfLocalModels = '75'
numberOfNeighbors =   '10'

#output cell size could be changed accordingly
outputCellSize   = {"distance":1,"units":"Kilometers"}
outputPredictionError   = 'false'

OutputName  =  {"serviceProperties":{"name":"outputservicename"}}
returnProcessInfo   = 'true'
data   = {'inputPointFeatures':inputPointFeatures,
             'interpolateField':interpolateField,
             'optimizeFor':optimizeFor,
             'transformData':transformData,
             'sizeOfLocalModels':sizeOfLocalModels,
             'numberOfNeighbors':numberOfNeighbors,
             'outputCellSize':outputCellSize,
             'outputPredictionError':outputPredictionError,
             'OutputName':OutputName,
             'returnProcessInfo':returnProcessInfo,
             'f':'json',
              'token':token}
# RA gp tool
URL = 'https://myraserver/webadaptorname/rest/services/System/RasterAnalysisTools/GPServer/InterpolatePoints/submitJob'
#skip ssl cert verifying
ssl._create_default_https_context = ssl._create_unverified_context
params = urllib.parse.urlencode(data).encode("utf-8")
#send request to RA gp
with urllib.request.urlopen(URL,params) as url:
    submitResponse = url.read()
print (submitResponse)

submitjson = json.loads(submitResponse)
taskURL = 'https://myraserver/webadaptorname/rest/services/System/RasterAnalysisTools/GPServer/InterpolatePoints'
#check gp result
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
                    resultsUrl =  jobURL +  "/results/outputRaster"
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
                    
        









