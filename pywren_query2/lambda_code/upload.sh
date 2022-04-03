rm lambda_code.zip
zip -r lambda_code.zip .
aws lambda update-function-code --function-name query2 --zip-file fileb://~/lambda_analysis/pywren_query2/lambda_code/lambda_code.zip