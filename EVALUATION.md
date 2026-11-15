# Evaluation

Run `npm test` or `node tests/evaluate.mjs`. The script writes real results to public/reports/evaluation.json and fixtures to tests/fixtures/benchmark.json. The live docs read those results.

## 60 developer-authored synthetic cases
- 20 name/date comparison cases: formatting equivalence versus real spelling/date differences.
- 15 conditional requirement cases: seven binary conditions and one under-six case.
- 15 unknown, sensitive, negated or extra-document requests, expected to abstain.
- 10 noisy **text** extraction cases. These do not measure raw-image OCR.

Expected labels are implemented-case expectations, not independent expert legal annotations. Safety assertions also cover confirmation gates, missing values, impossible and ambiguous dates, synthetic markers, unknown actions, source allowlist, review state and letter non-submission text.

Metrics include mismatch precision/recall, comparison accuracy, conditional applicability accuracy, unknown-request abstention and text field extraction accuracy. The exact-string baseline does not normalize case, spaces or Bangla digits. Actual numbers and run duration are in the JSON; no external or production accuracy claim is made.

## Not measured
Real-document OCR accuracy, multilingual OCR fairness, independent citation correctness, unseen semantic query relevance, model token use, provider cost, production latency, citizen outcomes or legal correctness. Browser smoke tests are separately recorded in docs/QA.md.
