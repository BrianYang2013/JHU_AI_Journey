# About this course

2023 Fall Seminar 

## Textbook

## Grade

1. 30%: Paper Presentations/Discussion Leadership
2. 30%: Preparation and Participation 
3. 40%: Course Project

# Course Topics

 1. Introduction: The Structure, Statistics, and Representation of Language
2. Introduction to the Modeling of Language
3. What Is Attention?
4. The Transformer: All You Need Is Attention
5. The First Large Language Models -- Finally, Good Text Generation!
6. GPT-3, Meta-Learning, and Prompting
7. Prompting, Continued
8. Composability and Chaining
9. ReAct -- Agentive LLM Systems
10. Types of Tuning
11. Efficiency Through Software
12. Efficiency Through Hardware
13. Final Projects Pt. I
14. Final Projects Pt. II

# Resources

## Courses: 

- [SP23 CS 601.471/671 NLP: Self-supervised Models](https://self-supervised.cs.jhu.edu/sp2023/)
- [FA22 CSCI 601.771: Self-supervised Statistical Models](https://self-supervised.cs.jhu.edu/fa2022/)
- [Standford: Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)

## Articles: 

- [What OpenAI Really Wants](https://www.wired.com/story/what-openai-really-wants/)
- [Richard S. Sutton - The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)

## Papers: 

### Before Transformer

2000: [A Neural Probabilistic Language Model](https://proceedings.neurips.cc/paper_files/paper/2000/file/728f206c2a01bf572b5940d7d9a8fa4c-Paper.pdf) - This paper has an alternative 2003 version 

2015: [From Feedforward to Recurrent LSTM Neural Networks for Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2000/file/728f206c2a01bf572b5940d7d9a8fa4c-Paper.pdf)

2016: [Building End-To-End Dialogue Systems Using Generative Hierarchical Neural Network Models](https://arxiv.org/pdf/1507.04808.pdf)

2015: [Generating Sentences from a Continuous Space](https://arxiv.org/pdf/1511.06349.pdf)

2014: [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf)

- [English-Japanese Neural Machine Translation with Encoder-Decoder-Reconstructor](https://syncedreview.com/2017/09/15/english-japanese-neural-machine-translation-with-encoder-decoder-reconstructor/)

2014: [Neural Turing Machines](https://arxiv.org/pdf/1410.5401.pdf)

2016: [Meta-Learning with Memory-Augmented Neural Networks](https://proceedings.mlr.press/v48/santoro16.pdf)

### Transformer era

#### **The Transformer + GPT2**

- [Attention is all you Need](https://arxiv.org/abs/1706.03762)
  - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  - [Visual Guide to Transformer Neural Networks - (Episode 1) Position Embeddings](https://www.youtube.com/watch?v=dichIcUZfOw)

- GPT-2 Paper: [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
  - [Better language models and their implications](https://openai.com/research/better-language-models)

- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) - Sampling

#### **Transformer Variants and Improvements**

- [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) 
- [REFORMER: THE EFFICIENT TRANSFORMER](https://arxiv.org/pdf/2001.04451.pdf) 
  - The original Google blog article on the [Reformer](https://blog.research.google/2020/01/reformer-efficient-transformer.html)
- [Big Bird](https://arxiv.org/pdf/2001.04451.pdf): Big Bird builds on previous work on sparse attention mechanisms, including local attention (also called [Sliding Window Attention](https://paperswithcode.com/method/sliding-window-attention) in the [Longformer: The Long-Document Transformer](https://paperswithcode.com/paper/longformer-the-long-document-transformer))
  - [Constructing Transformers For Longer Sequences with Sparse Attention Methods](https://blog.research.google/2021/03/constructing-transformers-for-longer.html): sparse attention mechanisms

#### **GPT-3 and Meta-Learning**

- GPT-3 Paper: [Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165.pdf)
- [Chinchilla (Training Compute-Optimal Large Language Models)](https://arxiv.org/abs/2203.15556): establishes the first empirical results about how much data you really need to train your LLM. Sometimes these are called the "Chinchilla scaling laws."

#### **Prompting and Composability**

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903): One of the early results in prompt engineering that has truly stood the test of time. 
  - [Prompt Engineering Papers List](https://www.promptingguide.ai/papers)
- [Ask Me Anything: A simple strategy for prompting language models](https://paperswithcode.com/paper/ask-me-anything-a-simple-strategy-for)
- [Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910)
  - [Composability in LLM Apps](https://betterprogramming.pub/composability-in-llm-apps-495f0f170874)

#### Composability and Chaining

- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)
- [Augmenting large language models with chemistry tools](https://arxiv.org/pdf/2304.05376.pdf)
- [Language Model Cascades](https://arxiv.org/abs/2207.10342)

#### **ReAct: Agentive LLM Systems**

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
  - [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) => Interesting
  - [AutoGPT](https://autogpt.net/) and [AutoGPT Github](https://github.com/Significant-Gravitas/AutoGPT)
- [PAL: Program-aided Language Models](https://proceedings.mlr.press/v202/gao23f.html)
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442): Standford town

#### Tuning

- [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652)
  - [Review — FLAN: Finetuned Language Models Are Zero-Shot Learners](https://sh-tsang.medium.com/review-flan-finetuned-language-models-are-zero-shot-learners-1a9249fdd296#:~:text=FLAN%2C%20A%20LLM%20Instruction%20Tuning%20Approach&text=Finetuned%20LAnguage%20Net%20(FLAN)%20is,of%20datasets%20described%20via%20instructions.): Review
  - [Introducing FLAN: More generalizable Language Models with Instruction Fine-Tuning](https://blog.research.google/2021/10/introducing-flan-more-generalizable.html): Original Google Blog
  - [Instruction Tuning for Large Language Models: A Survey](https://arxiv.org/pdf/2308.10792.pdf)

- [Training language models to follow instructions with human feedback](https://arxiv.org/pdf/2203.02155.pdf)
  - [Aligning language models to follow instructions](https://openai.com/research/instruction-following): Open AI blog
- [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)
  - [Prompt Tuning, Hard Prompts & Soft Prompts](https://cobusgreyling.medium.com/prompt-tuning-hard-prompts-soft-prompts-49740de6c64c#:~:text=Prompt%20tuning%20involves%20using%20a,%2Dengineered%20%E2%80%9Chard%E2%80%9D%20prompts.)
  - [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://aclanthology.org/2021.acl-long.353.pdf)
  - [Understanding Parameter-Efficient LLM Finetuning: Prompt Tuning And Prefix Tuning](https://magazine.sebastianraschka.com/p/understanding-parameter-efficient#:~:text=Prefix%20Versus%20Prompt%20Tuning&text=Prefix%20tuning%20modifies%20more%20layers,in%20fewer%20parameters%20being%20updated.)

- [LORA: LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2106.09685.pdf)

#### Reasoning And Other Miscellany

- [Towards Reasoning in Large Language Models: A Survey](https://aclanthology.org/2023.findings-acl.67.pdf)
  - [Remind Me Again Why Large Language Models Can’t Think](https://medium.com/the-modern-scientist/remind-me-again-why-large-language-models-cant-think-acab12da63de)
  - [Large Language Models: Reasoning Capabilities and Limitations](https://medium.com/@glovguy/large-language-models-reasoning-capabilities-and-limitations-951cee0ac642)
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)
- RAG: [When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories](https://arxiv.org/abs/2212.10511)

### More

- [Nougat: Neural Optical Understanding for Academic Documents](https://arxiv.org/pdf/2308.13418v1.pdf)
- [The ConceptARC Benchmark: Evaluating Understanding and Generalization in the ARC Domain](https://arxiv.org/pdf/2305.07141.pdf)
- [RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267)
- [Large language models are not zero-shot communicators](https://openreview.net/forum?id=WgbcOQMNXB)
- [Pragmatic Implicature Processing in ChatGPT](https://psyarxiv.com/qtbh9/)
- [Does GPT-3 Grasp Metaphors? Identifying Metaphor Mappings with Generative Language Models](https://aclanthology.org/2023.acl-long.58.pdf)
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071)
- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409): Take a deep breath and work step-by-step!
- [Large Language Model for Science: A Study on P vs. NP](https://arxiv.org/pdf/2309.05689.pdf)
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) => Interesting
- [From Sparse to Dense:GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/abs/2309.04269)
- [The Carbon Emissions of Writing and Illustrating Are Lower for AI than for Humans](https://arxiv.org/abs/2303.06219)
- [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://arxiv.org/pdf/2309.12288.pdf)
- [Retentive Network: A Successor to Transformer for Large Language Models](https://arxiv.org/pdf/2307.08621.pdf)
- [PROMPTBREEDER: SELF-REFERENTIAL SELF-IMPROVEMENT VIA PROMPT EVOLUTION](https://arxiv.org/pdf/2309.16797.pdf)
- [CONTRASTIVE PREFERENCE LEARNING: LEARNING FROM HUMAN FEEDBACK WITHOUT RL](https://arxiv.org/pdf/2310.13639.pdf)
- [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004)

## Misc: 

- [Anti-hype LLM reading list](https://gist.github.com/veekaybee/be375ab33085102f9027853128dc5f0e)
- Awesome
- Integrative complexity
- Psychometrics
- Tragedy of the commons
- [A Hackers' Guide to Language Models](https://www.youtube.com/watch?v=jkrNMKz9pWU)
- [promptimize](https://github.com/preset-io/promptimize)
- [Multi-modal prompt injection image attacks against GPT-4V](https://simonwillison.net/2023/Oct/14/multi-modal-prompt-injection/)
- [ollama](https://ollama.ai/) - Mistral-7B
- [New models and developer products announced at DevDay](https://openai.com/blog/new-models-and-developer-products-announced-at-devday)
- [Building LLM applications for production](https://huyenchip.com/2023/04/11/llm-engineering.html)
- [Block-Recurrent Transformer: LSTM and Transformer Combined](https://towardsdatascience.com/block-recurrent-transformer-lstm-and-transformer-combined-ec3e64af971a)
- [The Information Pathways Hypothesis: Transformers are Dynamic Self-Ensembles](https://arxiv.org/abs/2306.01705): Stochastically Subsampled self-Attention (SSA) – a general-purpose training strategy for transformers that can reduce both the memory and computational cost of self-attention by 4 to 8 times during training while also serving as a regularization method

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- [BERT](https://arxiv.org/abs/1810.04805)
- [Training Language Models to Follow Instructions](https://arxiv.org/abs/2203.02155)
- GPT:
  - Improving language understanding by generative pre-training
  - [Language Models are Unsupervised Multi-Task Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
  - [Language models are few-shot learners](https://arxiv.org/abs/2005.14165)
