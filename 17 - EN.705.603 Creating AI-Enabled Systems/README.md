# About this course

## Course Summary

## Textbook

None. Materials include papers and textbooks from O’Reilly online

Software:

- Jupyter Notebook: 
  - [O'Reilly tutorial on Jupyter notebooks](https://www.oreilly.com/member/login/?next=https%3A//learning.oreilly.com/scenarios/docker-for-ml/9781098109684/).

  - https://www.dataquest.io/blog/jupyter-notebook-tutorial/

- Docker
  - [Interactive Docker tutorial](https://www.oreilly.com/member/login/?next=https%3A//learning.oreilly.com/scenarios/docker-for-ml/9781098109684/) 
  - [The Docker Masterclass for Beginners](https://learning.oreilly.com/course/the-docker-masterclass/9781835888148/)

- Git/Github: 
  - https://learning.oreilly.com/videos/complete-git-guide/9781800209855/
  - https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners
  
- Matplotlib, Sklearn, pandas

- Flask

- [Pandas 101](https://zerotomastery.io/blog/pandas-101-data-manipulation-with-pandas-and-python/)

- [Numpy 101](https://zerotomastery.io/blog/numpy-101-tutorial/)

- [Matplotlib](https://zerotomastery.io/blog/matplotlib-guide-python/)


# Course Topics

- AI Overview & Case Studies
- ML Life-cycle Framework (6 Major Components)
- Requirements
- Data Engineering
- Feature Engineering
- Dataset Design
- Metrics
- Deployment & Post-Deployment
- Implementation Real-World Systems:
  - Object Detection
  - Visual Search
  - Multi-Modal Search
  - Recommendation System

# Course Schedule

- [x] Module 1	May 27	Introduction to AI Systems, Recommendation System	Discussion 1, Requirements Homework
- [x] Module 2	June 3	Data Engineering	Discussion 2, Data Engineering Homework
- [ ] Module 3	June 10	Feature Engineering & Dataset Design	Discussion 3, Feature Engineering Homework
- [ ] Module 4	June 17	Metrics & Model Development	Discussion 4, Metrics & Model Selection Homework
- [ ] Module 5	June 24	Deployment & Post-Deployment	Discussion 5, FRAUD DETECTION SYSTEM CASE STUDY
- [ ] Module 6	July 1	Object Detection System (Part 1)	Discussion 6, Object Detection Homework (Annotation Conversion, Negative Hard Mining, Data Streaming, etc.)
- [ ] Module 7	July 8	Object Detection System (Part 2)	Discussion 7, OBJECT DETECTION SYSTEM CASE STUDY
- [ ] Module 8	July 15	Visual Search Systems (Part 1)	Discussion 8, Visual Search Homework (RandAugment, Nearest Neighbor Search, etc.)
- [ ] Module 9	July 22	Visual Search Systems (Part 2)	Discussion 9, VISUAL SEARCH SYSTEM CASE STUDY
- [ ] Module 10	July 29	Multimodal Search Systems (Part 1)	Discussion 10, Multimodal Search (Text Processing, Multimodal Search, etc.)
- [ ] Module 11	August 5	Multimodal Search Systems (Part 2)	Discussion 11, MULTIMODAL SYSTEM CASE STUDY
- [ ] Module 12	August 12	Recommendation Systems	Discussion 12, RECOMMENDATION SYSTEM CASE STUDY

# Check List

- [x] Set up 1:1
- [x] Module 3 - Overview and Objectives
- [x] Module 3 - Readings 1
- [ ] Module 3 - Readings 2
- [x] Module 3 - Readings 3
- [x] Module 3 - Lectures 1
- [ ] Module 3 - Lectures 2
- [x] Module 3 - Numpy
- [x] Module 3 - Matplotlib
- [x] Assignment - transactions_1.parquet
- [ ] Assignment - Module 3 - Discussion?? 
- [ ] Assignment - Module 3 - Dataset Design & Feature Engineering for "SecureBank" Fraud Detection System
- [ ] Set up next week

# Grading

## Grading Policy

- Discussion Participation  20%
  - Timeliness

  - Critical Thinking

- Assignment 30%
- System project 50%

## Programming Assignments

# Notes

## Module 1

Course Objectives

- System Thinking
- Machine learning life-cycle
- Technologies + Resources
- Real-world Systems. 

Motivation

- Maximize value of ML models
- Improve research skills
- Implementation over theory
- Financial incentives

ML systems VS software systems

- Data vs Code, Model vs Algorithm, Iteration and experimentation vs Testing and debugging
- Probabilistic vs Deterministic, Adaptability vs Fixed logic, 
- Model evaluation vs Functional Test, Data dependence vs Code dependence. 
- Model deployment vs Software deployment, Monitoring and continuous vs Maintenance, Learning. 

When to use ML

- Capacity to learn, Patterns are complex, Data exists, Predictability, Similar distribution in production and training data, Tasks are repetitive, Consequence of errors is low, Tasks are scalable. 



## Modele 3

**Data Quality**

**Data**

Data issue: the label multiplicity problem, the lack of labels problem, the class imbalance problem, and techniques in data augmentation to address the lack of data problem. Data distribution shifts. 

We use the term “training data” instead of “training dataset” because “dataset” denotes a set that is finite and stationary.

Data is full of potential biases. There are biases caused during collecting, sampling, or labeling. Historical data might be embedded with human biases, and ML models, trained on this data, can perpetuate them.

**Sampling**

- Nonprobability Sampling: Convenience sampling (based on availability), Snowball samping (start with a small number and extend), Judgment sampling, Quota sampling, 
  - Language models are often trained not with data that is representative of all possible texts but with data that can be easily collected
  - Sentiment analysis: biased toward users who are willing to leave reviews online, and not necessarily representative of people who don’t have access to the internet or people who aren’t willing to put reviews online.
- Simple Random Sampling
  - Stratified Sampling
  - Weighted Sampling: random.choices
  - Reservoir Sampling: Sampling k elements from n Streaming data, ensure same probability
    - Put the first k elments into the reservoir. 
    - For each incoming element, generate a random number  1<=i<=n
    - If 1<=i<=k: replace the i-th element with the new income element. 
  - Importance sampling

**Labeling:** Data labeling has gone from being an auxiliary task to being a core function of many ML teams in production.

- Hand Labels: Difficult, expensive, data privacy, slow
- Label multiplicity: different data sources and annotators have different levels of accuracy. it’s important to first have a clear problem definition. 
- Data Lineage: keep track of the origin of each of your data samples as well as its labels
- Natural Labels: Travel time on google map, Stock price prediction, Clicks after recommend. Easier and cheaper to first start on tasks that have natural labels. 
  - Feedback loop length
  - Different type of user feedback: What is important. Choosing the eright window length

- Handling the Lack of Labels
  - Weak supervision: Leverages (often noisy) heuristics to generate labels
    - Snorkel: Labeling Function: Keyword heuristic, Regular expressions, Database lookup, The outputs of other models ...
    - Better performance with more data. LFs were being reused across tasks. 
  - Semi- supervision: Leverages structural assumptions to generate labels
    - Requires an initial set of labels.
    - Perturbation-based method: small perturbations to a sample shouldn’t change its label.
  - Transfer learning: Leverages models pretrained on another task for your new task
  - Active learning: Labels data samples that are most useful to your model
    - The hope here is that ML models can achieve greater accuracy with fewer training labels if they can choose which data samples to learn from.  A model (active learner) sends back queries in the form of unlabeled samples to be labeled by annotators (usually humans).
    - uncertainty measurement
    - query-by-committee
- Labeling Strategies: Manual Labeling, Crowdsourcing, Natural Labeling
- Measuring Label Quality, Inter-annotator Agreement: Cohen’s Kappa

**Class imbalance:** 

- Class imbalance can make learning difficult 
  - Class imbalance often means there’s insufficient signal for your model to learn to detect the minority classes. 
  - Class imbalance makes it easier for your model to get stuck in a nonoptimal solution by exploiting a simple heuristic instead of learning anything useful about the underlying pattern of the data.
  - Class imbalance leads to asymmetric costs of error—the cost of a wrong prediction on a sample of the rare class might be much higher than a wrong prediction on a sample of the majority class.
- Class imbalance: inherent in the problem, caused by biases during the sampling process, Lbeling errors. 
- Approaches to handeling class imbalance:
  - Using the right evaluation metrics: F1, precision, recall. Threshold. 
  - Data-level methods: Resampling (oversampling, undersampling). Tomek links, SMOTE (synthetic minority oversampling technique), two-phase learning, dynamic sampling. 
  - Algorithm level methods: Adjust loss function. Cost-sensitive learning, Class-balanced loss, Focal loss

**Data augmentation:** 

- Simple label-preserving transformations
  - image: cropping, flipping, rotating, inverting (horizontally or vertically), erasing part of the image, and more.
  - NLP: randomly replace a word with a similar word, assuming wouldn’t change the meaning or the sentiment
- Perturbation
  - Neural networks, in general, are sensitive to noise. AWGN (Additive White Gaussian Noise). 
  - Using deceptive data to trick a neural network into making wrong predictions is called adversarial attacks. 
- Data Synthesis



[**Feature Engineering Technique:** ](https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114)

- Imputation - Missing value

  - Drop
  	```python
  	threshold = 0.7#Dropping columns with missing value rate higher than threshold
  	data = data[data.columns[data.isnull().mean() < threshold]]
  	
  	#Dropping rows with missing value rate higher than threshold
  	data = data.loc[data.isnull().mean(axis=1) < threshold]
  	```

  - Numerical Imputation
    ```python
    #Filling all missing values with 0
    data = data.fillna(0)#Filling missing values with medians of the columns
    data = data.fillna(data.median())
    ```

  - Categorical Imputation

		```python
		**#Max fill function for categorical columns**
    data['column_name'].fillna(data['column_name'].value_counts().idxmax(), inplace=True)
    ```
	
- Handling Outlier

  - Outlier Detection with Standard Deviation

  - Outlier Detection with Percentiles

  - An Outlier Dilemma: Drop or Cap

- Binning

- Log transform

- OHE

- Grouping

- Feature Split

- Scaling: Normalization, Standardization

- Extracting Date

# Paper and article

3CQs...

1. Compliment the previous post
2. make the Comment.
3. make a Connection
4. ask a Question.

M1

- Chip Huyen. (2022). Designing Machine Learning Systems. Chapter 2: Introduction to Machine Learning Systems Design

M2

- Chip Huyen. (2022). Designing Machine Learning Systems. Chapter 3: Data Engineering Fundamentals
- Martin Kleppmann. (2017). Designing Data-Intensive Applications. Chapter 2. Data Models and Query Languages

M3

- Chip Huyen. (2022). *Designing Machine Learning Systems*. [Chapter 4: Training DatasetsLinks to an external site.](https://learning.oreilly.com/library/view/designing-machine-learning/9781098107956/ch04.html)
- Martin Kleppmann. (2017). *Designing Data-Intensive Applications*. [Chapter 5: Feature EngineeringLinks to an external site.](https://learning.oreilly.com/library/view/designing-machine-learning/9781098107956/ch05.html#feature_crossing)
- Emre Rençberoğlu. (2019). [Fundamental Techniques of Feature Engineering for Machine Learning](https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114) 



# Reference

14 weeks Course Topics (2022 or 2023?):

Module 1: AI Overview and Case Studies
Module 2: 6D Framework and Design Thinking
Module 3: Data Engineering - Computer Vision and Time Series
Module 4: Data Engineering for Unstructured Text
Module 5: Data Engineering for Categorical Data
Module 6: Data Storage
Module 7: Design Supervised Algorithms Part I
Module 8: Design Supervised Algorithms Part II
Module 9: Design Unsupervised Machine Learning Algorithms
Module 10: Reinforcement Learning Algorithms and Neuro-Symbolic Computing
Module 11: Testing, Metrics, and Bias
Module 12: Ethics in AI
Module 13: Deployment Part 1
Module 14: Deployment Part 2

M2

- [Data science + design thinking: A perfect blend to achieve the best user experience - Michael Radwin (Intuit) - Data science + design thinking: A perfect blend to achieve the best user experience [Video]](https://learning.oreilly.com/videos/data-science/0636920370871/0636920370871-video329150/?sso_link=yes&sso_link_from=johns-hopkins-university)

- [Design Thinking Methods and Tools for Innovation](https://link-springer-com.proxy1.library.jhu.edu/chapter/10.1007/978-3-319-20886-2_2)

M3

- [Image Filtering and Transformations in OpenCV - Practical Computer Vision [Book]](https://learning.oreilly.com/library/view/practical-computer-vision/9781788297684/1205ee0c-224d-455f-886b-b8c9c93cdcaa.xhtml#:-:text=Image%20Filtering%20and%20Transformations%20in%20OpenCV)

- [Practical Time Series Analysis]([Practical Time Series Analysis [Book]](https://learning.oreilly.com/library/view/practical-time-series/9781492041641/?sso_link=yes&sso_link_from=johns-hopkins-university)) - M3 Chapter 8

M4

- [Contextual Word Representations: A Contextual Introduction](https://arxiv-org.proxy1.library.jhu.edu/abs/1902.06006)

M6

- [Contextual Word Representations: A Contextual Introduction]([Designing Data-Intensive Applications [Book]](https://learning.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/?sso_link=yes&sso_link_from=johns-hopkins-university)) Chapter 2

- [NoSQL for Mere Mortals® [Book]](https://learning.oreilly.com/library/view/nosql-for-mere/9780134029894/?sso_link=yes&sso_link_from=johns-hopkins-university))

M7

- [Building Computer Vision Applications Using Artificial Neural Networks](https://link-springer-com.proxy1.library.jhu.edu/book/10.1007/978-1-4842-5887-3) - Chapter 6 Deep Learning in Object Detection

- [Practical Time Series Analysis]([Practical Time Series Analysis [Book]](https://learning.oreilly.com/library/view/practical-time-series/9781492041641/?sso_link=yes&sso_link_from=johns-hopkins-university)) - Chapter 6, 9, 10

- [You Only Look Once: Unified, Real-Time Object Detection](https://ieeexplore-ieee-org.proxy1.library.jhu.edu/document/7780460)

M8

- [Auto-WEKA: combined selection and hyperparameter optimization of classification algorithms](https://dl-acm-org.proxy1.library.jhu.edu/doi/10.1145/2487575.2487629)

- [A review of automatic selection methods for machine learning algorithms and hyper-parameter values](https://link-springer-com.proxy1.library.jhu.edu/article/10.1007/s13721-016-0125-6)

M9

- [Hands-On Unsupervised Learning with Python](https://learning.oreilly.com/library/view/hands-on-unsupervised-learning/9781789348279) Chapter 5, Soft Clustering and Gaussian Mixture Models

M10

- [Deep Reinforcement Learning Hands-On [Book]](https://learning.oreilly.com/library/view/deep-reinforcement-learning/9781788834247) Chapters 1, 2, 6, 8, 12, and 13

M11

- [Evaluating Machine Learning Models [Book]](https://learning.oreilly.com/library/view/evaluating-machine-learning/9781492048756)

M12

- [Building Ethics into Artificial Intelligence](https://arxiv-org.proxy1.library.jhu.edu/pdf/1812.02953.pdf)

- [Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing](https://dl-acm-org.proxy1.library.jhu.edu/doi/10.1145/3351095.3372873)

- [Datasheets for Datasets](https://arxiv.org/pdf/1803.09010.pdf)

- [Model Cards for Model Reporting](https://dl-acm-org.proxy1.library.jhu.edu/doi/pdf/10.1145/3287560.3287596)

M13

- [Building Machine Learning Powered Applications](https://learning.oreilly.com/library/view/building-machine-learning/9781492045106) Chapter 8-11

M14

- [Big Data Analysis: New Algorithms for a New Society](https://link-springer-com.proxy1.library.jhu.edu/book/10.1007/978-3-319-26989-4), An Overview of Concept Drift Applications

- [A survey on concept drift adaptation](https://dl-acm-org.proxy1.library.jhu.edu/doi/10.1145/2523813)
