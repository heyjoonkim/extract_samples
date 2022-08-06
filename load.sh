

benchmark_name='huggingface'
task_name='ag_news'
n_samples='3'
seeds='1'

for seed in $seeds; do
    python load.py \
        --task_name $task_name \
        --benchmark_name $benchmark_name \
        --output_dir ./$benchmark_name-$task_name-$n_samples-$seed \
        # --per_class
done