# serverless-api-example

## AWS Cloudformation
# test

### Create Stack

```shell

# CCOM
aws cloudformation create-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/clash-of-clans-manager.yml --capabilities CAPABILITY_NAMED_IAM --disable-rollback --stack-name SAPIE

# SAPIE-VPC
aws cloudformation create-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/vpc/vpc.yml --disable-rollback --stack-name SAPIE-VPC

# FBE-EC2-IAM
aws cloudformation create-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/IAM/iam.yml --capabilities CAPABILITY_NAMED_IAM --disable-rollback --stack-name SAPIE-IAM

# FBE-EC2-Lambda
aws cloudformation create-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/lambda/lambda.yml --disable-rollback --stack-name SAPIE-Lambda

```


### Update Stack

```shell
#CCOM
aws cloudformation update-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/clash-of-clans-manager.yml --capabilities CAPABILITY_NAMED_IAM --stack-name SAPIE

# SAPIE-VPC
aws cloudformation update-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/vpc/vpc.yml --stack-name SAPIE-VPC

# FBE-EC2-IAM
aws cloudformation update-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/IAM/iam.yml --capabilities CAPABILITY_NAMED_IAM --stack-name SAPIE-IAM

# FBE-EC2-Lambda
aws cloudformation update-stack --template-url https://serverless-api-example-cloudformation.s3.amazonaws.com/lambda/lambda.yml --stack-name SAPIE-Lambda

```