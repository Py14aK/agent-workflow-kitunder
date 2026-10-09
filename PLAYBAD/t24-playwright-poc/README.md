# T24 Playwright POC

Sanitized Playwright scaffold for Temenos T24 R21/R26 SYT smoke testing. Selectors, URLs, and credentials are placeholders. Replace them locally. Do not commit the replacements.

## Dependencies

Runtime:

- Node.js 20 or later, with npm. `@types/node` is pinned to `^22.0.0`.
- Microsoft Edge, because `playwright.config.ts` sets `channel: 'msedge'`.

Development dependencies from `package.json`:

| Package | Range | Role |
| --- | --- | --- |
| `@playwright/test` | `^1.48.0` | Test runner, browser control, assertions, HTML/JSON/JUnit reporters |
| `typescript` | `^5.6.0` | Type-check for the config, pages, helpers, and tests |
| `@types/node` | `^22.0.0` | Node types used by the screenshot helper |

There are no production dependencies. Install from this directory:

```powershell
npm ci
npx playwright install msedge
```

`npm ci` requires a lockfile. If this scaffold has no `package-lock.json` yet, use `npm install` once, review the lockfile, and commit only that lockfile. If the closed network cannot reach npm, use the Playwright and Node packages already approved and installed by IT. Do not bypass corporate network controls.

## Configuration

Copy the variable names from `.env.example` into an approved local secret store. Do not create a committed `.env` file. `.gitignore` already excludes `.env` and `.env.*` except `.env.example`.

| Variable | Required | Purpose |
| --- | --- | --- |
| `T24_BASE_URL` | Fallback | Base URL when a release-specific URL is absent |
| `T24_R21_URL` | For R21 | Base URL of the `T24-R21-SYT` project |
| `T24_R26_URL` | For R26 | Base URL of the `T24-R26-SYT` project |
| `T24_INPUT_USERNAME` | Yes | Test user. The smoke test fails if this is empty |
| `T24_INPUT_PASSWORD` | Yes | Test password. The smoke test fails if this is empty |
| `T24_SMOKE_COMMAND` | No | Terminal command. Defaults to `ENQ TXN.ENTRY` |

Before the first real run, replace every `TODO_...` selector in `tests/smoke/t24-terminal.smoke.spec.ts` from the approved working automation. The login page object accepts an optional frame and error selector. The terminal page object accepts an optional frame and command-error selector.

## Usage

From `PLAYBAD/t24-playwright-poc`:

```powershell
npm run test:list
$env:T24_R21_URL="APPROVED_INTERNAL_URL"
$env:T24_INPUT_USERNAME="APPROVED_TEST_USER"
$env:T24_INPUT_PASSWORD="LOCAL_SECRET"
$env:T24_SMOKE_COMMAND="ENQ TXN.ENTRY"
npm run test:ui
```

Scripts:

| Script | Command | Use |
| --- | --- | --- |
| `test` | `playwright test` | Run every project. Needs both release URLs, or `T24_BASE_URL` as fallback |
| `test:r21` | `playwright test --project=T24-R21-SYT --headed` | Headed R21 run |
| `test:r26` | `playwright test --project=T24-R26-SYT --headed` | Headed R26 run |
| `test:ui` | `playwright test --ui` | Playwright UI mode |
| `test:list` | `playwright test --list` | List tests without opening T24 |
| `report` | `playwright show-report reports/html` | Open the HTML report after a run |

A single smoke file:

```powershell
npx playwright test tests/smoke/t24-terminal.smoke.spec.ts --project=T24-R21-SYT --ui
```

The smoke test opens `/`, logs in, runs the enquiry command, and writes screenshots under `screenshots/`. That directory is git-ignored. Failure traces and results go to `test-results/` and `reports/`, which are also git-ignored. Tests run with one worker, a 120 second test timeout, and retries disabled.

## Layout

- `playwright.config.ts`: Edge channel, R21 and R26 projects, reporters.
- `pages/T24LoginPage.ts`: login actions and success check.
- `pages/TerminalPage.ts`: command line entry and target-screen wait.
- `helpers/KeyboardHelper.ts`: Enter, Tab, Shift+Tab, Escape, and F1-F12.
- `helpers/ScreenshotHelper.ts`: named evidence files and Playwright attachments.
- `tests/smoke/t24-terminal.smoke.spec.ts`: `T24-SMOKE-001`.

## Security

Never commit credentials, T24 URLs, account numbers, customer information, transaction IDs, XML payloads, screenshots, traces, or reports. Keep proprietary selectors out of this repository.
