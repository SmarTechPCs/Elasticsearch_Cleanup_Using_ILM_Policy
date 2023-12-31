# Elasticsearch Indices Cleanup Script Using ILM policy (Python3)

## What is this for?
This is an automated utility to delete logs from Elasticsearch indices, logs that are older than a defined number of days. This allows reclaiming storage space and improving Elasticsearch engine performance. 
This utility is relevant where no other means is used to maintain this Elasticsearch indices cleanup procedure.

## Installation
(1) Use git clone to download the latest version of the utility.
(2) Set up three environment variables:
ELASTICSEARCH_URL
ELASTICSEARCH_USERNAME
ELASTICSEARCH_PASSWORD
based of the relevant credential for Elasticsearch. Make sure ES is accessible from this environment.
**
Tip: If you are using a container orchestration platform, like K8s, use container secrets mechanism to protect them and expose them safely in workload.
**

Please note: ELASTICSEARCH_URL must include protocol prefix like https: https://elasticsearch.domain.svc:9200

(3) Create a scheduled task or cron job to run the Python script on a regular basis using the command:
python3 es_cleaner_start.py <number_of_days>
replacing <number_of_days> with the chosen number of retention days. 

(4) Enjoy!
