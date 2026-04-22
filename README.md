# Desafio: Customização de Agente

Neste teste, você vai pegar um agente simples já funcional e adaptá-lo para um caso de uso pessoal que faça sentido para você.

## Objetivo do desafio

Seu objetivo é transformar o agente atual em algo útil para uma tarefa pessoal. Alguns exemplos:

- assistente para organizar estudos
- agente para sugerir treinos
- agente para apoiar planejamento financeiro
- agente para gerar ideias de conteúdo
- agente para acompanhar hábitos

O mais importante não é o tema escolhido, e sim sua capacidade de entender a estrutura do agente e customizá-la com clareza.

## O que é um agente ReAct

Um agente ReAct combina duas capacidades:

- **Reason**: ele interpreta a solicitação, raciocina sobre o problema e decide o que fazer
- **Act**: ele pode executar ações por meio de ferramentas quando isso for útil

Na prática, isso significa que o agente não responde apenas com texto. Ele também pode decidir chamar uma ferramenta, observar o resultado e então produzir uma resposta melhor.

## O que é uma ferramenta

Uma ferramenta é uma função que o agente pode usar para executar alguma ação específica.

Exemplos:

- consultar uma agenda
- buscar uma cotação
- calcular algo
- registrar uma informação
- confirmar uma inscrição

Neste projeto, a ferramenta atual é apenas um exemplo simples. Você deve alterar essa ferramenta para combinar com o caso de uso que escolher.

## Sua tarefa

Você deve:

1. Escolher um caso de uso pessoal para o agente.
2. Alterar o **prompt** do agente para refletir esse novo papel.
3. Alterar ou substituir a **ferramenta** atual para apoiar esse caso de uso.
4. Garantir que a conversa com o agente faça sentido no terminal.
5. Entregar o **código alterado** com a sua customização funcionando.
6. Entregar um documento explicando:
   - por que você decidiu criar esse agente
   - o que você entendeu durante o processo de criação
   - quais decisões tomou ao customizar prompt e ferramenta

## Como enviar sua entrega

Envie sua entrega por email.

## O que será avaliado

- clareza na customização do prompt
- coerência entre o prompt e a ferramenta criada
- qualidade da experiência de uso
- organização do código
- sua capacidade de adaptar uma base existente sem complicar desnecessariamente
- clareza da sua explicação sobre decisões e aprendizados

## Estrutura atual do projeto

```text
meu_agente/
├── src/
│   ├── agente.py
│   └── cli.py
├── requirements.txt
├── .env.example
└── README.md
```

## Chaves de API

Este projeto usa o modelo `gemma-4-31b-it` via Google, então a variável principal é:

- `GOOGLE_API_KEY`

### A API do Google é gratuita?

Para este teste, você pode usar a **free tier** do Google AI Studio. Em termos práticos, isso significa que você consegue criar uma chave e testar a solução sem custo inicial, respeitando os limites gratuitos da plataforma.

### Como obter sua `GOOGLE_API_KEY`

1. Acesse [Google AI Studio](https://aistudio.google.com/).
2. Faça login com sua conta Google.
3. Aceite os termos da plataforma, se for o seu primeiro acesso.
4. Entre na área de API keys.
5. Crie uma nova chave ou visualize uma chave existente.
6. Copie `.env.example` para `.env`.
7. Preencha a variável `GOOGLE_API_KEY` com a sua chave.

Exemplo:

```env
GOOGLE_API_KEY="sua-chave-google-aqui"
```

## Configuração do ambiente

### Requisito mínimo

- Python 3.10 ou superior

### 1. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

## Como executar sem LangGraph Studio

Este repositório inclui um script para rodar o agente diretamente no terminal.

Se você ainda não ativou o ambiente virtual nesta sessão, ative antes de executar:

```bash
source .venv/bin/activate
```

Depois, rode:

```bash
python -m src.cli
```

Depois disso, basta conversar com o agente pelo terminal. As respostas serão exibidas em **streaming**, ou seja, aparecerão gradualmente na tela conforme forem geradas.

Para sair:

```text
exit
```

ou

```text
quit
```

## Arquivos principais

- `src/agente.py`: definição do agente, prompt e ferramentas
- `src/cli.py`: execução do agente em linha de comando

## Sobre o `cli.py`

O arquivo `src/cli.py` existe apenas como apoio para que você consiga executar o agente pelo terminal.

Você não precisa alterar esse arquivo para concluir o teste. Seu foco deve estar principalmente em `src/agente.py`, customizando o prompt e a ferramenta do agente.

## Observações importantes

- Não é necessário usar LangGraph Studio para concluir o desafio.
- Não é necessário criar várias ferramentas. Uma ferramenta bem pensada já é suficiente.
- Seu foco deve estar em personalização com critério, não em complexidade.
- Sua entrega deve incluir o código alterado e o documento com a reflexão pedida na seção "Sua tarefa".
