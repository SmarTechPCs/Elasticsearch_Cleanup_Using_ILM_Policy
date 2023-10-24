import requests
from configuration import *
from exceptions import *


def prepare_es_connection(es_url, es_auth):
    global url
    global auth
    auth = es_auth
    url = es_url


def delete_policy():

    print("Trying to delete policy...")

    policy_delete_url = f"{url}/_ilm/policy/{POLICY_NAME}"

    response = requests.delete(policy_delete_url, auth=auth)
    if response.status_code == 404:
        print("Policy not found. Considered as successful deletion.")
    elif response.status_code != 200:
        raise DeletePolicyException(response.text)
    print("Policy deleted.")


def create_policy(min_days):

    print("Trying to create policy...")

    policy_create_url = f"{url}/_ilm/policy/{POLICY_NAME}"

    payload = {
        "policy": {
            "phases": {
                "hot": {"actions": {}},
                "delete": {"min_age": f"{min_days}d", "actions": {"delete": {}}}
            }
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(policy_create_url, json=payload, auth=auth, headers=headers)
    if response.status_code != 200:
        raise CreatePolicyException(response.text)
    print("Policy created.")


def attach_policy():

    print("Trying to attach policy to indices...")

    index_settings_url = f"{url}/{INDEX_PATTERN}/_settings"
    headers = {"Content-Type": "application/json"}

    payload = {"lifecycle.name": POLICY_NAME}
    response = requests.put(index_settings_url, json=payload, auth=auth, headers=headers)
    if response.status_code != 200:
        raise AttachPolicyException(response.text)
    print("Policy attached successfully to index.")


url = auth = ""
