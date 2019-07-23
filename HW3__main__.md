## Report of 10 Classes Problem


* dataset : 800 M numeric data in txt. Loading it with numpy and tranform it into 3 dimensions array (songId, timeStep, features)
* Running with Keras in GPU:
 
>1. RNN : 256 RNN units and 5 Dense Layers. 
>
>			Running time: 1000 epochs 900s
>			Highest Acc: 40%
>
>2. GRU : 256 GRU units and 5 Dense Layers. 
>
>			Running time: 1000 epochs 4500s
>			Highest Acc: 75%
>
>3. LSTM : 256 LSTM units and 5 Dense Layers. 
>
>			Running time: 1000 epochs 11000s
>			Highest Acc: 68%
>
>