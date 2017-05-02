import sys
import os
import fnmatch
import linecache

selat = "*I*p*"
output_file_name="PDOS_I_p"

# List of all DOS files to add 
dosfiles=[]
for dfile in os.listdir('.'):
    if fnmatch.fnmatch(dfile, selat):
        dosfiles.append(dfile)

if len(dosfiles)==0:
    print "ERROR: Provide a (list of) valid DOS file(s)"
    sys.exit(0)

print "dosfiles list: ",
for dosfile in dosfiles:
   print dosfile,
print ""

mat=[]
for i in range(len(dosfiles)):
    mati=[]
    for line in open(dosfiles[i],'r'):
        if line.split()[0] != "#":
            mati.append([float(line.split()[0]),float(line.split()[1])])
    if mat == []: # if it is the first dos file, copy total matrix (mat) = the first dos files's data
          mat=mati[:]
    else:
          for j in range(len(mati)): # if it is not the first file, sum values
                mat[j]=[mat[j][0],mat[j][1]+mati[j][1]]


out=open(output_file_name,"w")
for i in mat:
    print>>out, i[0], i[1]

out.close()
