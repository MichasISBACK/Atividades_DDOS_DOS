# Atividades_DDOS_DOS
Prática: **DDOS e DOS** — Testar comportamento de um serviço ao limitar a RAM do container e simular consumo de memória via endpoint `/t`.  
> Somente em ambiente de teste.

# Teste de DoS por Consumo de Memória em Docker

Este projeto demonstra, em ambiente controlado, como um serviço pode ter seu funcionamento afetado ao sofrer um ataque de negação de serviço (**DoS**) baseado em consumo excessivo de memória.  
A aplicação utiliza **Flask** e um endpoint capaz de alocar memória artificialmente para fins educacionais.

> ⚠️ **IMPORTANTE:**  
> Este experimento deve ser executado **apenas em ambientes de teste**, em containers isolados e **nunca** em sistemas de produção.

---

## 📁 Estrutura do Projeto
.
├── app.py
└── Dockerfile

---

## 🚀 1. Requisitos

- Docker Desktop instalado  
- Virtualização habilitada (WSL2 / Hyper-V / BIOS)  
- (Opcional) Python 3.10+ para testes locais  

---

## 🐳 2. Construir a imagem Docker

No diretório do projeto, execute:

docker build -t teste-api .

---

## 🏃 3. Executar o container com limite de memória

Execute o container aplicando limite de RAM (ex.: **128 MB**):

docker run -d -p 8000:8000 --memory=128m --name teste-api-container teste-api

Verificar se está rodando:

---

## 🧪 4. Testes do endpoint `/t`

### ➤ Verificar uso atual de memória:

curl http://localhost:8000/t


Exemplo esperado:

{"allocated_chunks": 0, "rss_mb": 32}

---

### ➤ Alocar memória (ex.: **20 MB**):

curl "http://localhost:8000/t?allocate_mb=20"

---

### ➤ Testar comportamento de DoS (ex.: **200 MB**):

curl "http://localhost:8000/t?allocate_mb=200"

### ➤ Valor extremo (**500 MB**):
Comportamentos esperados:

- Retorno de `"MemoryError"`
- Container encerrado pelo **OOM Killer**
- Serviço pode parar de responder
- `docker ps` pode não listar mais o container

---

## 📉 5. Verificar logs após OOM

Mesmo com o container parado:
docker logs teste-api-container

Possíveis saídas: Killed ou MemoryError

---

## 📘 6. Funcionamento interno do endpoint `/t`

O endpoint aloca memória com:

```python
memory_chunks.append(bytearray(allocate_mb * 1024 * 1024))
Isso impede que o Python libere a memória, simulando um ataque DoS por saturação de RAM.

📊 7. Monitoramento do container

Monitorar uso de RAM em tempo real:

docker stats teste-api-container


Informações exibidas:

Memória usada

Limite de memória

Uso de CPU

Rede

🧱 8. Teste contínuo (ataque em loop)
Bash:
while true; do curl "http://localhost:8000/t?allocate_mb=50"; sleep 1; done

PowerShell:
while ($true) { curl "http://localhost:8000/t?allocate_mb=50"; Start-Sleep -Seconds 1 }

🧯 9. Boas práticas de proteção (em ambientes reais)

Limitar memória de containers

Rate limiting (NGINX, Traefik, Cloudflare)

Monitoramento (Prometheus + Grafana)

Validação de parâmetros

Timeouts e circuit breakers

Alertas de uso de RAM

🧹 10. Limpar containers e imagens
docker stop teste-api-container
docker rm teste-api-container
docker rmi teste-api

🔒 Segurança & Ética

Este teste deve ser feito somente em ambientes próprios.
Jamais execute testes de estresse em sistemas de terceiros sem autorização formal.

👨‍🏫 Créditos

Prática realizada para fins educacionais no Instituto Superior do Litoral do Paraná.



