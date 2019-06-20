# Datasets and Homeworks

## Dataset 
[Deep Learning](http://deeplearning.net/datasets/)

* **Description** : It is a well known dataset base, which has many dataset in many domain
* **Con** : datasets have been used many times, and students can get answer easily.

[Urban Sound Classification](https://www.kaggle.com/pavansanagapati/urban-sound-classification)

 * **Description** : The dataset contains **8732 sound excerpts** (<=4s) of urban sounds from 10 classes, namely: Air Conditioner Car Horn Children Playing Dog bark Drilling Engine Idling Gun Shot Jackhammer Siren Street Music.
 * **Pro** : It sounds data is perfect for RNN/LSTM to deal with, and it a multiclassification problem. And the student can acqure the experience in sounds data processing.
 * **Con** : It has 6GB size! Maybe we need to generate a subset of it if it works as a homework.

 
[Kuzushiji-MNIST](https://www.kaggle.com/anokas/kuzushiji)

 * **Description** :49 classes (28x28 grayscale, 270,912 images), is a much larger, but imbalanced dataset containing 48 Hiragana characters and one Hiragana iteration mark.
 * **Pro** : It a special version of MNIST, and images are suitable for both of CNN and RNN, we can set a comparission question like running time, accuracy. Moreover, multiclass and imbalanced data is a good task for their practise.
 * **Con** : As MNIST is easily to get a good performance, maybe not be a good task in parameters tuning!


[British Birdsong Dataset](https://www.kaggle.com/rtatman/british-birdsong-dataset)

* **Description** :88 species commonly heard in the United Kingdom.
And to classify the speis of a bird. Can you build a classifier to identify birds based on their songs?

* **Pro** : Handling the sound data, and Moreover can biuld sound gennerate model to generate new birdsongs based on this data. It is a good way for better understanding of RNN/LSTM.


[10 Monkey Species](https://www.kaggle.com/slothkong/10-monkey-species)

* **Description** :10 species Monkey classification. 

* **Pro** : Images are suitable for both of CNN and RNN, we can set a comparission question like running time, accuracy. And it would a little difficult than MNIST/Fashion MNIST.
* **Con** : It dont has many images for each categories (100-130 pieces). task would not be hard.

## And here are some Homework of Other School:


1. [Brown University HW RNN](http://cs.brown.edu/courses/cs1470/projects/public/hw5-rnn-lm.html)

 * **Difficulty** : ※ ※ ※ 
 * **Description** : Recurrent Neural Network Language Model with Word Embeddings for language modeling the Penn Treebank Corpus
 * **Task** : Language Modeling and need some extra knowledge in NLP

 
2. [Brown University HW RNN2](http://cs.brown.edu/courses/cs1470/projects/public/hw6-seq2seq.html)

 * **Difficulty** : ※ ※ ※ ※ ※ 
	* **Description** : Sequence to Sequence Machine Translation
	* **Task** :  **Machine Translation**. It would involed to RNN/LSTM one for encoder and another one for decoder. It would be more trick than the former one.

3. [Georgia Tech College of Computing](https://www.cc.gatech.edu/classes/AY2018/cs7643_fall/hw3/)

 * **Difficulty** : ※ ※ ※ ※ 
	* **Description** : implement vanilla recurrent neural networks (RNNs) and Long-Short Term Memory (LSTM) RNNs and apply them to image captioning on COCO
	* **Task** : **Image Captioning**. Good combination of RNN/LSTM with image. And without NLP knowledge required. But it is well known homework, so the answer is easily find on line.



