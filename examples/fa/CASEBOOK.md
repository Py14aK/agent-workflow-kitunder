# 23-case pack 2026-09-29

Deployed from the Vassil owner table and the handwritten arrow board.
No Word FSD, no BRD, no catalog slice. Every product FIELD is unmatched.

| Case | FSD_ID | Epic | Owner | Machine | Class | Collision |
|---:|---|---|---|---|---|---|
| 01 | UBBPMA1 | TSC-28363 | Reni-Antonio | E_BRIEFING | payments-adjacent UNKNOWN subtype | no |
| 02 | UBBPMBDG | TSC-17856 | Neda | E_BRIEFING | budget | no |
| 03 | UBBPMFCY05 | UNKNOWN | UNKNOWN | C_NON_EU | foreign-currency | no |
| 04 | UBBCSHAD | TSC-30860 | Niki | A_PERMISSION | cash | no |
| 05 | UBBCSHMN | TSC-17854 | Reni | E_BRIEFING | cash-management | YES |
| 06 | UBBPMDD | TSC-17855 | Antonio | D_STRUCTURE | direct-debits | YES |
| 07 | UBBPMBLK | TSC-17865 | Vassil | E_BRIEFING | bulk | no |
| 08 | UBBPMINTL | TSC-17852 | Antonio | B_VOP | international | no |
| 09 | UBBPMPRL | TSC-17866 | Antonio | C_NON_EU | payroll | no |
| 10 | UBBPMENTF | TSC-17666 | Reni | D_STRUCTURE | entry-fees | no |
| 11 | UBBSFBXS | TSC-22973 | Garbis | D_STRUCTURE | safe-boxes | no |
| 12 | UBBPMNR | TSC-17858 | Reni | C_NON_EU | non-resident | no |
| 13 | UBBPMFCY02 | TSC-17867 | Niki | A_PERMISSION | foreign-currency | no |
| 14 | UBBPMFCY03 | TSC-17849 | Neda | C_NON_EU | foreign-currency | no |
| 15 | UBBPMSMS | TSC-17850 | Niki | A_PERMISSION | notifications | no |
| 16 | UBBPMSTO | TSC-21194 | Niki | A_PERMISSION | standing-orders | no |
| 17 | UBBPMFCY01 | TSC-17863 | Neda | C_NON_EU | foreign-currency | no |
| 18 | UBBPMFCY04 | TSC-17848 | Niki | A_PERMISSION | foreign-currency | no |
| 19 | UBBCSHTLR | TSC-17851 | Garbis | D_STRUCTURE | cashier | no |
| 20 | UBBPMINS | TSC-17862 | Reni | D_STRUCTURE | insurance | no |
| 21 | UBBPMUTL | TSC-17853 | Vassil | E_BRIEFING | utilities | no |
| 22 | UBBPMWRN | TSC-17864 | Vassil | E_BRIEFING | warnings | no |
| 23 | UNKNOWN | TSC-30913 | Garbis | D_STRUCTURE | unnamed | no |

## Machines

- `A_PERMISSION`: Morning -> DACS 08:45 -> ASK Niki -> Jira / ASK -> Outsourcing
- `B_VOP`: VOP -> BOP / Ed 103 ; VOP -> 1st package ; PHASE 3 -> do A/od -> Fix
- `C_NON_EU`: (11/13) Payl. -> sept WT/SYNET -> NOT EU 818000$ ; FC -> AN / BIC
- `D_STRUCTURE`: update docs -> LAP ; Hold -> Scaffolding ; Mapping / SCRUB / wiki
- `E_BRIEFING`: how to answer -> VASKO | PANI/RENI? | ASI ; DATA -> CMB joins ; DATA -> followup -> UMP

## Locks

- TSC-17855 stays COLLISION. No winner.
- VoP Phase 2 TSC-46573 is not UBBPMINTL.
- Case 23 FSD_ID stays UNKNOWN.
- Identifiers are not renamed.

## Next catalog order

1. UBBPMINTL
2. UBBCSHMN
3. UBBPMDD
4. UBBPMFCY01
5. UBBPMPRL
