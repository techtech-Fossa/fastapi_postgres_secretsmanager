#!/bin/bash
set -e

aws secretsmanager create-secret \
    --name ${USER_ID} \
    --secret-string file:///var/tmp/secrets.json \
    --region ${AWS_REGION} \
    --endpoint-url=${AWS_ENDPOINT_URL}

# export AWS_ENDPOINT_URL=http://localhost:4566
# export AWS_REGION=ap-northeast-1
# export USER_ID=hoge

# aws secretsmanager delete-secret \
#     --secret-id ${USER_ID} \
#     --region ${AWS_REGION} \
#     --force-delete-without-recovery \
#     --profile localstack \
#     --endpoint-url=${AWS_ENDPOINT_URL}

# aws secretsmanager create-secret \
#     --name ${USER_ID} \
#     --secret-string file://aws/secrets.json \
#     --region ${AWS_REGION} \
#     --profile localstack \
#     --endpoint-url=${AWS_ENDPOINT_URL}


# >>>
# {
#     "ARN": "arn:aws:secretsmanager:ap-northeast-1:000000000000:secret:hoge-dNfaIa",
#     "Name": "hoge",
#     "VersionId": "6904a348-1a45-40ab-a506-36687d32aa5e"
# }


# aws secretsmanager get-secret-value \
#     --secret-id ${USER_ID} \
#     --region ${AWS_REGION} \
#     --endpoint-url=${AWS_ENDPOINT_URL}