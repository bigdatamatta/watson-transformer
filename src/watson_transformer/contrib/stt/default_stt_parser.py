
import json
from watson_transformer.contrib.response_base import ResponseBase
from pyspark.sql.types import StringType, FloatType, StructType, StructField, Row
from pyspark.sql import functions as F

"""
"
" default STT output interpreter which assume one alternative transcript and no speaker detection
"
"""

class DefaultSTTParser(ResponseBase):

    def __init__(self):
        super(DefaultSTTParser, self).__init__()


    """
    "
    " pass the json response to datatype
    "
    """
    def __call__(self, json_response):
        """
        @param::output: the output json object from STT
        @return:the transcript join by period in string format
        """
        response = json.loads(json_response)
        transcripts = [doc['alternatives'][0]['transcript'].strip() for doc in response['results']]
        return '. '.join(transcripts) + '.'

    """
    "
    " return the default STT return type
    "
    """
    def get_return_type(self):
        """
        @return: the defined return type and Pandas UDF data type
        """
        return  StringType()