def maxatomnum(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements and properties and a compound_formula. Returns a tuple where the first element is the highest atomic number element in the compound and the second element is it's corresponding atomic number.
    'O', 8
    'C', 6
    """


def molform(compound_formula):
    """(str) -> database
    When passed a string of the compound formula, returns a database with a string of the element symbol as the key and the number of atoms of that element as the value.
    {'C':2, 'H':6, 'O':1}
    {'C':1, 'H':4}
    """