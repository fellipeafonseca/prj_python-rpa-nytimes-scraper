# NYTimes - Automação RPA com ReFramework, Docker e WSL2 para coleta de notícias

## 📌 Descrição

Este projeto é uma automação RPA desenvolvida em **Python** seguindo o padrão **ReFramework**, utilizando **Selenium** para extrair notícias do site [The New York Times](https://www.nytimes.com/search).

Os dados extraídos são:

- **Título da notícia**
- **Data da publicação**
- **Descrição**
- **Imagem da Publicação**
- **Contagem de Ocorrências da frase de busca na notícia (título e descrição)**
- **Valor monetário (Dollars) na notícia (Verdadeiro/Falso)**



As notícias são salvas e é gerado um arquivo (`noticias.csv`) na raiz do projeto com dados extraídos.

## 📽️ Demonstração

### Execução Local
https://github.com/user-attachments/assets/9985e790-60a4-434e-a34a-0e1c4f1fdace


### Relatório gerado
![Relatorio Excel](https://github.com/user-attachments/assets/07ee2c78-ac0a-446b-86ae-b223e2c54578)


### Execução via docker

<img width="1358" height="473" alt="exec docker noticias" src="https://github.com/user-attachments/assets/85dcdf62-ee62-49c9-baa9-559a71ac0418" />


---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python** 🐍
- **Selenium WebDriver** 🌐
- **Pandas** 📊
- **ReFramework** (Robotic Enterprise Framework) 🤖
- **Docker** 🐳
- **WSL2 (Windows Subsystem for Linux 2)** 💻

---

## 📂 Estrutura do Projeto

```
📦 NYTimesScraper-RPA
├── 📜 config.json        # Configuração com parâmetros de busca
├── 📜 main.py            # Script principal que gerencia o fluxo
├── 📜 Dockerfile         # Configuração para containerização
├── 📜 requirements.txt   # Dependências do projeto
├── 📜 README.md          # Documentação do projeto
```

---

## ⚙️ Configuração e Execução

### 🔹 **1. Pré-requisitos**

Antes de rodar a aplicação, certifique-se de ter instalado:

- **Python 3.8+**
- **Docker e Docker Desktop (com integração WSL2 ativada)**
- **WSL2** configurado e habilitado para o Docker

### 🔹 **2. Clonar o Repositório**

```bash
git clone https://github.com/fellipeafonseca/prj_python-automacao-noticias-newYorkTimes.git

```

### 🔹 **3. Configurar as Variáveis no Config**

Abra o arquivo `config.json` e edite os valores conforme necessário:

```json
{
   "url": "https://www.nytimes.com/search",
    "frase": "grape", 
    "meses": 0,
    "idioma": "en",
    "tipo": "article",
    "ordenacao":"newest"
}
```

### 🔹 **4. Executar Localmente**

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rode o script principal:

```bash
python main.py
```

---

## 📝 Observações

- Certifique-se de que o **ChromeDriver** está compatível com a versão do Google Chrome instalada.
- Se o Docker não estiver rodando no **WSL2**, verifique as configurações no **Docker Desktop**.

---

## 🏆 Contribuições

Melhorias futuras para implementação:
- Estruturação melhor do reframework separando as responsabilidades em novas classes;

Fique à vontade para abrir um **Pull Request** ou relatar problemas na aba **Issues**!

🔗 **GitHub:** https://github.com/fellipeafonseca/prj_python-automacao-noticias-newYorkTimes

