# 


## Goals of this HW3

Problem : Multilabels/Multiclassification Problem

* **Understand RNN concept**: which are machine learning models that are able to recognize and act on sequences of inputs.

* Understand The difficulty in how to **TRAINING RNN NETWORK**
* gradient **explosiong and gradient dissapearance.**
* How to deal with the seq data in **batch** !


## Advantages
* Possibility of processing input of any length
* Model size not increasing with size of input
* Computation takes into account historical information
* Weights are shared across time

## Disadvantages
* Computation being slow
* Difficulty of accessing information from a long time ago
* Cannot consider any future input for the current state



##  Problems 
### 1. Model using
> * FNN
> * RNN
> * LSTM
	
### 2. Using the pretrain_model to get the results
### 3. Comparing the result in many aspects 
### 4. How to improve the performance of the model

## Dataset 
[Deep Learning](http://deeplearning.net/datasets/)

* **Description** : So many datasets.

[Urban Sound Classification](https://www.kaggle.com/pavansanagapati/urban-sound-classification)

 * **Description** : The dataset contains 8732 sound excerpts (<=4s) of urban sounds from 10 classes, namely: Air Conditioner Car Horn Children Playing Dog bark Drilling Engine Idling Gun Shot Jackhammer Siren Street Music

 
[Kuzushiji-MNIST](https://www.kaggle.com/anokas/kuzushiji)

 * **Description** :49 classes (28x28 grayscale, 270,912 images), is a much larger, but imbalanced dataset containing 48 Hiragana characters and one Hiragana iteration mark.


[British Birdsong Dataset](https://www.kaggle.com/rtatman/british-birdsong-dataset)

* **Description** :88 species commonly heard in the United Kingdom
* Can you build a classifier to identify birds based on their songs?
* Can you generate new birdsongs based on this data?

## And here are some Homework:

1. [DARPA TIMIT Acoustic-Phonetic Continuous Speech](https://www.kaggle.com/mfekadu/darpa-timit-acousticphonetic-continuous-speech)
 * **Description** :
 * **Task** :

2. [Brown University HW RNN](http://cs.brown.edu/courses/cs1470/projects/public/hw5-rnn-lm.html)
 * **Description** : Recurrent Neural Network Language Model with Word Embeddings for language modeling the Penn Treebank Corpus
 * **Task** :

 
3. [Brown University HW RNN2](http://cs.brown.edu/courses/cs1470/projects/public/hw6-seq2seq.html)
	* **Description** : Sequence to Sequence Machine Translation
	* **Task** :  **Machine Translation**

4. [Georgia Tech College of Computing](https://www.cc.gatech.edu/classes/AY2018/cs7643_fall/hw3/)
	* **Description** : implement vanilla recurrent neural networks (RNNs) and Long-Short Term Memory (LSTM) RNNs and apply them to image captioning on COCO
	* **Task** : **Image Captioning**


## Reply 



This is good. I like the first one the most. Maybe for HW, we can select a few types of sound. Ask them to compare RNN, LSTM and GRU in running time, accuracy, etc. 

We can leave the entire dataset and problem as a project choice. I plan to give a list of course projects they can choose from. They can, of course, also have their own projects.

I think a dataset of 2G maybe manageable, which means we will take about 3 types of sound. Can you experiment with it and see how long it will take to run RNN, LSTM on it? If you need more space on Erdos, let me know.

