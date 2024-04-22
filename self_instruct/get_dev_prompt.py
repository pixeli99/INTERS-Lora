import json
from datasets import load_dataset

def main(
    data_file: str = "dev-qu-du-zero-shot/query_clarification_clariq_fkw.zero_shot.dev.jsonl",
    prompt_file: str = "ir_instruct_dataset.json",
):
    # Load dataset and extract prompts
    dataset = load_dataset("yutaozhu94/INTERS", data_files={"dev": [data_file]})
    prompts = [item['prompt'] for item in dataset['dev']]

    # Write prompts to JSON file
    with open(prompt_file, "w") as f:
        json.dump(prompts, f, indent=2)

if __name__ == "__main__":
    main()
