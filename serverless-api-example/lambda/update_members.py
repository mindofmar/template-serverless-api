import json
import boto3
from botocore.vendored import requests
from botocore.exceptions import ClientError

def request_members( clan_tag ):
    lambda_client = boto3.client('lambda')
    invoke_response = lambda_client.invoke(FunctionName="CCOM-Get-Secret", InvocationType='RequestResponse')
    secret = json.loads(invoke_response['Payload'].read().decode("utf-8"))['body']

    url = "https://api.clashofclans.com/v1/clans/" + clan_tag.replace("#", "%23") + "/members"
    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + secret
    }
    api_response = requests.request("GET", url, headers=headers)

    return api_response.text

def lambda_handler(clan_tag, context):
    
    s3 = boto3.client('s3')
    bucket = "clash-of-clans-manager-json"
    key = "clans/" + clan_tag + "/" + clan_tag + ".json"
    
    try:
        s3_object = s3.get_object( Bucket = bucket, Key = key )
        # s3_object = s3.Object('clash-of-clans-manager-json', event)
    
    # The member list can not be found
    except ClientError as e:
        
        if e.response['Error']['Code'] == "NoSuchKey":
            # Add the member list to S3
            test = "ading clan to s3"
            s3.put_object( Bucket = bucket, Key = key, Body = str( request_members( clan_tag ) ) )
        
        else:
            # There was an error other than NoSuchKey
            raise

    # The member list was found
    else:
        test = "getting clan from s3"
        
        file_content = s3_object['Body'].read().decode('utf-8')
        file_content = json.loads(file_content)
        file_member_tags = []
        for member in file_content['items']:
            file_member_tags.append( member['tag'] )
            
        api_content = json.loads( request_members( clan_tag ) )
        api_member_tags = []
        for member in api_content['items']:
            api_member_tags.append( member['tag'] )
    
    return {
        'statusCode': 200,
        'body': test
        # 'body': json.loads(api_response.text)
        # 'from_file': file_member_tags,
        # 'from_api': api_member_tags
        # 'body': s3_objectdatetime.srtptime(datetime_object, format)
    }