# About this course

## Course Summary

## Textbook

- Ayyadevara, V. K. & Reddy, Y. (2020). Modern Computer Vision with P yT or ch: Explor e Deep Learning Concepts and

  Implement Ov er 50 Real-W orld Image Applications . Birmingham, UK: Packt Publishing.

  ISBN-10: 1839213477

  ISBN-13: 978-1839213472

- Reference:

  - Foundations of Statistical Natural Language Processing. Manning, C. D. & Schutze H. ISBN-10: ‎ 0262133601.
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

- Introduction to PyTorch
- Image Classification
- Object Detection
- Semantic Segmentation
- Video Action Recognition
- Vision Transformer and Its Applications
- Introduction to Contrastive Learning
- Introduction to Self-Supervised Learning
- Introduction to Multimodal Learning - Not in summer
- Advanced Topics of Vision Transformers - Not in summer

# Check List

- [ ] Syllabus
- [ ] Course Outline

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

# Misc Notes

## Week 01 

SGD vs Adam: 

Validation set vs Test set: 

- Validation set used to turne the model's parameters and hyper-parameters. It is used during the trianing phase, so will run multiple times. It help in selecting the best model, hyper-parameters, control the overfitting etc. 

- Test set used to evaluate the final model's performance. It is used after the model has been trained and validated, run once. It provide an unbiased evaluation of the final model, giving and estimation of its performance on unseen data. 

- Data distribution

  - Training set assume has the simliar underlying distribution of the problem, large and diverse enough to capture the essential characteristics of the data distribution. 

  - Validation set / Test set: suppose to draw from the same distribution of training set. 

    
