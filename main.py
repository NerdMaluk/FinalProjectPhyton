import contacts


# Gerencia a interação com o usuário através de um menu.
def mostrar_menu():
    print("Menu de Opções:")
    print("1. Adicionar Contacto")
    print("2. Editar Contacto")
    print("3. Remover Contacto")
    print("4. Pesquisar Contacto por Nome")
    print("5. Pesquisar Contacto por Número")
    print("6. Mostrar Todos os Contactos")
    print("7. Sair")

# Chama as funções do contacts.py com base na escolha do usuário.
def obter_input_contacto():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    return nome, email, telefone, endereco

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            try:
                nome, email, telefone, endereco = obter_input_contacto()
                contacto = contacts.adicionar_contacto(nome, email, telefone, endereco)
                print("Contacto adicionado com sucesso:", contacto)
            except ValueError as e:
                print(e)
        elif opcao == '2':
            nome = input("Nome do contacto a editar: ")
            novo_nome = input("Novo nome (deixe em branco para não alterar): ")
            novo_telefone = input("Novo telefone (deixe em branco para não alterar): ")
            try:
                contacto = contacts.editar_contacto(nome, novo_nome if novo_nome else None, novo_telefone if novo_telefone else None)
                print("Contacto editado com sucesso:", contacto)
            except ValueError as e:
                print(e)
        elif opcao == '3':
            nome = input("Nome do contacto a remover: ")
            try:
                contacto = contacts.remover_contacto(nome)
                print("Contacto removido com sucesso:", contacto)
            except ValueError as e:
                print(e)
        elif opcao == '4':
            nome = input("Nome do contacto a pesquisar: ")
            try:
                contacto = contacts.pesquisar_contacto_nome(nome)
                print("Contacto encontrado:", contacto)
            except ValueError as e:
                print(e)
        elif opcao == '5':
            telefone = input("Número do contacto a pesquisar: ")
            try:
                contacto = contacts.pesquisar_contacto_numero(telefone)
                print("Contacto encontrado:", contacto)
            except ValueError as e:
                print(e)
                
        elif opcao == '6':
            contactos = contacts.mostrar_todos_contactos()
            if contactos:
                for contacto in contactos:
                    print(f"Nome: {contacto['nome']}, Email: {contacto['email']}, Número: {contacto['telefone']}, Endereço: {contacto['endereco']}")
            else:
                print("Nenhum contacto encontrado.")   

        elif opcao == '7':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    try:
        main()
    except EOFError:
        print("\nPrograma terminado.")
