---
name: quant-research-lab
description: Build reproducible portfolio, risk, market-data, and time-series analyses from statements, holdings, CSVs, or price data.
---

# Quant research lab

## Workflow

1. Establish the authoritative source-of-truth snapshot and valuation date.
2. Normalize identifiers, quantities, currencies, timestamps, and missing values without silently mutating source fields.
3. Record market-data provider, field, adjustment method, frequency, and retrieval time.
4. Perform only methods relevant to the stated decision: returns, exposure, volatility, drawdown, dependence, factor/risk analysis, hypothesis tests, bootstrap, stress/scenario analysis.
5. Independently reconcile at least one portfolio total or key statistic.
6. Use frozen fixtures for tests and live data only when freshness is required.
7. Prefer a reproducible notebook/script with visible parameters and provenance.
8. State model assumptions separately from observed results.

## Failure conditions

Do not finalize when positions do not reconcile, units/dates remain ambiguous, or a claimed statistic cannot be reproduced within a stated tolerance.
