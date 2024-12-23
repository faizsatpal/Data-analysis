Data Analysis with Pandas and Matplotlib
This project demonstrates basic data analysis and visualization using the Iris dataset. It uses Python libraries such as pandas, matplotlib, and seaborn to load, analyse, and visualize the dataset.
________________________________________
Features
1.	Dataset Loading and Exploration
o	Loads the Iris dataset using sklearn.datasets.
o	Displays the first few rows and basic dataset information.
o	Checks and handles missing values.
2.	Basic Data Analysis
o	Computes basic statistics for numerical columns.
o	Groups data by species and calculates the mean for specific columns.
3.	Data Visualization
o	Line chart for cumulative trends.
o	Bar chart comparing average sepal length by species.
o	Histogram showing the distribution of sepal length.
o	Scatter plot visualizing the relationship between sepal length and sepal width.
________________________________________
Technologies Used
•	Python 3.8+
•	Libraries:
o	pandas for data manipulation and analysis.
o	matplotlib and seaborn for data visualization.
o	sklearn.datasets for loading the Iris dataset.
________________________________________
How to Run the Project
1.	Clone the repository:
bash
Copy code
git clone https://github.com/faizsatpal/Data-analysis.git
cd data-analysis-pandas
2.	Install the required libraries:
bash
Copy code
pip install pandas matplotlib seaborn scikit-learn
3.	Run the script:
bash
Copy code
python data.py
4.	View the visualizations and results in the terminal and pop-up windows.
________________________________________
Dataset
•	Name: Iris Dataset
•	Source: Built-in dataset from sklearn.datasets.
•	Description: The dataset contains measurements of iris flowers (sepal length, sepal width, petal length, petal width) and their species (Setosa, Versicolour, Virginica).
________________________________________
Findings and Observations
•	The average sepal length varies across different species.
•	Sepal length and width exhibit distinct relationships when grouped by species.
•	The dataset is clean, with no missing values after preprocessing.
