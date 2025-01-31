# Machine-Learning-Project-Combined-cycle-Power-Plant-
This project focused on building machine learning models to predict Energy Production from a power plant based on various input features. The dataset provided contains several columns related to operational variables such as temperature, exhaust vaccum, ambient pressure, and relative humidity, which are used to predict the energy production.

The data underwent extensive preprocessing, including:
-Handling duplicates and outliers.
-Scaling features using MinMaxScaler for better performance in models.
-Splitting the dataset into training and testing sets.

Additionally, the project includes steps for:
-Data exploration with visualizations such as histograms and scatter plots.
-Evaluation of residuals to ensure that predictions are accurate.
-Model serialization using pickle to save and load trained models for future use.

Conclusion:
This project demonstrates the process of building, evaluating, and comparing machine learning models for predicting energy production from a power plant. It shows how to clean and preprocess the data, apply multiple regression models, and evaluate their performance in a clear and structured way. The Random Forest Regressor model performed the best in termns of prediction accuracy, which is reflected by the R-squared score.
