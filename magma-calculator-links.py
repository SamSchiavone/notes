import urllib.parse

code = """R<x>:=PolynomialRing(Rationals());
f:=x^3-2;
K<nu>:=NumberField(f);
P1:=ideal<Integers(K)|11,nu-7>;
IsPrincipal(P1);"""

# We tell Python NOT to encode these characters:
safe_chars = "()<>:=;|[],.*^-" 

base_url = "https://magma.maths.usyd.edu.au/calc/?input="
clean_query = urllib.parse.quote(code, safe=safe_chars)
full_url = base_url + clean_query

print(full_url)
