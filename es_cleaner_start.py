#!/usr/bin/env python3

import os
import sys

from es_runner import *
from configuration import *
from exceptions import *

# Error codes
GENERAL_ERROR_CODE = 100
INVALID_INPUT_ERROR_CODE = 200
SUCCESS_CODE = 0

# Environment variables names
ENV_ELASTICSEARCH_URL = "ELASTICSEARCH_URL"
ENV_ELASTICSEARCH_USERNAME = "ELASTICSEARCH_USERNAME"
ENV_ELASTICSEARCH_PASSWORD = "ELASTICSEARCH_PASSWORD"
env_vars = [ENV_ELASTICSEARCH_URL, ENV_ELASTICSEARCH_USERNAME, ENV_ELASTICSEARCH_PASSWORD]


def check_usage():

    if len(sys.argv) != 2 or not sys.argv[1].isdecimal():
        print("Error: Wrong command usage.")
        print(f"Usage: {sys.argv[0]} <number_of_days> # Ex. python3 {sys.argv[0]} {MIN_DAYS}")
        exit(INVALID_INPUT_ERROR_CODE)

    retention_days = sys.argv[1]

    if int(retention_days) < MIN_DAYS:
        print(f"Error: Minimal log retention period is not met. Please allow at least {MIN_DAYS} days")
        exit(INVALID_INPUT_ERROR_CODE)

    return retention_days


def check_environment_variables(elasticsearch_url, elasticsearch_username, elasticsearch_password):
    if not (elasticsearch_url and elasticsearch_username and elasticsearch_password):
        print("Error: Some environment variables are not set.")
        exit(INVALID_INPUT_ERROR_CODE)


def main():

    retention_days = check_usage()

    elasticsearch_url = os.environ.get(ENV_ELASTICSEARCH_URL)
    elasticsearch_username = os.environ.get(ENV_ELASTICSEARCH_USERNAME)
    elasticsearch_password = os.environ.get(ENV_ELASTICSEARCH_PASSWORD)
    authentication_data = (elasticsearch_username, elasticsearch_password)

    check_environment_variables(elasticsearch_url, elasticsearch_username, elasticsearch_password)

    try:
        prepare_es_connection(elasticsearch_url, authentication_data)
        delete_policy()
        create_policy(retention_days)
        attach_policy()
    except (DeletePolicyException, CreatePolicyException, AttachPolicyException) as ex:
        print(ex)
        exit(ex.error_code)
    except Exception as ex:
        print("Failed registering the indices cleanup action:", str(ex))
        exit(GENERAL_ERROR_CODE)

    print("Elasticsearch ILM policy was successfully registered, indices " +
          "cleanup should be initiated soon.")

    exit(SUCCESS_CODE)


if __name__ == "__main__":
    main()
