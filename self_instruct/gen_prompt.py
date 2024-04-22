import json
import random

# define task
tasks = {
    "Query Understanding": ["Query Intent Classification", "Query Relevance Judgment"],
    "Document Understanding": ["Document Summarization", "Keyword Extraction"],
    "Query-Document Relationship Understanding": ["Document Ranking", "Query-Document Relevance Matching"]
}

# define task prompt, follow INTERS
task_description = "The query description task aims at describing documents potentially relevant to a user-provided query. Queries typically comprise keywords reflecting the user's information needs. The objective of the task is to describe the characteristics and content of documents that would be considered relevant to the queries, aiding in the understanding and retrieval of relevant information."

# templates
templates = {
    "Query Intent Classification": "Describe the search intent of the given query \"[Q]\".",
    "Query Relevance Judgment": "Referring to this description that describes the documents relevant to a query: [D], please infer the corresponding query.",
    "Document Summarization": "Summarize the key information in the following document: [D]",
    "Keyword Extraction": "Extract the most important keywords from the following document: [D]",
    "Document Ranking": "Given the query \"[Q]\", rank the following documents in order of relevance: [D1], [D2], [D3]",
    "Query-Document Relevance Matching": "Determine if the document [D] is relevant to the query \"[Q]\"."
}

# few examples
examples = {
    "Query": ["wetlands wastewater treatment", "History of Physicians in America", "Federal welfare reform"],
    "Document": [
        "Wetlands wastewater treatment projects purposely integrate wetlands to act as final filters for wastewater. The project must be named or geographically located, more precisely than simply the state in which it resides.",
        "The history of physicians in America is relevant. Native American practitioners would not be relevant. Women who knew herbs and practiced midwifery would be relevant. Mention of \"doctor\" would be relevant if he/she is considered to be a doctor by other people.",
        "Relevant documents will provide information on efforts to reform U.S. federal welfare programs. Of particular relevance are reform efforts undertaken by the federal government, as opposed to state or local efforts."
    ]
}

##### Uncomment to read from file #####

# Load example data from files
# def load_examples(file_path):
#     with open(file_path, "r") as f:
#         return f.read().splitlines()

# examples = {
#     "Query": load_examples("queries.txt"),
#     "Document": load_examples("documents.txt")
# }


def generate_prompt(task, template, examples):
    prompt = f"{task_description}\n\n{task}: {template}\n\nResult: "
    
    # random choice
    if "[Q]" in template:
        query = random.choice(examples["Query"])
        prompt = prompt.replace("[Q]", query)
    if "[D]" in template:
        doc = random.choice(examples["Document"])
        prompt = prompt.replace("[D]", doc)
    
    return prompt


dataset = []
for category, subtasks in tasks.items():
    for subtask in subtasks:
        for i in range(5):  # for each subtask, we gen 5 prompts
            prompt = generate_prompt(subtask, templates[subtask], examples)
            dataset.append(prompt)

# write the results
with open("ir_instruct_dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
