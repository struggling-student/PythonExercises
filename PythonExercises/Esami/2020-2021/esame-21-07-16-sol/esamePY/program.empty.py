################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER"""

name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To check the error stack trace, you can uncomment the dedicated line in
# testlib.py (see the comment in the body of function runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #
'''Ex1: 7 points
    Design and implement a function ex1(file_rows, file_cols,
    file_values), that takes as input 3 file paths and returns as
    output a matrix represented as list of list.  The objective is to
    write the output matrix (henceforth named as "out"), computed on
    the basis of three matrices ("rows", "cols" and "values") stored
    in the three text files provided as an input to the function
    (file_rows, file_cols, file_values, respectively).

    The files contain integer numbers on their lines separated by
    commas (there is a comma after each integer). Every file line is a
    matrix row.  The c-th comma-separated number in a line is the
    element in the c-th column. Therefore, the c-th number in the r-th
    line of the file is the element at position (r,c) in the matrix.
    For example, if the file content is as follows:

    0  ,   1          ,     2,
    0,1,2,

    the corresponding matrix, represented as a list of lists, is the
    following:

    [[0, 1, 2],
     [0, 1, 2]].

    - The "out" should bear at position (r,c) the element of "values"
    at indexes (i,j) so that r = rows(i,j) e c = cols(i,j).
    - The size of "out" can be recovered observing the maximum value of
    "rows" and "cols". The maximum of "rows" and "cols" corresponds to
    the last row and column index of "out", respectively.
    - For all the remaning indexes not specified by "rows" and "cols",
    "out" should contain None.
    - If "values" cannot be accessed at the position (i,j), given that
    (i,j) is out of bounds, "out" should contain the sum of all
    elements of "cols" except that at position cols(i,j).

    For example: given three input files encoding the following
    matrices:
          "rows"              "cols"                     "values"
     0     1     2     |   1     5     3     |     5       2
     0     1     2     |   0     2     4     |     -10     3

    the function should return:

    "out" with dimensions 3x6:

    [[-10, 5, None, None, None, None],
    [None, None, 3, None, None, 2],
    [None, None, None, 12, 11, None]]

    Notice that::
    - "out" at position (0,1) holds 5, given that 5 was copied from
    "values" at position (0,0) and written in out at position (0,1);
    in fact, rows(0,0) = 0 e cols(0,0) = 1.
    - all the positions of "out" that are not specified in "rows" and
      "cols" are set to None
    - out(2,3) contains 12 given that indexes (2,3) are out of bounds
    accessing "values". So, the value is replaced with the sum of all
    elements of "cols" (15) except cols(0,2) = 3, which holds 12.

    Final Note: "rows" and "cols" have the same size, whereas the size
          of "values" can be different.
'''


def ex1(file_rows, file_cols, file_values):
    pass
    # Insert your code here


# ----------------------------------- EX.2 ----------------------------------- #

'''Ex2: 7 points
    
    A gang of space intruders is invading the pictures on our hard
    drive.  Design and implement a function ex2(image_file,
    space_intruder_pic_file) that helps us find out the exact location
    of the space intruder (whose picture is stored in
    space_intruder_pic_file) inside the image (image_file).

    Both space_intruder_pic_file and image_file are paths to PNG
    images.

    The function should return a pair (x,y) with the x and y
    coordinates of the space intruder in the image, if it is entirely
    there (that is, if the whole space intruder's picture lies within
    the area of the image). (x,y) is most upper left pixel of the
    image indicated by image_file from which the space intruder patch
    starts. If the indicated space intruder is not in the image (or
    only partially there), then the function should return (-1, -1).
     
    For example, if space_intruders_pic_file is "img/pastel.png" and
    space_intruder_pic_file is "intruder-00.png", the function should
    return (91,52). Notice that if space_intruders_pic_file is
    "img/napoleon.png" and space_intruder_pic_file is
    "intruder-00.png", the function should return (-1, -1) as that
    space intruder is not in the picture.
'''

import images
def ex2(image_file, space_intruder_pic_file):
    pass
    # Insert your code here


# ----------------------------------- EX.3 ----------------------------------- #

'''Ex3: 6+4 points
   Given genealogical relationships of a family, we seek for the heirs
   (the successors that will own the goods) of a deceased person.

   The informations about the family are described using a dictionary
   that contains:
    - as keys, the name of each person present in the family
    - as value associated to the key, the information of that person:

        'nameoftheperson' : { 
                'parents' : [ list of the parents (if known) ],
                'spouse'  : name of the partner (or None if 
                                                 not married
                                                 or divorced),
                'alive'   : True if alive, False if deceased,
                }

   Please, note:
    - It is impossible to find people with the same name.
    - For each person X that appears in the properties of some other
      people, X always exists in the main dictionary.
    - You can assume that if a name X is 'spouse' of Y, then Y is
      'spouse' of X.
    - There exist people (divorced or living together) that have
      children yet they are not married.
    - There exist people (with a second marriage) that have some
      children but they are not in common since coming from another
      marriage.

Part 1: 6 points.
    Implement a recursive function avi(name, family) that takes
    as input:

    - name: the name of one of the family members, which we have to use
      to find all the ancestors along with the distance from the
      person.
    - family: dictionary describing the family, following the format
      described above.

    NOTE: The dictionary family should NOT be changed

    The function should return a dictionary with:
    - as key, the name of the person and all of her/his ancestors
      (using only the relationships 'parents' and not 'spouse')
    - as value, the corresponding minimal distance to that person,
      which holds 0 for the same person.

    NOTE: the families used in the tests can contain people that have
    had children with their relatives, thus the same ancestors can be found at
    different distances according to the kinship branch taken. In this
    case, you should take the MINIMUM distance.

    (please check families/Kassie.pdf as a sample of ancestors of
    Kassie in the family families/big.json)

    Example: if the family is as follows (UPPERCASE=female,
    lowercase=male)
                        
                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

    avi('L', family) returns the dictionary
    {'L':0, 'f':1, 'Q':1, 'R':2, 's':2, 'a':2, 'B':2}
'''

## Ex3a
def avi(name, family):
    pass
    # Insert your code here


'''
Part 2: 4 points

    Implement the function ex3(family, name) that takes as input:
    - family: dictionary that describes a family according to the
      format described in EX3 - part 1.
    - name: the name of one of the family members of which we want to
      know the heirs

    NOTE: The dictionary family should NOT be changed

    To find the heirs, follow these rules, to be applied in this order:
      - if has a partner and/or has children alive, then only the
        partner and children inherit.
      - if has no no children nor a partner, the closest relatives
        up to the sixth degree inherit.
    
    The function should return as result a set that contains the names
    of the heirs of the deceased person.

    For instance, if the people and their relationships
    parent/children are as follows:

           Carlo + Lucia
                |              
             Aurora - Giovanni
            ________|_________
            |                |
           Ciro            Federica 
 
    the Ciro's heirs are only Aurora and Giovanni given that Ciro does
    not have either children nor wife and his parents are alive and
    are closer (1st degree) than the sister Federica (2nd degree).

    NOTA: The degree is the minimum number of parent relationships to
    traverse to go from a person to the other.

    The relationships to consider are exclusively those parent-child
    (and not those given by marriage).

    To compute the distance between two people X,Y you have to:
       - get the ancestors of X and Y along with their distances from
         X to Y using the function avi(name, family).
       - find the common ancestor Z so that the path X--Z--U has
         minimum lenght
       - if a common ancestor between X and Y does not exist, then X
         and Y are not related.
 
    Example: if the family is as follows (UPPERCASE=female,
    lowercase=male)

                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n


    The degree between G and J is 4 (the shortest path that connects
    them is G-c-a/B-E-J and contains 4 edges). In fact. G and J have
    in common the ancestors a, B.
'''

## Ex3b
def ex3(family, name):
    pass
    # write the code here

# ----------------------------------- EX.4 ----------------------------------- #


'''Es4: 8 points [BASED ON A TRUE STORY]

    An AI researcher tested some automated reasoning tools. These
    tools return one out of three possible results: 'sat', 'unsat',
    'timeout' (in case the computation took too long). The researcher
    let those tools run on a number of benchmarks and collected the
    results in a rather peculiar way: given a root directory (e.g.,
    "testbed/00") that contains all the results gathered during the
    "testbed/00" series of experiments, the first sub-directories of
    the root specify the tool names (e.g., "fastsolver" and
    "powertool"). Then, for every tool-directory, each path to a text
    file identifies a benchmark. The text file contains the result of
    the automated reasoing task.
    
    For example, under "testbed/00" we have
    "fastsolver/alaska/demo-v2/demo-v-00.txt" and
    "powertool/alaska/demo-v2/demo-v-00.txt".
    Both files contain the string "sat", which means that both tools
    returned the same result.
    
    Notice that the sole filename does not suffice to uniquely
    identify a test: indeed, under "testbed/00" we have also
    "fastsolver/alaska/demo-v3/demo-v-00.txt" and
    "powertool/alaska/demo-v3/demo-v-00.txt", which are different
    tests than the ones listed above (see the "demo-v3" directory name
    in place of "demo-v2").
    
    Also, it might happen that some tools did not run over a given
    benchmark, thus some files or entire sub-directories could be
    missing under a tool whereas they occur under other tools (e.g.,
    under "testbed/00/powertool" we have
    "alaska/demo-v2/demo-v-02.txt" though it does not occur under
    "testbed/00/fastsolver").
    
    To help our researcher properly summarise the results of the
    experiments, design and implement a function ex4(testbed_dir) such
    that:
    - it is recursive or uses recursive function(s)/method(s);
    - it receives the root directory (testbed_dir) with the test
      results,nested as explained above 
    - it returns the following data structure.
    
    The returned data structure is a pair containing
    1) the set of all tools used in this test (e.g., for ""testbed/00"
    the set should be {"fastsolver", "powertool"}), as per the
    subdirectories of testbed_dir;
    2) a dictionary that has as a key, the test name (e.g.,
    "alaska/demo-v3/demo-v-00.txt"), and as the value, a dictionary
    associating to every tool its result on that benchmark (e.g.,
    {'powertool': 'unsat', 'fastsolver': 'sat'}).

    The result of ex4("testbed/00"), for example, should be:
    ( {'powertool', 'fastsolver'}, 
      {'alaska/demo-v3/demo-v-00.txt':
              {'powertool': 'unsat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-00.txt': 
              {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-01.txt': 
              {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-02.txt':
              {'powertool': 'sat'}}
    ).
'''
import os

def ex4(dir1, ext):
    pass
    # Insert your code here

################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass
