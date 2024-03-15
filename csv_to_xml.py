from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint
import ast

# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'dd56805c-3e3f-4b15-85ed-db9482fb843a'



# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = 'files_to_compare/Kamly.docx' # file | Input file to perform the operation on.

try:
    # Convert Word DOCX Document to PDF
    api_response = api_instance.convert_document_docx_to_pdf(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_docx_to_pdf: %s\n" % e)
output_file = "output.pdf"

data = ast.literal_eval(api_response)

with open(output_file, 'wb') as binary_file:
    binary_file.write(data)