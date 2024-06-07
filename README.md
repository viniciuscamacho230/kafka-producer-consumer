# kafka-producer-consumer
Trabalho - Criação de fila com Documentação
# kafka-docker-project
# Sistema Produtor/Consumidor com Docker e Apache Kafka

## Objetivos

- Desenvolver uma estrutura de Docker Compose.
- Implementar um sistema de produtor/consumidor.
- Utilizar a fila de Apache Kafka para a comunicação de mensagens.
- Utilizar linguagens diferentes no produtor e consumidor.
- O produtor precisa receber requisições REST para produzir as mensagens na fila.
- Criar uma estrutura JSON sobre qualquer tema.

## Requisitos

- Conhecimento em Docker e Kafka.
- Entendimento básico das estruturas de produtor/consumidor.
- Capacidade para escrever documentação clara e concisa.

## Estrutura do Projeto

kafka-docker-project/
│
├── docker-compose.yml
├── producer/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
└── consumer/
├── app.js
├── Dockerfile
└── package.json
