### Local Setup
**Install dependencies**
```
pip install -r requirements.txt
```
If bitsandbytes doesn't work, install it from source. Windows users can follow these instructions.

### Training (finetune.py)

First, you may need to set the `templates/inters.json` to the templates you need, don't forget to confirm😆.

This file contains a straightforward application of PEFT to the LLaMA model, as well as some code related to prompt construction and tokenization. PRs adapting this code to support larger models are always welcome.

Example usage:
```
python finetune.py \
    --base_model 'meta-llama/Llama-2-7b-chat-hf'
```
We can also tweak our hyperparameters:
```
python finetune.py \
    --base_model 'meta-llama/Llama-2-7b-chat-hf' \
    --output_dir './lora-inters' \
    --batch_size 128 \
    --micro_batch_size 4 \
    --num_epochs 3 \
    --learning_rate 1e-4 \
    --cutoff_len 512 \
    --val_set_size 2000 \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules '[q_proj,v_proj]' \
    --train_on_inputs \
    --group_by_length
```

### Generate (generate.py)
```bash
python generate.py --base_model='huggyllama/llama-7b'
```

## Credits

This project borrowed some code from the following sources:

* [alpaca-lora](https://github.com/tloen/alpaca-lora)

We're grateful to the authors for their wonderful work.
