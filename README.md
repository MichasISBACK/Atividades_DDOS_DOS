# Atividades_DDOS_DOS
Prática: DDOS e DOS  Testar comportamento de um serviço ao limitar RAM do container e simular consumo de  memória via endpoint /t. Somente em seu ambiente de teste. 

# Teste de DoS por Consumo de Memória em Docker

Este projeto demonstra, em ambiente controlado, como um serviço pode ter seu funcionamento afetado ao sofrer um ataque de negação de serviço (DoS) baseado em consumo excessivo de memória.  
A aplicação utiliza **Flask** e um endpoint que permite alocar memória artificialmente para fins de estudo.

> ⚠️ **IMPORTANTE:**  
> Este experimento deve ser executado **apenas em ambientes de teste**, em containers isolados e nunca em sistemas de produção.

---

## 📁 Estrutura do Projeto

.
├── app.py

└── Dockerfile


---

## 🚀 1. Requisitos

- Docker Desktop instalado
- Virtualização habilitada
- (Opcional) Python 3.10+ para executar localmente

---

## 🐳 2. Construir a imagem Docker

No diretório do projeto:


docker build -t teste-api .

---

## 3. Executar o container com limite de memória

Execute o container aplicando limite de RAM (ex.: 128 MB):

```bash
docker run -d -p 8000:8000 --memory=128m --name teste-api-container teste-api
