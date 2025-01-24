Using a dataset on satellites from kaggle to test and compare a traditional approach, specifically a decision tree, and a  neural network approach to classify the orbits of each satellite against the original data. To run the code, clone it and use a development environment such as VSCode or Google Colab.
The dataset can be found at 'https://www.kaggle.com/datasets/ucsusa/active-satellites/data' and details active satellites currently in orbit around earth. For each satellite there are 26 tracked values such as name, country, owner etc. For the code I'm running the relevant datapoints are: Type of Orbit, Class of Orbit, Apogee (Kilometeres), Perigee (Kilometers), Inclination (Degrees). Using the apogee, perigee and inclination to classify each satellite into Type/Class of Orbit. The question answered was "Is a neural network more effective at classifying satellite orbits than a traditional approach?", this question was chosen to support later work I will be doing with satellite orbits as well as being a point of interest for me.
Required dependencies (for module version look at dependencies.txt):
pandas
scikit-learn
matplotlib
numpy
torch
