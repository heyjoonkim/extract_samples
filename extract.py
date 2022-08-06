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
    parser.add_argument(
        "--seed", 
        type=int, 
        default=100, 
        help="A seed for reproducible training."
    )
    parser.add_argument(
        "--n_samples", 
        type=int, 
        default=0, 
        help="Number of samples for in-context learning."
    )
    # for balanced sampling
    parser.add_argument(
        '--balance', 
        default=False, 
        action="store_true",
        help='Balance samples per label for in-context learning.'
    )
    # sample per class
    parser.add_argument(
        '--per_class', 
        default=False, 
        action="store_true",
        help='Sample per class.'
    )
    args = parser.parse_args() 

    return args


def main():
    args = parse_args()

    stats = dict()
    stats['task_name'] = args.task_name
    stats['benchmark_name'] = args.benchmark_name
    stats['seed'] = args.seed
    stats['n_samples'] = args.n_samples
    stats['balance'] = args.balance
    stats['per_class'] = args.per_class

    print(f'TASK : {args.benchmark_name}-{args.task_name}')
    print(f'Generate dataset samples to path : {args.output_dir}')
    # mkdir output directory to save logs and configs.
    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    print(f'Set seed to {args.seed}')
    # set random seet to 1 to sample same train/validation set 
    set_seed(args.seed)
    random.seed(args.seed)

    # key for input sentence
    keys_dict = task_to_keys.get(args.task_name)
    sentence1_key, sentence2_key = keys_dict.get('input')
    label_key = keys_dict.get('label')

    # load dataset
    if args.benchmark_name == 'huggingface':
        train_dataset = load_dataset(args.task_name, split='train')
    else:
        # GLUE, SuperGLUE, tweet_eval
        train_dataset = load_dataset(args.benchmark_name, args.task_name, split='train')
    print(f'Loaded {len(train_dataset)} train samples')
    num_class = len(set(train_dataset[label_key]))
    print(f'NUM CLASS : {num_class}')
    
    train_dataset = [sample for sample in train_dataset]

    selected_samples = []
    if args.per_class:
        total_samples = num_class * args.n_samples
        print(f'Load samples per class : {num_class} class * {args.n_samples} samples = {total_samples} samples')
        for class_index in range(num_class):
            samples_per_class = list(filter(lambda sample : sample[label_key] == class_index, train_dataset))
            num_samples_per_class = len(samples_per_class)
            print(f'CLASS {class_index} : {num_samples_per_class} samples => {args.n_samples} samples')
            random_indices = random.sample(range(num_samples_per_class), args.n_samples)
            for random_index in random_indices:
                selected_samples.append(samples_per_class[random_index])

        assert len(selected_samples) == total_samples, f'{len(selected_samples)} != {total_samples}'
        print(f'Selected {len(selected_samples)} samples. Done.')
    else:
        print(f'Load samples : {args.n_samples} samples')

        random_indices = random.sample(range(len(train_dataset)), args.n_samples)
        for random_index in random_indices:
            selected_samples.append(train_dataset[random_index])

        assert len(selected_samples) == args.n_samples, f'{len(selected_samples)} != {args.n_samples}'
        print(f'Selected {len(selected_samples)} samples. Done.')


    stats_dict = dict()
    for selected_sample in selected_samples:
        selected_label = selected_sample[label_key]
        stats_dict[selected_label] = stats_dict.get(selected_label, 0) + 1
    print(f'\n\nStats : {stats_dict}')

    # write to output file
    train_path = os.path.join(args.output_dir, 'train.jsonl')
    with open(train_path, 'w') as output_file:
        for selected_sample in selected_samples:
            output_file.write(json.dumps(selected_sample, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    print('Selecting samples....')
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Total runtime : {end_time - start_time} sec.')