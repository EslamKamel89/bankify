
# Docker Compose (Local Development)

## ▶️ Run the Application

Starts all services using the base configuration and local overrides.

```bash
docker compose \
  -f docker-compose.yml \
  -f docker-compose.local.yml \
  up
````

---

## 🔍 Validate Configuration

Renders the fully merged configuration (after applying overrides and env variables).

Use this to verify:

* Environment variables are injected correctly
* Final service definitions are as expected

```bash
docker compose \
  -f docker-compose.yml \
  -f docker-compose.local.yml \
  config
```


