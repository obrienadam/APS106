import math

# Ex. 1, defining a list
items = ['apple', 'pear', 'orange', 'grape', 4, 3, 4.32, math.sin]

# Ex. 2, count the number of sentences in a paragraph
paragraph = """
The University of Toronto (U of T, UToronto, or Toronto) is a public research university in Toronto, Ontario, Canada on
the grounds that surround Queen's Park. It was founded by royal charter in 1827 as King's College, the first institution
of higher learning in the colony of Upper Canada. Originally controlled by the Church of England, the university assumed
the present name in 1850 upon becoming a secular institution. As a collegiate university, it comprises twelve colleges,
which differ in character and history, each with substantial autonomy on financial and institutional affairs. It has two
satellite campuses in Scarborough and Mississauga. Academically, the University of Toronto is noted for influential
movements and curricula in literary criticism and communication theory, known collectively as the Toronto School.
The university was the birthplace of insulin and stem cell research, and was the site of the first practical electron
microscope, the development of multi-touch technology, the identification of the first black hole Cygnus X-1, and the
development of the theory of NP-completeness. By a significant margin, it receives the most annual scientific research
funding of any Canadian university. It is one of two members of the Association of American Universities outside the
United States, the other being McGill University.[5] The Varsity Blues are the athletic teams that represent the
university in intercollegiate league matches, with long and storied ties to gridiron football and ice hockey. The
university's Hart House is an early example of the North American student centre, simultaneously serving cultural,
intellectual and recreational interests within its large Gothic-revival complex. The University of Toronto has educated
two Governors General of Canada and four Prime Ministers of Canada, four foreign leaders,[who?] fourteen Justices of the
Supreme Court, and has been affiliated with ten Nobel laureates.
"""

sentences = paragraph.split('. ')
print(len(sentences))
