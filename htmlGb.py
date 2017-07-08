# Html Groebner 

## original data
source = [ \
"<html>", \
"<body>", \
"<p>ここに文章</p>", \
"<i>たとえばイタリックにしたり？</i>", \
"<p><strong>文章を強調</strong>してみたり！</p>", \
"</body>", \
"</html>" \
]

source2 = [ \
"<html>", \
"<body>", \
"<p>ここに文章</p>", \
"<p><strong>文章を強調</strong>してみたり！</p>", \
"</body>", \
"</html>" \
]

tags = [ \
"<html>","<body>","<p>","<strong>", \
"</html>","</body>","</p>","</strong>"]

contents = [ \
"ここに文章" , \
"<i>" , "たとえばイタリックにしたり？", "</i>" , \
"文章を強調", "してみたり！"\
]


## symbolic data
basis = [ \
"x1", "x2", "x3", "x4", \
"x5", "x6", "x7", "x8" \
]

field = [ \
"a1", \
"a2" , "a3", "a4", \
"a5", "a6" \
]

# convert Source to polynomial
def convertSorce(source):
    equation = []
    for s in source:
        for (t, b) in zip(tags, basis):
            s = s.replace(t, b)
        for (c, f) in zip(contents, field):
            s = s.replace(c, f)
        for (b, f) in zip(basis, field):
            index = s.find(b)
            if (index != 0) and (index != -1):
                s = s.replace(b, "*" + b)
            index = s.find(f)
            if (index != 0) and (index != -1):
                s = s.replace(f, "*" + f)
        equation.append(s)
    
    polynomial = equation[0]
    for i in range(1, len(equation)):
        polynomial += " + " + equation[i]
    return polynomial

# convert polynomial to source
def convertPolynomial(polynomial):
    source = []
    for m in polynomial.split("+"):
        s = ""
        for term in m.split("*"):
            for (t, b) in zip(tags ,basis):
                term = term.replace(b, t)
            for (c, f) in zip(contents, field):
                term = term.replace(f, c)
            s += term
        source.append(s)
    return source


poly1 = convertSorce(source)
poly2 = convertSorce(source2)

print(poly1)
print(poly2)

cs1 = convertPolynomial(poly1)
cs2 = convertPolynomial(poly2)
print(cs1)
print(cs2)
