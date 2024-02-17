# WISEST-QA-Dataset

## Install the fetcher
```
pip install wisest-data-fetcher==0.1
```
## Usage
```
import wisest_data_fetcher.fetcher as fetcher
import json

qa_dataset = fetcher.fetch_json(task='qa', version='latest')

dpr_dataset = fetcher.fetch_json(task='dpr', version='latest')


# Save the QA dataset to a file
with open('WQA_QA.json', 'w') as f:
    json.dump(qa_dataset, f, indent=4)

# Save the DPR dataset to a file
with open('WQA_DPR.json', 'w') as f:
    json.dump(dpr_dataset, f, indent=4)
```
