The algorithm was tested on 4 databases, namely, i)myoglobins, ii)Proteases, iii)TransGlucosidases and iv) All three together

The submission contains 4 folders, with each folder representing one database.
All the folders contain the same codes, so running any one would be sufficient.

Inside each folder, Train and Test folders contain the .pdb files.
Train_csv and Test_csv contain the phi psi angles measured from the .pdb files.
DSSP folder contains the dssp outputs from the corresponding .pdb files.
DSSP_Struct contains the structure predicted by DSSP algorithm.

DSSP_Test.py extracts the secondary structure from DSSP files.
Train.py trains the database to generate the RAI matrix.
Evaluate.py runs the algorithm on all the test files and compares them with DSSP results.

Evaluate.py outputs the accuracy and confusion matrix measures.



