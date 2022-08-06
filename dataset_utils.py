task_to_keys = {
    # SINGLE SENTENCE TASKS
    # GLUE
    "cola" :  {
        'input' : ("sentence", None),
        'label' : 'label'
    },
    "sst2": {
        'input' : ("sentence", None),     # #labels = 2
        'label' : 'label',
    },
    "trec":  {
        'input' : ("text", None),         # #labels = 6
        'label' : 'label-coarse'
    },
    # tweet_eval
    "hate" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "stance_atheism" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "emotion" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "sentiment" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "offensive" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "imdb" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "rotten_tomatoes" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "yelp_review_full" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "ag_news": {
        'input' : ("text", None),      # #labels = 4
        'label' : 'label',
    },
    "hate_speech18" :  {
        'input' : ("text", None),
        'label' : 'label'
    },
    "mr" :  {
        'input' : ("sentence1", None),
        'label' : 'label'
    },
    "cr" :  {
        'input' : ("sentence1", None),
        'label' : 'label'
    },
    "plus" :  {
        'input' : ("text", None),
        'label' : 'intent'
    },
    "banking77" :  {
        'input' : ("text", None),
        'label' : 'label'
    },

    # SENTENCE PAIR TASKS
    # glue
    "mnli":  {
        'input' : ("premise", "hypothesis"),
        'label' : 'label',
    },
    "mrpc":  {
        'input' : ("sentence1", "sentence2"),
        'label' : 'label',
    },
    "qnli":  {
        'input' : ("question", "sentence"),
        'label' : 'label',
    },
    "qqp":  {
        'input' : ("question1", "question2"),
        'label' : 'label',
    },
    "rte":  {
        'input' : ("sentence1", "sentence2"),
        'label' : 'label'
    },
    "wnli":  {
        'input' : ("sentence1", "sentence2"),
        'label' : 'label'
    },
    # super_glue
    "boolq" :  {
        'input' : ("question", "passage"),
        'label' : 'label'
    },
    "cb" :  {
        'input' : ("premise", "hypothesis"),
        'label' : 'label'
    },
    "multirc" :  {
        'input' : ("paragraph", "question"),
        'label' : 'label'
    },
    # others
    "sick" :  {
        'input' : ("sentence_A", "sentence_B"),
        'label' : 'label'
    },
    "snli" :  {
        'input' : ("premise", "hypothesis"),
        'label' : 'label'
    },
}