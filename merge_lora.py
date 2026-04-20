"""
合并 LoRA 权重到基座模型并导出

使用方法:
python merge_lora.py --lora_path ./neil_invest_lora/lora_model --output ./neil_invest_merged
"""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

def merge_and_export(lora_path, output_path):
    print(f"Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        "unsloth/Qwen2.5-7B-Instruct",
        torch_dtype = torch.bfloat16,
        device_map = "auto",
    )
    
    print(f"Loading LoRA adapter from {lora_path}...")
    model = PeftModel.from_pretrained(base_model, lora_path)
    
    print("Merging LoRA weights...")
    model = model.merge_and_unload()
    
    print(f"Saving merged model to {output_path}...")
    model.save_pretrained(output_path)
    
    print("Saving tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen2.5-7B-Instruct")
    tokenizer.save_pretrained(output_path)
    
    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lora_path", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    
    merge_and_export(args.lora_path, args.output)
