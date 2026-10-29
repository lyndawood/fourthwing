# Agent conventions

Written by Forge from the team Wiki. Coding agents (Forge, Claude, Devin…) read this file first.

### Coding Standards
Applies to every repository unless its own AGENTS.md or Wiki pages say otherwise.

- **Scope:** change only what the request needs. No drive-by refactors, extra docs or demo files.
- **Match the repo:** follow the existing language, framework, file layout, naming and formatting. Use the project's formatter and linter when it has them.
- **Small commits:** commit each logical chunk of work (a feature plus its tests) with an imperative message, e.g. `Add pagination to GET /characters`.
- **Tests:** add or update tests for behaviour you change, and run the project's test command before committing.
- **Errors:** handle failures explicitly; never swallow exceptions silently.
- **Secrets:** never commit tokens, keys or `.env` files, and never print secrets in output.
- **Dependencies:** prefer the standard library and existing dependencies; add a new package only when it clearly pays for itself.
- **Accessibility:** UI changes keep WCAG AA contrast, visible focus and keyboard access.
(shared page: applies to every repository)

### Architecture Decisions
A running log of decisions that shape the code. Add one entry per decision, newest first, in this form:

### <Decision title> (<date>)
- **Context:** what problem or constraint prompted it.
- **Decision:** what was chosen.
- **Alternatives:** what else was considered and why it lost.
- **Consequences:** what this makes easier or harder.

Record decisions about frameworks, data storage, APIs and contracts, deployment, and anything a new contributor would otherwise have to rediscover.
(shared page: applies to every repository)
