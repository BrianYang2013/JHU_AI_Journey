# Module 01

**Embedding Algorithm**: 

- Convert discrete data, such as words, into continuous vectors of fixed dimensions. These vectors, known as embeddings, capture semantic information about the words. In the Transformer, embeddings are applied to both the input tokens (words) and the position information, creating word embeddings and positional embeddings. 
- Dimensionality Reduction, Semantic Understanding

Layer normalization







# Moduel 04 - Object Detection, RCNN DETR

**CV Tasks:** Classification(No spetial extend), Semantic Segmentation(No object, just pixels), Object Detection, Instance Segmentation

**Foreground objects**: primary subjects of interest in an image or video, often closer to the camera and typically the **focus** of analysis. Background objects: behind the foreground, forming the environment or setting but not the main focus.  

**Multi-scale features**: features that capture information at different spatial scales within an image. 

- Key aspects: Hierarchical information, Object Detection and Recognition, Semantic Segmentation, Texture and Context. 
-  Methods: Image pyramids, Multi-Scale Convolutional Networks, Spatial Pooling

**Hierarchical feature maps** in computer vision are the result of deep learning models, like convolutional neural networks (CNNs), extracting features at multiple levels of abstraction across different layers. Early layers capture low-level features (e.g., edges, textures), while deeper layers represent more complex, high-level features (e.g., shapes, objects). This hierarchy allows the model to process and combine different levels of detail, making it more robust for tasks like object detection, segmentation, and classification. Models such as **ResNet** and **FPN**(Feature Pyramid Networks) use hierarchical feature maps for better performance across scales.

**Challenges in Object Detection**: 

- **Multiple types of outputs**: Classification (label, softmax loss) + Regression (bounding box, L2 loss)
- **Multiple objects**: Each image needs a different number eof outputs
- **Computational expensive**: Apply CNN to huge number of locations, scales, and aspect ratios. 
- And more such as class imbalance, data annotation and quality, robustness to env variations, real-time processing ... 

**Bounding boxes:** 

- YOLO (You Only Look Once):  (center_x, center_y, width, height) normalized to the dimensions of the image. 
- COCO (Common Objects in Context): (x_min, y_min, width, height), where (x_min, y_min) represents the top-left corner
- Pascal VOC: (x_min, y_min, x_max, y_max), where (x_min, y_min) is the top-left and (x_max, y_max) is the bottom-right corner. 

2 stage detection model: **Selective Search** is a **region proposal algorithm** used in object detection, designed to efficiently identify potential object locations (regions of interest or ROIs) in an image. The core idea is to propose a limited number of regions that are likely to contain objects, instead of exhaustively evaluating every possible location and scale (which would be computationally expensive).

**R-CNN**: Regions with CNN features. 

- **Region Proposal**: R-CNN generates a set of *region proposals* (potential object locations) using a technique like Selective Search. This reduces the task of object detection to a classification problem over a limited number of regions instead of scanning the entire image.
- **CNN Feature Extraction**: For each proposed region, a CNN is used to extract fixed-length feature vectors, providing rich, discriminative features for the objects within those regions.
- **Classification and Regression**: The extracted features are passed to a classifier (like SVM) to classify the object in the region, and a regression model is used to refine the bounding box coordinates.

**R-CNN Training**

- Train a classificaiton model for ImageNet. Image -> Convolution and polling -> Final Conv feature map -> Fully connected layers -> Class scores 1k classes -> Softmax loss
- Continue fine-tuning the pre-trained model for detection. Re-initialize the last layer, to k(object classes) + 1 (background class). Fine-tune the pre-trained model with positive/negative regions on detected data (decided by IoU threshold, ignore small portion of ground truth)
  - IoU (Intersection over Union). 0.3 (threshold), 0.5(correct), 0.7(good), 0.9(Almost perfect). 
- Extract features: 
  - Apply selective search and extract region proposals for all images (~2k per image). 
  - Warp each region proposal to CNN input size, pass through CNN, save pool5 features to disk
- Train one binary SVM per class(cat) to classify region features
- Bbox regression

**Non-Maximum Suppression (NMS)** : used in object detection tasks to **filter out multiple overlapping bounding boxes** for the same object. It helps in refining the output by selecting the best bounding box for each detected object while removing redundant or overlapping ones.

**Hard Negative Mining** is a technique used in **object detection** and **binary classification tasks**, to improve the performance of models by focusing on difficult examples during training. It is especially useful when there is an imbalance between positive and negative samples, where most negative samples are easy to classify but a few are very challenging (i.e., hard negatives).

**Issues of R-CNN**

- Due to independent forward passes of the CNN, both training (84h) and inference (47s/image with VGG16) are slow => Share CNN computations for all proposals in the same image. 
- The training is post-hoc. i.e., CNN is not updated in response to final classifiers and regressors.  => Train the wntire system end to end all at once. 
- Complicated training pipeline => Train the wntire system end to end all at once. 

**Fast R-CNN**:  **processes the entire input image once through the convolutional layers**. This generates a **single set of feature maps** that are shared by all region proposals.

ROI Projection

ROI Pooling

**Fast R-CNN Architecture**

- Training: Input Image, Convent (full image feature maps), ROIs , ROI Pooling, FCs, Linear+softmax/Linear, Log loss + smooth L1 loss. Train end to end. 
- Inference: Input Image, Convent (whole image), ROIs, ROI Pooling, FCs, Linear+softmax/Linear

**Faster R-CNN Architecture**: Replace selective search with **RPN(Region Proposal Network)** to predict CNN-based RoIs from feature maps. 

- Input Image, CNN, Feature map, Region Proposal Network (proposals: classification loss, bounding box regression loss), RoI pooling, ... 



Coding

- How to get the feature map

# Misc

[视频内容分析：现状与六大趋势](https://fvl.fudan.edu.cn/_upload/article/files/3b/ca/e4f4b632467c8b42d3d02238b2b3/bb3faf3e-8461-468f-b269-dc4cbf58680c.pdf)

- Optical flow: refers to the motion of image points between two consecutive frames of a video sequence. It is a technique used to estimate the displacement of each pixel in an image over time. This information is crucial for various tasks such as: Motion detection, Object tracking, Video stabilization, Augmented reality.

- Motion Boundaries: refer to the edges or contours that delineate regions of different motion within an image sequence. These boundaries can be used to segment moving objects from the background, track objects over time, and understand the overall motion dynamics of a scene.

- Models: Non-local, SlowFast, MViT, VideoSwin, BEVT, OmniVL

- Dataset: HMDB51, UCF101(University of Central Florida 101), Kinetics-400VIdeoLT

- Contrastive Learning

- Knowledge Distillation is a technique in machine learning where we transfer the knowledge from a large, complex neural network (often called the "teacher" model) to a smaller, simpler one (the "student" model).

- Trustworthy Machine Learning is a subfield of artificial intelligence that focuses on developing machine learning models that are reliable, fair, and interpretable. In essence, it's about creating AI systems that we can trust.