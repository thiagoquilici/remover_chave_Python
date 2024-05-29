pessoa = {
    'Nome': 'Alex Machado',
    'Idade': 39,
    'Profissão': 'Programador',
    'Empresa': 'SENAI',
    'Gênero': 'Masculino',
    'Cidade': 'Taguatinga'
}

# remover chave
del pessoa[input('Informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')