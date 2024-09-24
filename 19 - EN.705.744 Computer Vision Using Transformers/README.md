# About this course

## Course Summary

## Textbook

- N/A

- Reference:

  - Foundations of Statistical Natural Language Processing. Manning, C. D. & Schutze H. ISBN-10: ‎ 0262133601.
  - Modern Computer Vision with PyTorch: Explore Deep Learning Concepts and Implement Over 50 Real-World Image Applications. Ayyadevara, V. K. & Reddy, Y. ISBN-10: 1839213477.
  - Deep Learning with PyTorch: Build, train, and tune neural networks using Python tools. Stevens, E., Antiga, L., & Viehmann, T. ISBN-10:1617295264.
  - Deep Learning. Goodfellow I., Bengio Y., & Courville A. ISBN-10: ‎ 0262035618.
  - Official PyTorch Tutorials: https://pytorch.org/tutorials/


## Software

- PyTorch: Install PyTorch to Local Machines, Use PyTorch from Google Colab Notebook, Use PyTorch on GPU servers. 

## Technical

- Python machine learning and data science libraries, including but not limited to, NumPy, Pandas, MatplotLib, Scipy, Scikit-Learn, and others.
- Elementary single/multivariable calculus, including partial derivatives and vector calculus.
- Basic linear algebra, including matrix operations, decompositions, and eigenvectors. 
- Fundamental probability and statistics, including common discrete/continuous random variables, statistical distributions, expectation, variance, sampling, estimation. 
- Some machine learning basics, including training versus testing, learning taxonomy such as supervised versus unsupervised, classification versus regression, etc. Previous experience with deep learning would be helpful but not required, tensors, datasets/dataloaders, data augmentation, back-propagation, optimizers, loss functions, and fully connected neural networks etc.

# Course Topics

- Overview of Transformer Networks
- Transformers in Computer Vision
- Transformers in Image Classification: ViT
- Transformers as General-Purpose Visual Backbones: Swin Transformer
- Transformers in Object Detection Part I: DETR
- Transformers in Object Detection Part II: Deformable DETR
- Transformers in Semantic Segmentation Part I: SETR
- Transformers in Semantic Segmentation Part II: MaskFormer
- Transformers in Video Understanding Part I: ViViT
- Transformers in Video Understanding Part II: VisTR
- Transformers in Self-Supervised Learning: DINO
- Contrastive Learning and Mask Image Modeling: MAE and SimMIM
- Transformers in Multimodal Learning: CLIP
- Large-scale Pre-training of Foundation Models in the Transformer Era

# Check List

- [x] Syllabus
- [x] Course Outline
- [ ] Assignment 1 
- [ ] Assignment 2
- [ ] Assignment 3 
- [ ] Assignment 4 
- [ ] Assignment 5 
- [ ] Assignment 6 
- [ ] Final Project

# Grading

## Grading Policy

- Assignment 60%
  - Qualitative assignments: All parts of question are addressed; Writing Quality/ Rationale/ Examples/ Outside References [rich in content; full of thought, insight, and analysis].
    - Each part of question is answered (20%)
    - Writing quality and technical accuracy (30%) (Writing is expected to meet or exceed accepted graduate-level English and scholarship standards. That is, all assignments will be graded on grammar and style as well as content.)
    - Rationale for answer is provided (20%)
    - Examples are included to illustrate rationale (15%) (If you do not have direct experience related to a particular question, then you are to provide analogies versus examples.)
    - Outside references are included (15%)
  - Quantitative assignments: All parts of question are addressed; All assumptions are clearly stated; All intermediate derivations and calculations are provided; Answer is technically correct and is clearly indicated; Answer precision and units are appropriate.
    - Each part of question is answered (20%)
    - Assumptions are clearly stated (20%)
    - Intermediate derivations and calculations are provided (25%)
    - Answer is technically correct and is clearly indicated (25%)
    - Answer precision and units are appropriate (10%)
- Course Project 40%
  -  Student preparation and participation (as described in Course Project Description) (40%)
  - Student technical understanding of the course project topic (as related to individual role that the student assumes and described in the Course Project Description) (20%)
  - Team preparation and participation (as described in Course Project Description) (20%)
  - Team technical understanding of the course project topic (as related to the Customer Team roles assumed by the students and the Seller Team roles assumed by the students and described in the Course Project Description) (20%)

# Notes

## Week 01 

Reference: 

- [Official PyTorch Tutorials](https://pytorch.org/tutorials/)

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  - [Visualizing A Neural Machine Translation Model (Mechanics of Seq2seq Models With Attention)](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
  - [Tensor2Tensor Intro](https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello_t2t.ipynb#scrollTo=OJKU36QAfqOC)

Misc

- [Zhihu: 为什么现在的LLM都是Decoder only的架构？](https://www.zhihu.com/question/588325646/answer/3357252612)
- [PaperWeekly - 为什么现在的大语言模型（LLM）都是Decoder-only的架构？](https://mp.weixin.qq.com/s/ZsHX-M9pisUvG9vqfzdzTQ)
- [PaperWeekly - 让研究人员绞尽脑汁的Transformer位置编码](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247521021&idx=1&sn=237295f1dc737eec233583451f861798)
- [PaperWeekly - Decoder-only的LLM为什么需要位置编码？](https://mp.weixin.qq.com/s/3sBYrKyEPP93nwigaOAAAA)
- [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide)
- [Large Language Models (in 2023)](https://www.youtube.com/watch?v=dbo3kNKPaUA)

## Week 02

ViT

## Week 03

Swin Transformer

- A hierarchical vision Transformer that excels at various computer vision tasks. It employing a **hierarchical architecture** and introduces **Shifted Windows**, a technique for efficient self-attention computation, and demonstrates the architecture's effectiveness in tasks like image classification, object detection, and semantic segmentation. The second addresses challenges in training large vision models, including instability, resolution gaps, and data hunger. 
- https://notebooklm.google.com/notebook/d8f1c767-cb6b-47b5-aaba-f7a509dbb71f

Pyramid Vision Transformer





## Week 04

Rich feature hierarchies for accurate object detection and semantic segmentation

- R-CNN: Regions with CNN features. 
