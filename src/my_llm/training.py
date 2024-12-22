from datasets import load_dataset

train_dataset = load_dataset("tatsu-lab/alpaca", split="train")
print(train_dataset)
rows = train_dataset.to_list()[0:10]
print(rows)
