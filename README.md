# Notification Orchestrator

A distributed event-driven notification orchestration system designed to reliably deliver notifications across multiple communication channels.

The system uses Redis Streams for asynchronous event processing, PostgreSQL for persistent job tracking, and worker-based processing to achieve reliable message delivery with retry capabilities.

> ⚠️ This project is currently under active development.

---

## Features

- Asynchronous notification processing
- Event-driven architecture
- Redis Streams based message queue
- Worker-based notification processing
- Multi-channel delivery
    - Email
    - SMS
    - WhatsApp
- Retry mechanism *(Planned)*
- Dead Letter Queue *(Planned)*
- Delivery tracking *(Planned)*
- Observability with Grafana *(Planned)*

---

## Current Progress

- [x] FastAPI project setup
- [x] Redis connection
- [x] Notification Producer
- [x] Publish notifications to Redis Streams
- [ ] Consumer Groups
- [ ] Notification Workers
- [ ] Fan-out Dispatcher
- [ ] Retry Worker
- [ ] Dead Letter Queue
- [ ] PostgreSQL Integration
- [ ] Prometheus Metrics
- [ ] Grafana Dashboards

---

## Architecture

```
Provider

        │

        ▼

POST /notifications

        │

        ▼

Notification Service

        │

        ▼

Redis Streams

        │

        ▼

Notification Worker

        │

        ▼

Email Adapter
SMS Adapter
WhatsApp Adapter

        │

        ▼

Delivery Status
```

---

## Tech Stack

- FastAPI
- Redis Streams
- PostgreSQL *(Upcoming)*
- Docker
- Pydantic
- SQLAlchemy *(Upcoming)*

---

## Why Redis Streams?

Traditional queues are simple but provide limited visibility into message processing.

Redis Streams provide:

- Consumer Groups
- Message Acknowledgements
- Pending Message Recovery
- Horizontal Worker Scaling
- Ordered Event Processing

making them suitable for reliable notification systems.

---

## Future Improvements

- Exponential Backoff Retries
- Rate Limiting
- Scheduled Notifications
- Notification Templates
- Provider Failover
- Prometheus Metrics
- Grafana Dashboards
- OpenTelemetry Tracing

---

## Status

🚧 Work in Progress
