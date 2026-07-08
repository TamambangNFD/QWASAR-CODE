# IDAP — Intelligent Data Analytics Platform

Enterprise SaaS Data Analytics Platform. See `/docs` (added in later takes) for
the full architecture (Volumes 1–4).

## Status: Take 1 of 12 — Repo & Infra Skeleton ✅

This is a **working walking skeleton**: a FastAPI backend, a Next.js frontend,
Postgres, and Redis, all wired together and running under Docker Compose. It
does not yet do anything analytics-related — that starts at Take 2. Its only
job is to prove the foundation runs cleanly before anything is built on top of it.

## Run it locally

```bash
cp .env.example .env
docker compose up --build
```

- Backend: http://localhost:8000 (docs at `/docs`)
- Frontend: http://localhost:3000 — should show "Backend status: ok"
- Postgres: localhost:5432 (user/pass: idap/idap)

## Repo structure

```
idap/
├── backend/           FastAPI app (Python)
│   ├── app/
│   │   ├── api/v1/    Route modules — one per feature area
│   │   ├── core/      Config, security (Take 2+)
│   │   ├── db/        SQLAlchemy session/engine
│   │   └── models/    ORM models (Take 3 onward)
│   ├── alembic/       DB migrations
│   └── tests/
├── frontend/          Next.js app (TypeScript)
│   └── app/
├── infra/             Deployment configs (populated from Take 12)
├── .github/workflows/ CI pipeline
└── docker-compose.yml Local dev environment
```

## Roadmap (see `CONTINUE_WITH_CLAUDE_CODE.md` for how to execute each take)

| Take | Scope | Status |
|---|---|---|
| 1 | Repo & infra skeleton | ✅ Done |
| 2 | Auth & multi-tenancy | ⬜ Next |
| 3 | Core data model + migrations | ⬜ |
| 4 | Dataset upload & profiling | ⬜ |
| 5 | Cleaning + transformation pipeline | ⬜ |
| 6 | KPI engine + calculation | ⬜ |
| 7 | Dashboard builder (frontend) | ⬜ |
| 8 | Report engine | ⬜ |
| 9 | First analytics package (plugin proof) | ⬜ |
| 10 | Billing & subscriptions | ⬜ |
| 11 | Admin portal | ⬜ |
| 12 | Production deployment | ⬜ |

## Tech stack

Backend: FastAPI, SQLAlchemy, Alembic, PostgreSQL, Redis, JWT/OAuth2
Frontend: Next.js, React, TypeScript, Tailwind CSS
Infra: Docker, Docker Compose, GitHub Actions
