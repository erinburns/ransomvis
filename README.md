# Python Plotly projects
Learning how to use Plotly for data visualisation by creating graphs using data about ransomware and malware. The data and graphs have been removed so others can use these files as a boilerplate for their own data visualisations.

Submit issues or improvements on Github. 

## Install Plotly
These instructions work for Mac OSX

Run

``` pip3 install plotly==4.1.0```

## Import your data
Save your data in CSV format in the same folder as the Python scripts.

Change this line in the Python script to your desired variable name and file name of the CSV where the data is located.

```ransomData = pd.read_csv("Edata.csv")```

## View graphs
View a the desired graph by running

```python3 fileName.py ```