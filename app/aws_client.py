import boto3
import os
import json

region = os.getenv("AWS_REGION")
user_id = os.getenv("USER_ID")

print(f"{region=}")
print(f"{user_id=}")


def get_secretsmanager_client_local() -> boto3.client:
    """Get boto3 Client For SecretsManager (local env.)

    Returns:
        boto3.client:
    """
    endpoint_url = os.getenv("AWS_ENDPOINT_URL")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    print(f"{endpoint_url=}")
    print(f"{aws_access_key_id=}")
    print(f"{aws_secret_access_key=}")

    client = boto3.client(
        "secretsmanager",
        region_name=region,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    return client


def get_secrets(secret_id: str) -> dict:
    """Get Secrets from SecretsManager

    Args:
        secret_id (str): SecretId

    Returns:
        dict: secret converted from secret string
    """
    secrets_manager_client = get_secretsmanager_client_local()
    secret_value = secrets_manager_client.get_secret_value(SecretId=secret_id)
    secrets = json.loads(secret_value["SecretString"])
    print(f"Secrets: {secrets}")
    return secrets
