# coding: utf-8

"Copa 2014"

'Copa de 2014'

'''2014 - Copa do Mundo
'''

"Copa 'padrão fifa'"

'Copa "padrão fifa"'

# exemplo de multilines

print("""\
Uso: consulta_base [OPCOES]
    -h                      Exibe Saída de ajuda
    -U url                  Url do dataset
""")

# operações com string

st = 'maracana'
st[0] = 'm'
len(st) = 8

# captalize
st.capitalize()
# count
st.count("a")
>> 4
# startswith
st.startswith("m")
# endswith
st.endswith("z")
# split
"Copa de 2014".split(" ")
# join
" ".join(["Copa", "de", "2014"])
# replace
"Coda de 2014".replace("2014", "2018")


# interpolação
"% dias para a copa" % (dias)

"{} dias para a copa".format(100)

"{dias} para a copa".format(dias = 100)
