# mmdet_customize
Just for mmdetection usage 


## dataset preparation 
# use custom dataset for mmdet training 
directory should be look like.. 

directory
  - images / train
  - images / test
  - images / val
  - train.json
  - test.json
  - val.json

# modify config files 
top directory: mmdetection/configs/_base_
- models:
- datasets:
- schedules:
- runtime.py

# Running Command 
# Train 
CUDA_VISIBLE_DEVICES={GPU_ID} python tools/train.py configs/{your own repository}/{model_task}.py

# Test 
CUDA_VISIBLE_DEVICES={GPU_ID} python tools/test.py configs/{your repo}/{model_task}.py work_dirs/{model_task}/{checkpoint}.pth —show-dir {test_repository}

### another options can be added please refer to original mmdetection docs 
