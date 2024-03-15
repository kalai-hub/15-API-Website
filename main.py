from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'dd56805c-3e3f-4b15-85ed-db9482fb843a'



# create an instance of the API class
api_instance = cloudmersive_convert_api_client.CompareDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = 'files_to_compare/Kalai.docx' # file | First input file to perform the operation on.
input_file2 = 'files_to_compare/Kalai.docx' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Compare Two Word DOCX
    api_response = api_instance.compare_document_docx(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompareDocumentApi->compare_document_docx: %s\n" % e)