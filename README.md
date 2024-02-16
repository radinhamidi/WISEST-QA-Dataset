# WISEST-QA-Dataset

## Install the fetcher
```
pip install wisest-data-fetcher==0.1
```
## Usage
```
import wisest_data_fetcher.fetcher as fetcher
import json

qa_dataset_url = 'https://wisest-data.ls3.rnet.torontomu.ca/qa_data/'
qa_dataset = fetcher.fetch_json(qa_dataset_url)

dpr_dataset_url = 'https://wisest-data.ls3.rnet.torontomu.ca/dpr_data/'
dpr_dataset = fetcher.fetch_json(dpr_dataset_url)

idx_dataset_url = 'https://wisest-data.ls3.rnet.torontomu.ca/index/'
idx_dataset = fetcher.fetch_json(idx_dataset_url)

# Save the QA dataset to a file
with open('WQA_QA.json', 'w') as f:
    json.dump(qa_dataset, f, indent=4)

# Save the DPR dataset to a file
with open('WQA_DPR.json', 'w') as f:
    json.dump(dpr_dataset, f, indent=4)

# Save the IDX dataset to a file
with open('WQA_IDX.json', 'w') as f:
    json.dump(idx_dataset, f, indent=4)
```
