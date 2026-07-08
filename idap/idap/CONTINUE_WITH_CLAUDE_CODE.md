# Continuing IDAP in Claude Code

This repo was started in Claude (chat) as Take 1. Everything from Take 2
onward should happen in **Claude Code**, because those takes require
iterating against real errors — running the test suite, seeing what fails,
fixing it, re-running — which chat cannot do. Claude Code can.

---

## 1. Get the repo onto your machine and into GitHub

```bash
# unzip the file you downloaded from Claude, then:
cd idap
git init
git add .
git commit -m "Take 1: repo & infra skeleton"

# create a new empty repo on github.com first (no README/gitignore), then:
git remote add origin https://github.com/<your-username>/idap.git
git branch -M main
git push -u origin main
```

## 2. Install Claude Code

If you haven't already:

```bash
npm install -g @anthropic-ai/claude-code
```

(If that package name has changed, check `docs.claude.com` — product details
can shift after my knowledge cutoff.)

## 3. Open the project

```bash
cd idap
claude
```

This starts Claude Code inside the repo. It can see the whole file tree,
run `docker compose up`, run `pytest`, edit files, and commit — across as
many sessions as it takes.

## 4. First thing to do in Claude Code

Paste this as your first message, so it has full context:

> This is the IDAP repo, Take 1 of 12 complete (repo skeleton, FastAPI +
> Next.js + Postgres + Redis, all running under Docker Compose). Read
> README.md for the full roadmap. Run `docker compose up --build` and
> confirm the health check passes before doing anything else. Then start
> Take 2: Auth & multi-tenancy.

## 5. The prompt to give it for each subsequent take

Copy-paste one of these per session. Each assumes the previous take is
merged and working.

**Take 2 — Auth & multi-tenancy**
> Implement Take 2 from README.md: JWT + refresh token auth, an
> Organization model with row-level tenant isolation, RBAC matching the
> roles in Volume 1 Chapter 7 (Platform Owner, Platform Admin, Org Admin,
> Manager, Analyst, Data Collector, Viewer, Guest), and registration/
> login/invite endpoints. Write tests proving two orgs cannot see each
> other's data. Update the CI workflow if needed. Commit when tests pass.

**Take 3 — Core data model + migrations**
> Implement Take 3: build out the full schema from Volume 2 Chapter 3
> (users, organizations, workspaces, projects, teams, roles, permissions,
> subscriptions, datasets, data sources, reports, dashboards, widgets,
> notifications, audit logs, scheduled jobs, api keys, activity logs) as
> SQLAlchemy models + Alembic migrations. Run `alembic upgrade head`
> against a clean DB and confirm it succeeds.

**Take 4 — Dataset upload & profiling**
> Implement Take 4: CSV/Excel upload endpoint, S3-compatible storage
> (use MinIO in docker-compose for local dev), and a Dataset Intelligence
> service that detects column types, keys, duplicates, missing values,
> outliers, and computes the Data Quality Score described in Volume 4
> Chapter 2. Return a profiling report from the API.

**Take 5 — Cleaning + transformation pipeline**
> Implement Take 5: configurable cleaning rules (as data, not code) per
> Volume 4 Chapter 3, applied through a Transformation Service pipeline.
> Every run should log a before/after diff to a history table and update
> the Data Quality Score.

**Take 6 — KPI engine + calculation**
> Implement Take 6: config-driven KPI definitions per Volume 4 Chapter 4,
> a Calculation Engine that resolves formulas against dataset fields at
> runtime, and the dependency-graph recomputation strategy from Volume 4
> Chapter 10 (only recompute affected KPIs on data change, not everything).

**Take 7 — Dashboard builder (frontend)**
> Implement Take 7: a drag-and-drop dashboard canvas in Next.js using
> Apache ECharts, save/load against the backend, widget types for KPIs,
> charts, tables. Follow the design system direction from Volume 3.

**Take 8 — Report engine**
> Implement Take 8: template-driven report generation (PDF and Excel to
> start) from dashboard data, per Volume 4 Chapter 9.

**Take 9 — First analytics package (plugin proof)**
> Implement Take 9: build "Business Analytics" as an installable package
> through the Plugin Framework (Volume 4 Chapter 12) — package manifest,
> KPI set, dashboard templates — touching zero core engine code. This
> proves the plugin architecture actually works before more packages
> are built.

**Take 10 — Billing & subscriptions**
> Implement Take 10: Stripe integration, package-level subscription
> gating so an org can only use packages they've paid for, basic usage
> limits.

**Take 11 — Admin portal**
> Implement Take 11: a minimal platform-owner admin view — organizations
> list, subscriptions, system health — per Volume 3 Chapter 5.

**Take 12 — Production deployment**
> Implement Take 12: production Dockerfiles review, deployment config
> for [your chosen host], managed Postgres connection, secrets
> management, HTTPS, health checks, and basic error tracking. Deploy and
> confirm the live URL works end to end.

## 6. General rules to give Claude Code up front (paste once, keep it in context)

> Follow the architecture in the Volume 1–4 documents referenced in this
> repo. No industry-specific logic belongs in the core engine — only in
> installable packages. Every take should end with passing tests and a
> commit. Don't skip ahead to a later take before the current one's tests
> pass. If a design decision from the volumes turns out to be wrong once
> you're actually building it, flag it and explain why before deviating.
