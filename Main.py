
from preprocess.extract import getDataInDataframe
from simpletransformers.classification import ClassificationModel
import pandas as pd


print('starting process')
data = getDataInDataframe()

print('assigning data')
train_df = data
eval_df = data

print('initializing model')
model = ClassificationModel('bert','bert-base-cased',num_labels=5,args={'reprocess_input_data': True, 'overwrite_output_dir':True})


print('training model')
model.train_model(train_df)

print('evaluating model')
result, model_outputs, wrong_predictions = model.eval_model(eval_df)

print('testPrediction')
prediction,raw_outputs = model.predict(['testSentecne'])








