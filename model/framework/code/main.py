# imports
import os
import csv
import sys
import datamol as dm
import molfeat
from molfeat.trans.fp import FPVecTransformer

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles):
    import numpy as np
    n_dims = 60
    transformer = FPVecTransformer(kind='usrcat', dtype=float)
    results = []
    for s in smiles:
        try:
            mol = dm.to_mol(s)
            if mol is None:
                raise ValueError("Invalid SMILES")
            mol_3d = dm.conformers.generate(mol, n_confs=1, minimize_energy=True)
            feat = transformer([mol_3d])[0]
        except Exception:
            feat = [float('nan')] * n_dims
        results.append(feat)
    return results

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["dim_{0}".format(str(i).zfill(2)) for i in range(60)])  # header
    for o in outputs:
        writer.writerow(o)
