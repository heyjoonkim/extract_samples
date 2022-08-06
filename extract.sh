

benchmark_name='huggingface'
task_name='banking77'
n_samples='3'
seeds='1'

for seed in $seeds; do
    python extract.py \
        --task_name $task_name \
        --benchmark_name $benchmark_name \
        --seed $seed \
        --output_dir ./$benchmark_name-$task_name-$n_samples-$seed \
        --n_samples $n_samples \
        --per_class
done