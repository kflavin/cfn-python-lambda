# cfn-python-lambda

An example of an AWS Cloudformation, lambda backed custom resource using Python. 

```bash
git clone git@github.com:kflavin/cfn-python-lambda.git
cd cfn-python-lambda
zip -r ../cfn-python-lambda.zip .
aws lambda update-function-code --function-name CreateIAMResources --zip-file fileb://../pylambda.zip
aws lambda create-function --function-name cfn-python-lambda --runtime python2.7 --role <role ARN> --handler lambda_function.lambdahandler --zip-file fileb://../cfn-python-lambda.zip
```

The role should have necessary IAM permissions to create an instance profile.
