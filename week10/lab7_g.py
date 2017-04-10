def minden(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements and properties and a compound_formula. Returns a tuple where the first element is the lowest density element in the compound and the second element is it's corresponding density.
    #>>>minden("elements_a.txt", "K1Fe4")
    'K', 0.862
    #>>>minden("elements_a.txt", "Fe6Cr1")
    'Cr', 7.19
    """
    min_rho = None

    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '#':
                continue
            elif line.strip() == 'END':
                break

            ele, tm, rho = line.strip().split('\t')

            try:
                rho = float(rho)
            except ValueError:
                continue

            if not min_rho or rho < min_rho[1]:
                min_rho = ele, rho

    return min_rho

    
def molform(compound_formula):
    """(str) -> database
    When passed a string of the compound formula, returns a database with a string of the element symbol as the key and the number of atoms of that element as the value.
     #>>>molform("C2H6O1")
    {'C':2, 'H':6, 'O':1}
    #>>>molfor("C1H4")
    {'C':1, 'H':4}
    """

    syms, nums = [], []
    is_num = False
    is_sym = False

    for ch in compound_formula:
        if ch.isdigit():
            if is_num:
                nums[-1] += ch
            else:
                nums.append(ch)
            is_num = True
            is_sym = False
        else:
            if is_sym:
                syms[-1] += ch
            else:
                syms.append(ch)
            is_num = False
            is_sym = True

    form = {}
    for sym, num in zip(syms, nums):
        form[sym] = int(num)

    return form

if __name__ == '__main__':
    print(minden('elements_g.txt', 'K1Fe4'))
    print(molform('Co34H2He134Li24234H2534C234'))