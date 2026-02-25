def input_int(mensagem: str) -> int:
    """Pede um inteiro até o usuário digitar corretamente."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Digite apenas números.")


def input_nome(mensagem: str) -> str:
    """Pede um nome não vazio."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("❌ Nome não pode ser vazio.")


def encontrar_usuario(usuarios: list[dict], nome: str) -> dict | None:
    """Busca usuário pelo nome (case-insensitive)."""
    nome_lower = nome.lower()
    for u in usuarios:
        if u["nome"].lower() == nome_lower:
            return u
    return None


def cadastrar_usuario(usuarios: list[dict]) -> None:
    nome = input_nome("Digite o nome: ")
    if encontrar_usuario(usuarios, nome):
        print("⚠️ Já existe um usuário com esse nome.")
        return

    idade = input_int("Digite a idade: ")
    if idade <= 0 or idade > 120:
        print("⚠️ Idade inválida.")
        return

    usuarios.append({"nome": nome, "idade": idade})
    print("✅ Usuário cadastrado!")


def listar_usuarios(usuarios: list[dict]) -> None:
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return

    print("\n📋 Usuários cadastrados:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['idade']}")


def buscar_usuario(usuarios: list[dict]) -> None:
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return

    nome = input_nome("Digite o nome para buscar: ")
    u = encontrar_usuario(usuarios, nome)
    if u:
        print(f"✅ Encontrado: {u['nome']} - {u['idade']}")
    else:
        print("❌ Usuário não encontrado.")


def editar_usuario(usuarios: list[dict]) -> None:
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return

    nome = input_nome("Digite o nome para editar: ")
    u = encontrar_usuario(usuarios, nome)
    if not u:
        print("❌ Usuário não encontrado.")
        return

    nova_idade = input_int("Digite a nova idade: ")
    if nova_idade <= 0 or nova_idade > 120:
        print("⚠️ Idade inválida.")
        return

    u["idade"] = nova_idade
    print("✅ Usuário atualizado!")


def deletar_usuario(usuarios: list[dict]) -> None:
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return

    nome = input_nome("Digite o nome para deletar: ")
    u = encontrar_usuario(usuarios, nome)
    if not u:
        print("❌ Usuário não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja remover '{u['nome']}'? (s/n): ").strip().lower()
    if confirm == "s":
        usuarios.remove(u)
        print("✅ Usuário removido!")
    else:
        print("ℹ️ Operação cancelada.")


def mostrar_menu() -> None:
    print("\n=== USER MANAGEMENT SYSTEM ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Editar usuário")
    print("5 - Deletar usuário")
    print("6 - Sair")


def main():
    usuarios: list[dict] = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            buscar_usuario(usuarios)
        elif opcao == "4":
            editar_usuario(usuarios)
        elif opcao == "5":
            deletar_usuario(usuarios)
        elif opcao == "6":
            print("👋 Saindo... até a próxima!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()