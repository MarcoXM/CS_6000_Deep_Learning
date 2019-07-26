# Final Project Code Guideline 

## Structure of the code

The code for each **Tensorflow / Keras** example shares a common structure:

	data/ #in which we keep our dataset
	 	train/
    	dev/
    	test/
	experiments/  # find the best parameters
	
	model/
		input_fn.py
		model_fn.py
		utils.py
		training.py
		evaluation.py
	build_dataset.py
	train.py
	search_hyperparams.py
	synthesize_results.py
	evaluate.py

### Here is each `model/` file purpose:

* `model/input_fn.py`: where you define the input data pipeline, from Raw data >>>> Tensor.
* `model/model_fn.py`: creates the deep learning model/architecture
* `model/utils.py`: utility functions for handling hyperparams / logging
* `model/training.py`: utility functions to train a model
* `model/evaluation.py`: utility functions to evaluate a model
We recommend reading through train.py to get a high-level overview.

Once you get the high-level idea, depending on your task and dataset, you might want to modify

* `build_dataset.py`: creates or transforms the dataset, build the split into train/dev/test.
* `train.py`: train the model on the input data, and evaluate each epoch on the dev set
* `search_hyperparams.py`: run train.py multiple times with different hyperparameters
* `synthesize_results.py`: explore different experiments in a directory and display a nice table of the results
* `evaluate.py`: evaluate the model on the test set (should be run once at the end of your project)


Once you get something working for your dataset, feel free to edit any part of the code to suit your own needs.

## Final project 
1. 训练记录，record every 2% of Epoch！
2. scripts and markdown.
3. if youc can deploy your model. There would be a 10 point extra credit.
 