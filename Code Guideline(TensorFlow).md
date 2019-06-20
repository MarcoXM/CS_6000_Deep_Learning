# Code Guideline （TensorFlow)

## Structure of the code

The code for each Tensorflow example shares a common structure:

	data/ 
	experiments/
	model/
		input_fn.py
		model_fn.py
		utils.py
		training.py
		evaluation.py
	train.py
	search_hyperparams.py
	synthesize_results.py
	evaluate.py

### Here is each `model/` file purpose:

* `model/input_fn.py`: where you define the input data pipeline
* `model/model_fn.py`: creates the deep learning model
* `model/utils.py`: utility functions for handling hyperparams / logging
* `model/training.py`: utility functions to train a model
* `model/evaluation.py`: utility functions to evaluate a model
We recommend reading through train.py to get a high-level overview.

Once you get the high-level idea, depending on your task and dataset, you might want to modify

* `model/model_fn.py` to change the model’s architecture, i.e. how you transform your input into your prediction as well as your loss, etc.
* `model/input_fn.py` to change the process of feeding data to the model.
* `train.py and evaluate.py` to change the story-line (maybe you need to change the filenames, load a vocabulary, etc.)

Once you get something working for your dataset, feel free to edit any part of the code to suit your own needs.


 