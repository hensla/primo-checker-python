Verifica via terminal se um número inteiro fornecido pelo usuário é ou não um número primo, utilizando divisão por tentativa.

---

## 📋 Descrição

Script Python de linha de comando que exercita conceitos fundamentais:

- Entrada e conversão de dados com `input()` e `int()`
- Laço `for` com `range()`
- Operador módulo `%` para verificar divisibilidade
- Uso de flag booleana para controle de estado
- Instrução `break` para otimizar o loop

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.6 ou superior instalado

### Executando o script

```bash
python main.py
```

### Exemplos de execução

```
n = 7
é primo
```

```
n = 12
não é primo
```

```
n = 1
não é primo
```

---

## 🧠 Como funciona

1. O usuário digita um número inteiro `n`
2. Uma flag `primo` é definida como `True`
3. O laço `for` percorre todos os inteiros de 2 até `n - 1`
4. Se algum desses valores dividir `n` sem resto (`n % i == 0`), `primo` é marcado como `False` e o loop é interrompido com `break`
5. Ao final, se `primo` ainda for `True` e `n > 1`, o número é primo

---

## ⚠️ Bugs na versão original

O código original continha dois erros que o impedem de executar:

```python
# ❌ 1. elif sem condição — SyntaxError
elif:
    n % i == 2

# ❌ 2. Lógica incompleta — nunca imprime "é primo"
```

```python
# ✅ Versão corrigida
n = int(input("n = "))
primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False
        break

if primo and n > 1:
    print("é primo")
else:
    print("não é primo")
```

---

## 📁 Estrutura do projeto

```
prime-number-checker/
└── main.py
```

---

## 🛠️ Tecnologias

- **Python 3** — linguagem principal

---

## 📚 Conceitos demonstrados

| Conceito          | Aplicação no código              |
|-------------------|----------------------------------|
| Operador módulo   | `n % i == 0`                     |
| Laço for + range  | `for i in range(2, n)`           |
| Flag booleana     | `primo = True / False`           |
| Break             | Interrompe o loop ao achar divisor|
| Condicional       | `if primo and n > 1`             |

---

## 💡 Possíveis melhorias

- Validar entradas negativas ou não numéricas
- Usar o algoritmo **Crivo de Eratóstenes** para checar múltiplos números de uma vez
- Otimizar o loop percorrendo apenas até `√n` em vez de `n - 1`
- Permitir verificar uma lista de números em sequência

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

> Projeto didático para praticar lógica de programação e teoria dos números em Python.
