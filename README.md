# 원하는 크기의 few-shot dataset 추출하기

### 1. 샘플 추출하기

Train dataset을 로드해서 지정한 샘플 수 만큼 랜덤하게 샘플 추출.

기본적으로 <code>n_samples</code> 개의 샘플을 랜덤하게 추출함. (label balance 무관, 순서 무관, 랜덤하게 총 <code>n_samples</code> 개수 만큼 뽑아냄)

<code>--per_class</code> 옵션을 같이 주면 각 클래스 마다 <code>n_samples</code> 개 만큼의 샘플을 뽑음.

예를들어, <code>banking77</code> 의 경우 77개의 클래스가 있는데, <code>n_samples=3</code>으로 주는 경우 <code>77*3=231</code> 개의 샘플을 뽑음. (현재 실험 세팅에 적합)

뽑아낸 샘플들은 <code>benchmark_name-task_name-n_samples-seed</code> 디렉토리에 <code>train.jsonl</code> 파일로 저장됨. 
(파일이 저장되는 위치는 스크립트에서 변경할 수 있는데, 파일명을 변경하려면 코드에서 수정해야 함. Line 140)

<code>.jsonl</code> 파일은 <code>extract.py</code> 에서 짜둔대로 읽어올 수 있음. (2번 참고)

<code>extract.sh</code> 파일에서 원하는 파라미터만 바꿔주면 됨. (<code>benchmark_name</code>, <code>task_name</code>, <code>n_samples</code>, <code>seeds</code>) 
<code>benchmark_name</code>, <code>task_name</code>은 기존에 사용하던 코드와 동일하게 입력해주면 됨 (huggingface, glue, super_glue 등)


---


### 2. 샘플 읽어오기

1번에서 데이터 저장한 디렉토리에서 <code>train.jsonl</code> 파일 읽어옴,

datasets에서 이미 <code>.jsonl</code> 파일을 읽어오는걸 구현해둬서 그냥 <code>load.py</code> 에 있는 코드를 복사해서 train data 로드하는 부분에 붙여넣기만 하면 될 듯.

<code>load.sh</code>로 한 번 로드해볼 수 있음.

---

### TODO : clinc에서 OOD에 해당하는 index를 제외해서 처리하게 짜야하는데, 아직 그거까진 구현 X
