# Appendices

## Appendix A: Mathematical Reference

### A.1 Matrix Calculus Cheat Sheet
- Gradient identities for linear layers, softmax, and cross-entropy.
- Jacobian/Hessian intuition and when second-order approximations matter.
- Shape-check rules to prevent silent broadcasting bugs.

### A.2 Probability Distributions Reference
- Core distributions (Bernoulli, Binomial, Gaussian, Poisson, Categorical).
- Practical usage: classification likelihoods, count modeling, uncertainty estimates.
- Parameter estimation notes (MLE/MAP) and calibration implications.

### A.3 Optimization Convergence Proofs
- Convex vs non-convex assumptions and convergence guarantees.
- SGD, Momentum, Adam/AdamW behavior under noisy gradients.
- Learning-rate schedules and stability criteria.

### A.4 Information Theory Basics
- Entropy, cross-entropy, KL divergence, mutual information.
- Why KL appears in VAEs, distillation, and policy optimization.
- Metrics interpretation pitfalls in model evaluation.

## Appendix B: Tools & Environment Setup

### B.1 GPU Setup: CUDA, cuDNN, NVIDIA Drivers
- Driver/CUDA/cuDNN compatibility matrix documentation.
- Reproducible environment provisioning for Linux/Windows/WSL.
- Validation commands for GPU visibility and compute capability.

### B.2 Cloud Platforms
- AWS/GCP/Azure starter blueprints for training, serving, and artifact storage.
- IAM least-privilege patterns for data/model access.
- Cost controls: quotas, auto-shutdown, and budget alerts.

### B.3 Local Development
- Dockerized ML dev containers and pinned dependencies.
- JupyterLab/VS Code setup with linting, formatting, type checks.
- Secrets management and local mock-service strategy.

### B.4 Hardware Guide
- Workstation vs cloud trade-offs by workload profile.
- Memory, VRAM, bandwidth planning for dataset/model sizes.
- Multi-GPU distributed training readiness checklist.

## Appendix C: Datasets & Benchmarks

### C.1 Classic ML Datasets
- UCI/OpenML/Kaggle dataset suitability and caveats.
- Licensing, redistribution, and privacy/compliance checks.

### C.2 Vision Datasets
- ImageNet/COCO/CIFAR evaluation conventions.
- Train/val/test split hygiene and leakage prevention.

### C.3 NLP Datasets
- GLUE/SuperGLUE/Common Crawl usage and preprocessing notes.
- Tokenization consistency and benchmark comparability.

### C.4 RL Environments
- Gym/Gymnasium/MuJoCo environment reproducibility.
- Seed control and statistically valid evaluation protocols.

### C.5 Benchmarking
- MLPerf/HELM-style reporting standards.
- Required reporting: latency, throughput, quality, cost-per-inference.

## Appendix D: Cheat Sheets & Quick Reference

### D.1 PyTorch vs TensorFlow API Mapping
- Equivalent APIs for data pipelines, model definitions, and training loops.
- Debugging/performance tooling equivalents.

### D.2 Regular Expressions for NLP
- Token extraction, normalization, and safe pattern usage.
- Unicode and locale edge cases.

### D.3 SQL for Data Scientists
- Feature extraction query patterns and anti-patterns.
- Window functions for temporal features.

### D.4 Big-O Complexity for ML Algorithms
- Training/inference complexity for common model families.
- Practical scaling bottlenecks (memory, I/O, communication).

### D.5 Git Commands for ML Projects
- Branching strategy for experiment-heavy workflows.
- Artifact/versioning conventions for models and datasets.

## Appendix E: Glossary of Terms
- End-to-end glossary from data ingestion to production inference.
- Includes MLOps, GenAI, evaluation, governance, and safety terminology.
