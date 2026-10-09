# T24 Playwright POC

Sanitized Playwright scaffold for Temenos T24 R21/R26 SYT testing.

## Security

- Never commit credentials, T24 URLs, account numbers, customer information, transaction IDs, XML payloads, screenshots, traces, or reports.
- Copy `.env.example` only to an approved local secret mechanism.
- Replace all `TODO_...` selectors using the existing working KHN automation.

## Work setup

```powershell
npm ci
npx playwright test --list
$env:T24_R21_URL="APPROVED_INTERNAL_URL"
$env:T24_INPUT_USERNAME="APPROVED_TEST_USER"
$env:T24_INPUT_PASSWORD="LOCAL_SECRET"
$env:T24_SMOKE_COMMAND="ENQ TXN.ENTRY"
npx playwright test tests/smoke/t24-terminal.smoke.spec.ts --project=T24-R21-SYT --ui
```

If the closed network cannot reach npm, use the Playwright and Node dependencies already approved and installed by IT. Do not attempt to bypass corporate network controls.
