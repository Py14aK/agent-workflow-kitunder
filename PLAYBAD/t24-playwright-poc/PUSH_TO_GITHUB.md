# Add this package to GitHub

Suggested destination based on the repository that contains the `codex` folder:

```text
Py14aK/agent-workflow-kitunder/examples/t24-playwright-poc
```

## Safe procedure

1. Confirm company policy permits placing this sanitized scaffold in personal GitHub.
2. Confirm there are no credentials, internal URLs, customer data, account data, screenshots, traces, reports, or proprietary KHN selectors.
3. Clone the repository and create a branch.

```powershell
git clone https://github.com/Py14aK/agent-workflow-kitunder.git
cd agent-workflow-kitunder
git checkout -b feature/t24-playwright-poc
New-Item -ItemType Directory -Force examples\t24-playwright-poc
```

4. Copy the contents of this package into `examples\t24-playwright-poc`.
5. Review staged files before committing.

```powershell
git status
git diff -- .
git add examples/t24-playwright-poc
git diff --cached
git commit -m "Add sanitized T24 Playwright POC scaffold"
git push -u origin feature/t24-playwright-poc
```

6. Open a pull request. Do not push real selectors or internal banking information to a personal/public repository.
