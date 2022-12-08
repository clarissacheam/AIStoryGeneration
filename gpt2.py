## -- Run using colab
## -- Each # comment is a section


# install gpt2 and tensorflow-gpu
!pip install gpt-2-simple
!pip install tensorflow-gpu


# imports
import nltk
import os
import csv
import pandas as pd
import gpt_2_simple as gpt2
from tqdm import tqdm_notebook as tqdm
from dataclasses import dataclass


# data processing
data = ["train", "test", "valid"]

TARGET_DIR = 'working/'
target_data = [TARGET_DIR+"train", TARGET_DIR+"test", TARGET_DIR+"valid"]

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
# !head working/train.wp_combined
# !head working/test.wp_combined
# !head working/valid.wp_combined


# Model training
model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

sess = gpt2.start_tf_sess()
gpt2.finetune(sess, 'working/train.wp_combined', model_name=model_name, 
              steps=200, )

gpt2.generate(sess)


# creating the validation/dev set as a csv for evaluation
valid_data = pd.read_csv("working/valid.wp_combined", 
                         names=['source_text', 'target_text'], 
                         header=None,
                         delimiter="<CLS>")

valid_data.shape


# evaluation
total = 0
ctr = 0

data = open('gpt2_results.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(data)
writer.writerow(['prompt', 'original story', 'model story', 'BLEU score'])
for source, target in zip(valid_data['source_text'], \
                          valid_data['target_text']):
    sess = gpt2.reset_session(sess)
    gpt2.load_gpt2(sess)
    model_prediction = gpt2.generate(sess, prefix=source + ' <CLS>', 
                                     truncate="\n", return_as_list=True)[0]
    model_prediction = model_prediction.replace(source + ' <CLS> ', '')
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
files.download('gpt2_results.csv')
