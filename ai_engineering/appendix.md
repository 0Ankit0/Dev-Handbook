# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Mathematical Quick Reference

### Gradient Descent and Optimization

```text
Parameter update rule:
  θ = θ - α · ∇L(θ)

Where:
  θ   = model parameters (weights and biases)
  α   = learning rate (step size)
  ∇L  = gradient of loss function with respect to θ
```

**Key optimizers compared:**

| Optimizer | Update Rule (simplified) | Characteristics |
|-----------|--------------------------|-----------------|
| SGD | `θ = θ - α · g` | Simple; sensitive to learning rate |
| SGD + Momentum | `v = βv + g; θ = θ - α·v` | Smooths gradient noise; faster convergence |
| AdaGrad | `θ = θ - α/√(G+ε) · g` | Adaptive per-parameter LR; LR decays over time |
| RMSProp | `θ = θ - α/√(E[g²]+ε) · g` | Fixes AdaGrad's LR decay; good for RNNs |
| Adam | Combines Momentum + RMSProp | Most commonly used; robust defaults |
| AdamW | Adam + weight decay decoupled | Better generalization; preferred over Adam |

### Activation Functions

| Function | Formula | Range | Used In |
|----------|---------|-------|---------|
| ReLU | `max(0, x)` | [0, ∞) | Hidden layers (default) |
| Leaky ReLU | `max(0.01x, x)` | (-∞, ∞) | When dying ReLU is a problem |
| Sigmoid | `1/(1+e^-x)` | (0, 1) | Binary classification output |
| Softmax | `e^xᵢ / Σe^xⱼ` | (0, 1), sum=1 | Multi-class output layer |
| Tanh | `(e^x - e^-x)/(e^x + e^-x)` | (-1, 1) | RNNs, normalized hidden layers |
| GELU | `x·Φ(x)` | approx ReLU | Transformers (BERT, GPT) |

### Loss Functions

| Loss | Use Case | Formula (simplified) |
|------|----------|----------------------|
| MSE (Mean Squared Error) | Regression | `(1/n) Σ(y - ŷ)²` |
| MAE (Mean Absolute Error) | Regression (robust to outliers) | `(1/n) Σ|y - ŷ|` |
| Binary Cross-Entropy | Binary classification | `-[y·log(ŷ) + (1-y)·log(1-ŷ)]` |
| Categorical Cross-Entropy | Multi-class classification | `-Σ y·log(ŷ)` |
| Huber Loss | Regression (combines MSE+MAE) | Quadratic near 0, linear for large errors |

---

## Appendix B: PyTorch Quick Reference

### Model Definition

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
```

### Training Loop

```python
model = MLP(input_dim=784, hidden_dim=256, output_dim=10)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
criterion = nn.CrossEntropyLoss()

# Training
model.train()
for batch_x, batch_y in train_loader:
    optimizer.zero_grad()           # clear gradients from previous step
    logits = model(batch_x)        # forward pass
    loss = criterion(logits, batch_y)  # compute loss
    loss.backward()                 # compute gradients (backprop)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # gradient clipping
    optimizer.step()               # update parameters

# Evaluation
model.eval()
with torch.no_grad():              # disable gradient tracking (saves memory)
    for batch_x, batch_y in val_loader:
        logits = model(batch_x)
        preds = logits.argmax(dim=-1)
        # compute metrics...
```

### Useful Tensor Operations

```python
import torch

# Shape manipulation
x = torch.randn(32, 10)       # batch=32, features=10
x.shape                        # torch.Size([32, 10])
x.view(32, 2, 5)               # reshape
x.unsqueeze(0)                 # add dim → [1, 32, 10]
x.squeeze(0)                   # remove dim
x.permute(1, 0)                # transpose → [10, 32]

# Device movement
device = 'cuda' if torch.cuda.is_available() else 'cpu'
x = x.to(device)
model = model.to(device)

# Gradient control
x.requires_grad_(True)         # track gradients
with torch.no_grad(): ...      # no gradients (inference)

# Common ops
torch.cat([a, b], dim=0)       # concatenate
torch.stack([a, b], dim=0)     # stack (adds new dim)
torch.argmax(x, dim=-1)        # index of max value
torch.softmax(x, dim=-1)       # softmax probabilities
```

---

## Appendix C: Evaluation Metrics Quick Reference

### Classification

| Metric | Formula | When to Use |
|--------|---------|-------------|
| Accuracy | `(TP+TN)/(TP+TN+FP+FN)` | Balanced classes |
| Precision | `TP/(TP+FP)` | When false positives are costly (spam filter) |
| Recall | `TP/(TP+FN)` | When false negatives are costly (cancer detection) |
| F1 Score | `2·(P·R)/(P+R)` | Imbalanced classes, balanced precision/recall |
| AUC-ROC | Area under ROC curve | Ranking quality, threshold-independent |
| PR-AUC | Area under PR curve | Imbalanced datasets (rare positives) |

### Regression

| Metric | Formula | Notes |
|--------|---------|-------|
| MSE | `mean((y - ŷ)²)` | Penalizes large errors heavily |
| RMSE | `√MSE` | Same units as target |
| MAE | `mean(|y - ŷ|)` | Robust to outliers |
| R² | `1 - SS_res/SS_tot` | 1.0 = perfect; negative = worse than mean |
| MAPE | `mean(|y-ŷ|/|y|)·100` | Percentage error; fails when y≈0 |

### NLP / Generation

| Metric | What It Measures |
|--------|-----------------|
| BLEU | N-gram overlap between generated and reference text (translation) |
| ROUGE-L | Longest common subsequence overlap (summarization) |
| Perplexity | How well a language model predicts a sample (lower = better) |
| BERTScore | Semantic similarity using BERT embeddings |

---

## Appendix D: MLOps Glossary

**Feature Store**
A centralized repository for storing, versioning, and serving features (computed inputs) for ML models. Ensures consistency between training and serving — the same feature computation runs in both. Examples: Feast, Tecton, Vertex AI Feature Store.

**Model Registry**
A system for versioning, staging, and promoting ML models. Similar to a package registry for code. Tracks model metadata, metrics, and deployment status. Examples: MLflow Model Registry, W&B Artifacts.

**Data Drift**
When the statistical distribution of input data in production shifts compared to what the model was trained on. Causes model performance to degrade over time. Detected by monitoring feature distributions in production.

**Concept Drift**
When the underlying relationship between input features and the target variable changes over time (e.g., user behavior patterns shift). Harder to detect than data drift since it requires monitoring output quality.

**Training-Serving Skew**
When features are computed differently at training time vs. serving time, leading to degraded production performance. The feature store pattern is designed to eliminate this.

**Shadow Deployment**
Running a new model in parallel with the current production model without actually serving its predictions to users. Used to compare real-world behavior before promoting.

**Canary Deployment**
Gradually routing a small percentage of traffic to a new model while keeping most traffic on the old model. Allows real-world validation with limited risk.

**A/B Testing (ML)**
Splitting users into groups and serving different model versions to each. Statistical analysis determines which model performs better on business metrics.

**RLHF (Reinforcement Learning from Human Feedback)**
A technique used to align language models with human preferences. A reward model is trained on human comparisons, then used to fine-tune the LLM with RL. Used in ChatGPT, Claude, etc.

**RAG (Retrieval-Augmented Generation)**
A pattern for grounding language model outputs in retrieved documents. Instead of relying on parametric memory alone, the model retrieves relevant documents at inference time and includes them in the context.

**Quantization**
Reducing model weight precision from FP32 to INT8 or INT4 to reduce memory and speed up inference. Trades a small amount of accuracy for significant efficiency gains. Common for LLM deployment.

**LoRA (Low-Rank Adaptation)**
A parameter-efficient fine-tuning technique. Instead of fine-tuning all model weights, small low-rank matrices are added to certain layers. Dramatically reduces memory and compute requirements for fine-tuning large models.

---

## Appendix E: Resources

### Foundational ML
- [fast.ai Practical Deep Learning](https://course.fast.ai/) — top-down practical approach
- [deeplearning.ai Specializations](https://www.coursera.org/deeplearning-ai) — comprehensive ML curriculum
- *Deep Learning* — Goodfellow, Bengio, Courville (free online)

### LLMs and GenAI
- [Hugging Face Course](https://huggingface.co/learn/nlp-course/) — transformers and NLP
- [LangChain Docs](https://docs.langchain.com/) — LLM application framework
- [LlamaIndex Docs](https://docs.llamaindex.ai/) — RAG and knowledge bases

### MLOps
- [MLflow Docs](https://mlflow.org/docs/latest/) — experiment tracking and model registry
- [Weights & Biases Docs](https://docs.wandb.ai/) — experiment visualization
- [Evidently AI](https://docs.evidentlyai.com/) — model monitoring and drift detection

### Papers
- Attention Is All You Need (Transformer architecture)
- BERT: Pre-training of Deep Bidirectional Transformers
- GPT-3: Language Models are Few-Shot Learners
- LoRA: Low-Rank Adaptation of Large Language Models
