"""
NEIL-value invest LoRA Fine-tune 训练脚本
基于 Qwen2.5-7B-Instruct，使用 Unsloth 加速

使用方法:
1. 在 Google Colab (T4 GPU) 或本地 GPU 机器上运行
2. 准备好你自己的投资笔记数据 JSONL 文件
3. 修改下面的 DATA_PATH 为你的数据路径
4. 运行全部单元格

预计训练时间 (Qwen2.5-7B + 100条数据):
- T4 GPU: ~30-60 分钟
- A100: ~10-20 分钟
"""

# ============================================================
# Step 1: 安装依赖
# ============================================================
# !pip install "unsloth[colab] @ git+https://github.com/unslothai/unsloth.git"
# !pip install --no-deps trl peft accelerate bitsandbytes
# !pip install torch --index-url https://download.pytorch.org/whl/cu121  # 如果用 GPU

# ============================================================
# Step 2: 导入
# ============================================================
from unsloth import FastLanguageModel
import torch
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth.chat_templates import get_chat_template
import os

# ============================================================
# Step 3: 配置参数
# ============================================================
max_seq_length = 2048
dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
load_in_4bit = True

# 数据路径 - 改成你自己的 JSONL 文件
DATA_PATH = "data/neil_invest_train.jsonl"

# 输出目录
OUTPUT_DIR = "./neil_invest_lora"

# ============================================================
# Step 4: 加载模型
# ============================================================
print("Loading model...")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen2.5-7B-Instruct-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# ============================================================
# Step 5: 添加 LoRA 适配器
# ============================================================
print("Adding LoRA adapters...")

model = FastLanguageModel.get_peft_model(
    model,
    r = 32,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 64,
    lora_dropout = 0.05,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
)

# ============================================================
# Step 6: 格式化数据
# ============================================================
print("Formatting data...")

def formatting_prompts_func(examples):
    """将数据格式化为对话格式"""
    conversations = examples["conversations"]
    texts = []
    for conv in conversations:
        text = tokenizer.apply_chat_template(
            conv, tokenize=False, add_generation_prompt=False
        )
        texts.append(text)
    return {"text": texts}

# ============================================================
# Step 7: 开始训练
# ============================================================
print("Starting training...")

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = ...,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = True,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_ratio = 0.1,
        num_train_epochs = 3,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 10,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 42,
        output_dir = OUTPUT_DIR,
        report_to = "none",
    ),
)

trainer.train()

# ============================================================
# Step 8: 保存模型
# ============================================================
print(f"Saving to {OUTPUT_DIR}...")
model.save_pretrained(f"{OUTPUT_DIR}/lora_model")
tokenizer.save_pretrained(f"{OUTPUT_DIR}/lora_model")

print("Done! To merge and export:")
print(f"  python merge_lora.py --lora_path {OUTPUT_DIR}/lora_model --output {OUTPUT_DIR}/merged_model")
