#!/usr/bin/env python
# coding: utf-8

# In[85]:


import os

import math
def degrees(rad_angle) :
    """Converts any angle in radians to degrees.

    If the input is None, the it returns None.
    For numerical input, the output is mapped to [-180,180]
    """
    if rad_angle is None :
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180 :
        angle = angle - 360
    while angle < -180 :
        angle = angle + 360
    return angle

def ramachandran_type(residue, next_residue) :
    """Expects Bio.PDB residues, returns ramachandran 'type'

    If this is the last residue in a polypeptide, use None
    for next_residue.

    Return value is a string: "General", "Glycine", "Proline"
    or "Pre-Pro".
    """
    if residue.resname.upper()=="GLY" :
        return "Glycine"
    elif residue.resname.upper()=="PRO" :
        return "Proline"
    elif next_residue is not None     and next_residue.resname.upper()=="PRO" :
        #exlcudes those that are Pro or Gly
        return "Pre-Pro"
    else :
        return "General" 

proteins  = ["GLY","ALA","LEU","MET","PHE","TRP","LYS","GLN","GLU","SER","PRO","VAL","ILE","CYS","TYR","HIS","ARG","ASN","ASP","THR"]
initials = ["G","A","L","M","F","W","K","Q","E","S","P","V","I","C","Y","H","R","N","D","T"]
path = 'Train/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdb' in file:
            files.append(os.path.join(r, file))

import Bio.PDB
for f in files:
	pdb_code = f[6:len(f)-4]
	#print(pdb_code)
	structure = Bio.PDB.PDBParser().get_structure(pdb_code, "Train/%s.pdb" % pdb_code)
	output_file = open("Train_csv/%s.csv" % pdb_code,"w")
	for model in structure :
   		for chain in model:
        	 #print ("Chain %s" %str(chain.id))
        	 polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
        	 for poly_index, poly in enumerate(polypeptides) :
            	  phi_psi = poly.get_phi_psi_list()
            	  for res_index, residue in enumerate(poly) :
                	  phi, psi = phi_psi[res_index]
                	  if phi and psi :
                	  #Don't write output when missing an angle
                    	   output_file.write("%s\t%f\t%f\t%s\n" % (initials[proteins.index(residue.resname)],	degrees(phi), degrees(psi),ramachandran_type(residue, poly[res_index+1])))
	output_file.close()
print ("Done")


path = 'Test/'

test_files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdb' in file:
            test_files.append(os.path.join(r, file))

import Bio.PDB
for f in test_files:
    pdb_code = f[5:len(f)-4]
    #print(pdb_code)
    structure = Bio.PDB.PDBParser().get_structure(pdb_code, "Test/%s.pdb" % pdb_code)
    output_file = open("Test_csv/%s.csv" % pdb_code,"w")
    for model in structure :
        for chain in model:
            #print ("Chain %s" %str(chain.id))
            polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
            for poly_index, poly in enumerate(polypeptides) :
                phi_psi = poly.get_phi_psi_list()
                for res_index, residue in enumerate(poly) :
                    phi, psi = phi_psi[res_index]
                    if phi and psi :
                        output_file.write("%s\t%f\t%f\t%s\n" % (initials[proteins.index(residue.resname)],	degrees(phi), degrees(psi),ramachandran_type(residue, poly[res_index+1])))
                    else: 
                        output_file.write("%s\t360\t360\txxx\n" % (initials[proteins.index(residue.resname)]))


    output_file.close()
print ("Done")


# In[ ]:




