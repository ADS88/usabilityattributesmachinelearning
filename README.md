Project to automatically identify usability quality attributes in agile user stories Uses spaCy library for machine learning. Python files included are used for data processing and ML model generation/training.
output folders hold the three machine learning models referenced in the report. 

Accessoutput contains the best & most recent model trained on accessibility. efficiencyoutput contains the best & most recent model trained on efficiency. output contains the best and most recent model trained to identify all usability quality attributes.
backlog.txt contains a specific backlog of user stories.

config/base_config.cfg contain the parameters used to train the machine learning models.
format_csv takes a CSV file and converts it into a suitable format to be read by main.py

specific_backlog.py takes the entire backlog and prints stories and their classifications from a specific backlog.

test_data.csv contains the entire test dataset used. test_models contains methods to evaluate the accuracy of specific models.

training_data.csv contains all the training data used to create the models.

main.py contains code converting CSVs to training format required by spacy and saving training data in binary format.

Machine learning models can be generated with the command "-m spacy train config.cfg --output ./outputdirectory"
where outputdirectory is the directory to save the models.

Example workflow to create a new model.
1) Create separate test and training CSV files mapping usability attributes and stories in a similar format to training_data.csv 
2) Run main.py with the filename containing your training new stories. Ensure to change the filename of the model will be saved in the data directory. 
3) Change base_config/config paths to point to the new model
4) Run the spacy train command mentioned above.
5) Run test_models.py with the file name containing your test data