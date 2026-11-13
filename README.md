# 🔐 Verificador de Força de Senha

Script em Python que avalia a força de uma senha e sugere melhorias.

## Como funciona
- Verifica tamanho, letras maiúsculas e minúsculas, números e símbolos
- Detecta senhas muito comuns
- Usa `getpass`, então a senha não aparece na tela
- Nada é salvo nem enviado para a internet

## Como executar
```bash
python verificador_senha.py
```

## Tecnologias
Python 3.9+

## Próximos passos
- Checar vazamentos via hash (k-anonymity)
- Interface gráfica
- Testes automatizados com pytest
