# Classifier-Sandbox

Built for Uvic Hackathing 2017. Interactive GUI to experiment with effect of change in classifier parameters. 

Using a dataset of spinal geometry vs. spinal abnormality in order to classify spinal abnormality.

![Spinal Classifier](https://samwheating.github.io/images/Spinal_Classifier.jpg) 

This visualization uses PCA to reduce the data dimensionality from 8 dimensions to 2 (This is not ideal). 
After studying statistics and data analysis a little more, I've realized that there are way better methods of dimensionality reduction for preserving inter-class separation (Discriminant Analysis, t-SNE etc.). Eventually I'll update this with a better data-flattening method.

**Try it Out!:**

start with `python GUI.py`

put in a set of values!

(If you don't feel like measuring your own spine, try [60, 20, 40, 45 , 100, 0])

If you want to try with Dimensionality Reduction by Linear Discriminant Analysis, use python GUI.py -LDA

Read more about this project here: https://samwheating.github.io/SpinalClassifier.html
