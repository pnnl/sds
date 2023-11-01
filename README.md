SDS
=======
Similarity down-selection (SDS) is a heuristic, greedy algorithm instantiated in Python for finding the subset of n items most dissimilar to each other out of a larger population.

SDS heuristically finds the most dissimilar set of size `n`
out of a population represented as an NxN matrix where the ith row (as well as the
ith column) belong to item i, and the element (i,j) is some pairwise relation between 
items i and j. 

The pairwise relation is a floating point value where larger values indicate
greater dissimilarity, and where the pairwise relation between item i and itself is represented
as np.nan (this allows the program to work with numpy log conversion and sums).

SDS was originally written to find the subset of n most dissimiliar conformers 
(similarity being determined by average pairwise RMSD between atoms).
In the original implemenation finding the n most dissimlar conformers 
for 50000x50000 matricies, SDS substationally outperformed a benchmark random sampling method in both 
time and accuracy. 

Note that because SDS finds the set of size `n` by building off of set `n-1`, finding set `n` also finds
also previous set sizes from 2-n. 


To run SDS
------------
1. import sds
2. matrix = sds.load(<path_to_matrix_containing_file>)
3. SDS = sds.downselect.SDS()
4. SDS.run(matrix, 3) # to yield n=3 structures


Citing SDS
-------------
If you would like to reference SDS in an academic paper, we ask you include the following.
The arXiv link will be updated pending completion of the journal review process.
* SDS, version 2.0.0 http://github.com/pnnl/sds (accessed MMM YYYY)
* Felicity F. Nielson, Sean M. Colby, Ryan S. Renslow, Thomas O. Metz. Similarity Downselection: A Python implementation of a heuristic search algorithm for finding the set of the n most dissimilar items with an application in conformer sampling.
* Felicity F. Nielson, Bill Kay, Stephen J. Young, Sean M. Colby, Ryan S. Renslow, Thomas O. Metz. Similarity Downselection: Finding the n Most Dissimilar Molecular Conformers for Reference-Free Metabolomics.

Disclaimer
----------
This material was prepared as an account of work sponsored by an agency of the United States Government.
Neither the United States Government nor the United States Department of Energy, nor Battelle, nor any of their employees, 
nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty, express or implied, 
or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software,
or process disclosed, or represents that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer,
or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government 
or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state 
or reflect those of the United States Government or any agency thereof.

PACIFIC NORTHWEST NATIONAL LABORATORY operated by BATTELLE for the UNITED STATES DEPARTMENT OF ENERGY under Contract DE-AC05-76RL01830
