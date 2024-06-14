import os

CONTACTS_FILE = 'contacts.txt'


# Lê os contactos do ficheiro contacts.txt e retorna uma lista de dicionários.
def ler_ficheiro():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        lines = file.readlines()
    contacts = [eval(line.strip()) for line in lines]
    return contacts


# Escreve a lista de contactos no ficheiro contacts.txt.
def escrever_ficheiro(contactos):
    with open(CONTACTS_FILE, 'w') as file:
        for contacto in contactos:
            file.write(f"{contacto}\n")


# Adiciona um novo contacto à lista após verificar se ele já não existe.
def adicionar_contacto(nome, email, telefone, endereco):
    contactos = ler_ficheiro()
    for contacto in contactos:
        if contacto['nome'] == nome:
            raise ValueError("Contacto já existe.")
    novo_contacto = {'nome': nome, 'email': email, 'telefone': telefone, 'endereco': endereco}
    contactos.append(novo_contacto)
    escrever_ficheiro(contactos)
    return novo_contacto


# Edita as informações de um contacto existente. Permite atualizar o nome, email, número de telefone e endereço.
def editar_contacto(nome, novo_nome=None, novo_telefone=None):
    contactos = ler_ficheiro()
    for contacto in contactos:
        if contacto['nome'] == nome:
            if novo_nome:
                contacto['nome'] = novo_nome
            if novo_telefone:
                contacto['telefone'] = novo_telefone
            escrever_ficheiro(contactos)
            return contacto
    raise ValueError("Contacto não encontrado.")


# Remove um contacto da lista após verificar se ele existe.
def remover_contacto(nome):
    contactos = ler_ficheiro()
    for contacto in contactos:
        if contacto['nome'] == nome:
            contactos.remove(contacto)
            escrever_ficheiro(contactos)
            return contacto
    raise ValueError("Contacto não encontrado.")


# Pesquisa e retorna as informações de um contacto pelo nome.
def pesquisar_contacto_nome(nome):
    contactos = ler_ficheiro()
    for contacto in contactos:
        if contacto['nome'] == nome:
            return contacto
    raise ValueError("Contacto não encontrado.")


# Pesquisa e retorna as informações de um contacto pelo número de telefone.
def pesquisar_contacto_numero(telefone):
    contactos = ler_ficheiro()
    for contacto in contactos:
        if contacto['telefone'] == telefone:
            return contacto
    raise ValueError("Contacto não encontrado.")


# Lê e retorna todos os contactos armazenados no ficheiro.
def mostrar_todos_contactos():
    contactos = ler_ficheiro()
    return contactos