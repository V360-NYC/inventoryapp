import tempfile
import os
import requests
from google.cloud import storage
import pandas as pd
import shutil

tempdir = tempfile.mkdtemp()

def sendEmail(data, context):
    client = storage.Client(project="dinsightmessenger")
    print(data)
    uid = data['delta']['userID']
    
    filepath = os.path.join(tempdir, 'report.xlsx')

    bucket = client.get_bucket('dinsight-summary-files')

    blob = bucket.blob(uid+'/summary.xlsx')
    doesReportExists = blob.exists()

    if not doesReportExists:
        requests.post(
		"https://api.mailgun.net/v3/devinsider.tech/messages",
	    auth=("api", os.environ.get('API_KEY')),
		data={"from": "System <support@v360.studio>",
			"to": data['delta']['email'],
			"subject": data['delta']['subject'],
			"text": "Summary Report not available. This might be because of your inventory in empty."})

        return

    print(filepath)
    with open(filepath, 'wb+') as file:
        blob.download_to_file(file)
    
    requests.post(
		"https://api.mailgun.net/v3/devinsider.tech/messages",
	    auth=("api", os.environ.get('API_KEY')),
        files={"attachment":open(filepath, 'rb')},
		data={"from": "System <support@v360.studio>",
			"to": data['delta']['email'],
			"subject": data['delta']['subject'],
			"text": "Find Attached summary file"})
    
  


    