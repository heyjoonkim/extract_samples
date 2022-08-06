import argparse
import os
import random
import time
import json

from datasets import load_dataset
from tqdm.auto import tqdm

from transformers import (
    set_seed,
)

from dataset_utils import task_to_keys

def parse_args():
    parser = argparse.ArgumentParser(description="Finetune a transformers model on a text classification task")
    parser.add_argument(
        "--task_name",
        type=str,
        default=None,
        help="The name of the task to generate few-shot.",
        choices=list(task_to_keys.keys())
    )
    parser.add_argument(
        "--benchmark_name",
        type=str,
        default=None,
        help="The name of the benchmark to generate few-shot.",
        choices=['glue', 'super_glue', 'huggingface', 'tweet_eval', 'clinc'],
    )
    parser.add_argument(
        "--output_dir", 
        type=str, 
        default=None, 
        help="Where to store the final model."
    )
    args = parser.parse_args() 

    return args


def main():
    args = parse_args()

    print(f'TASK : {args.benchmark_name}-{args.task_name}')
    print(f'Load .jsonl file from : {args.output_dir}')
    # mkdir output directory to save logs and configs.
    if not os.path.isdir(args.output_dir):
        print(f'Path {args.output_dir} does not exist.')
        exit()

    # load dataset
    data_file = os.path.join(args.output_dir, 'train.jsonl')
    train_dataset = load_dataset('json', data_files=data_file)['train']

    print(f'Done loading dataset : {len(train_dataset)} samples')

    for index, sample in enumerate(train_dataset):
        print('index', index, sample)
    

if __name__ == "__main__":
    print('Loading samples....')
    main()