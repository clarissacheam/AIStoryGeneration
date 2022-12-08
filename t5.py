## -- Run using colab
## -- Each # comment is a section

# install simplet5
!pip install simplet5


# imports
import torch
import csv
import nltk
import pandas as pd
import tensorflow as tf
from simplet5 import SimpleT5
from tqdm import tqdm_notebook as tqdm


# GPU Code
!nvidia-smi

torch.cuda.is_available()
#### Output would be True if Pytorch is using GPU otherwise it would be False.

tf.test.gpu_device_name()
#### Standard output is '/device:GPU:0'


# data processing
data = ["train", "test", "valid"]
### data = ["valid"]

TARGET_DIR = 'working/'
target_data = [TARGET_DIR+"train", TARGET_DIR+"test", TARGET_DIR+"valid"]
### target_data = [TARGET_DIR+"valid"]

NUM_WORDS = 300

for name_id in tqdm(range(len(data))):
    ft = open(data[name_id] + ".wp_target") 
    fp = open(data[name_id] + ".wp_source") 

    stories = ft.readlines()
    prompts = fp.readlines()
    
    #assert len(prompts) == len(stories)
    
    new_stories = [prompts[i].rstrip()+ " <CLS> " + \
                   " ".join(stories[i].split()[
                       0:NUM_WORDS]) for i in range(len(stories))]
    
    with open(target_data[name_id] + ".wp_combined", "w") as o:
        for line in new_stories:
            o.write(line.strip() + "\n")
        print('finish writing',target_data[name_id] + ".wp_combined")
    
    fp.close()
    ft.close()

## testing the outputs
### !head working/train.wp_combined
### !head working/test.wp_combined
### !head working/valid.wp_combined


# data conversion to csvs as simplet5 only takes csvs as input
train_data = pd.read_csv("working/train.wp_combined", 
                         names=['source_text', 'target_text'], 
                         header=None,
                         delimiter="<CLS>")

train_data.shape

test_data = pd.read_csv("working/test.wp_combined", 
                         names=['source_text', 'target_text'], 
                         header=None,
                         delimiter="<CLS>")

test_data.shape

valid_data = pd.read_csv("working/valid.wp_combined", 
                         names=['source_text', 'target_text'], 
                         header=None,
                         delimiter="<CLS>")

valid_data.shape


# Model training
model = SimpleT5()
model.from_pretrained(model_type="t5", model_name="t5-small")

model.train(train_df=train_data, 
            eval_df=test_data, 
            batch_size=8, source_max_token_len=128, 
            target_max_token_len=128, use_gpu=True)


# evaluation
model = SimpleT5()
model.load_model(
    "t5", 
    "simplet5-epoch-1-train-loss-3.0144-val-loss-2.8617"
    )
total = 0
ctr = 0

data = open('results.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(data)
writer.writerow([
                  'prompt', 'original story', 
                  'model story', 'BLEU score'
                  ])
for source, target in zip(valid_data['source_text'], valid_data['target_text']):
    model_prediction = model.predict(source)
    BLEU = nltk.translate.bleu_score.sentence_bleu(model_prediction, target)
    total += BLEU
    ctr += 1
    to_write = [source, target, model_prediction, BLEU]
    writer.writerow(to_write)
    print(ctr)
data.close()
print(total/ctr)

# saving the model results
from google.colab import files
files.download('results.csv')
