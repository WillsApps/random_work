import torch
from trl import SFTTrainer
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_int8_training
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments

train_dataset = load_dataset("tatsu-lab/alpaca", split="train")
print(train_dataset)
rows = train_dataset.to_list()[0:10]
print(rows)
