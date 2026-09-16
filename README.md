NFL Play-Call Predictor
How predictable is an NFL play call before the snap?

This project uses NFL play-by-play data and machine learning to predict whether an offense will run or pass based on the game situation before the play.

Features
The model uses seven pre-play features:

Down
Yards to go
Field position
Score differential
Quarter
Shotgun formation
Time remaining in the quarter

Models
I experimented with several classification approaches, including:

Logistic Regression
Random Forest
LightGBM

After testing several approaches, I ultimately chose Random Forest for the final application, because I wanted to balance model performance with a simple UI and limited inputs.

Interactive Application

The project includes a Gradio application that allows users to enter an NFL game situation and receive a predicted play call.

What I Learned
This project gave me experience working through a complete machine-learning workflow: preparing data, selecting features, comparing classification models, evaluating model performance, analyzing predictive features, saving a trained model, and deploying it through an interactive application.

One of the most useful parts of the project was discovering how much model performance could be maintained while reducing the number of inputs. Testing different feature combinations helped me distinguish between information that was impactful for prediction and information that added little to the model. This allowed me to build a simpler application without sacrificing much predictive performance.