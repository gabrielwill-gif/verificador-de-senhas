import getpass
import re

SENHAS_COMUNS = {"123456", "12345678", "password", "senha", "qwerty", "admin", "abc123"}


def avaliar_senha(senha: str) -> tuple[str, list[str]]:
    """Retorna a classificação da senha e uma lista de dicas de melhoria."""
    if senha.lower() in SENHAS_COMUNS:
        return "Muito fraca", ["Essa senha é extremamente comum. Troque imediatamente."]

    pontos = 0
    dicas = []

    if len(senha) >= 12:
        pontos += 2
    elif len(senha) >= 8:
        pontos += 1
    else:
        dicas.append("Use pelo menos 8 caracteres (o ideal é 12 ou mais).")

    regras = [
        (r"[a-z]", "Adicione letras minúsculas."),
        (r"[A-Z]", "Adicione letras maiúsculas."),
        (r"\d", "Adicione números."),
        (r"[^\w\s]", "Adicione símbolos (!@#$%...)."),
    ]
    for padrao, dica in regras:
        if re.search(padrao, senha):
            pontos += 1
        else:
            dicas.append(dica)

    if pontos <= 2:
        nivel = "Fraca"
    elif pontos <= 4:
        nivel = "Média"
    else:
        nivel = "Forte"

    return nivel, dicas


def main():
    print("=== Verificador de Força de Senha ===")
    senha = getpass.getpass("Digite a senha (não aparece na tela): ")
    nivel, dicas = avaliar_senha(senha)
    print(f"\nClassificação: {nivel}")
    for dica in dicas:
        print(f" - {dica}")


if __name__ == "__main__":
    main()
