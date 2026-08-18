

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_hybrid_search "High blood pressure damages kidney function"
Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 547.48it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Candidate depth per system: 30

Rank: 1
Document ID: 8318922
RRF score: 0.032787
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 6157837
RRF score: 0.031054
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 3
Document ID: 202259
RRF score: 0.030366
Title: Effect of lowering blood pressure on cardiovascular events and mortality in patients on dialysis: a systematic review and meta-analysis of randomised controlled trials
Excerpt: BACKGROUND Patients undergoing dialysis have a substantially increased risk of cardiovascular mortality and morbidity. Although several trials have shown the cardiovascular benefits of lowering blood pressure in the general population, there is uncer...

Rank: 4
Document ID: 24998764
RRF score: 0.030118
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 5
Document ID: 11071351
RRF score: 0.028718
Title: Primary prevention of hypertension: clinical and public health advisory from The National High Blood Pressure Education Program.
Excerpt: The National High Blood Pressure Education Program Coordinating Committee published its first statement on the primary prevention of hypertension in 1993. This article updates the 1993 report, using new and further evidence from the scientific litera...

Rank: 6
Document ID: 19804204
RRF score: 0.028571
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
Excerpt: BACKGROUND AND OBJECTIVES Children with chronic kidney disease (CKD) are at risk for cognitive dysfunction, and over half have hypertension. Data on the potential contribution of hypertension to CKD-associated neurocognitive deficits in children are ...

Rank: 7
Document ID: 26025820
RRF score: 0.027673
Title: Induction of AMPK activity corrects early pathophysiological alterations in the subtotal nephrectomy model of chronic kidney disease.
Excerpt: The rat kidney ablation and infarction (A/I) model of subtotal or 5/6th nephrectomy is the most commonly studied model of nondiabetic chronic kidney disease (CKD). The A/I kidney at 1 wk exhibits reductions in kidney function, as determined by glomer...

Rank: 8
Document ID: 25104843
RRF score: 0.027052
Title: Hemoperfusion-hemodialysis ineffective for paraquat removal in life-threatening poisoning?
Excerpt: We report on a patient treated with hemoperfusion-hemodialysis (HP-HD) for severe paraquat poisoning. This procedure was adopted since the combination of adsorption and dialysis may improve overall drug removal. On admission blood paraquat was 15.8 m...

Rank: 9
Document ID: 21859699
RRF score: 0.026084
Title: Successful three-way kidney paired donation with cross-country live donor allograft transport.
Excerpt: Providing transplantation opportunities for patients with incompatible live donors through kidney paired donation (KPD) is seen as one of the important strategies for easing the crisis in organ availability. It has been estimated that an additional 1...

Rank: 10
Document ID: 39368721
RRF score: 0.023393
Title: Glucose tolerance and blood pressure: long term follow up in middle aged men.
Excerpt: OBJECTIVE to investigate the role of glucose tolerance in the development of hypertension. DESIGN Retrospective analysis of the results of a health check up in a group of clinically healthy middle aged men in the late 1960s (median year 1968). The su...
```

With 50 candidates
```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_hybrid_search "High blood pressure damages kidney function" --candidate-k 50
Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 598.31it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Candidate depth per system: 50

Rank: 1
Document ID: 8318922
RRF score: 0.032787
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 6157837
RRF score: 0.031054
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 3
Document ID: 202259
RRF score: 0.030366
Title: Effect of lowering blood pressure on cardiovascular events and mortality in patients on dialysis: a systematic review and meta-analysis of randomised controlled trials
Excerpt: BACKGROUND Patients undergoing dialysis have a substantially increased risk of cardiovascular mortality and morbidity. Although several trials have shown the cardiovascular benefits of lowering blood pressure in the general population, there is uncer...

Rank: 4
Document ID: 24998764
RRF score: 0.030118
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 5
Document ID: 11071351
RRF score: 0.028718
Title: Primary prevention of hypertension: clinical and public health advisory from The National High Blood Pressure Education Program.
Excerpt: The National High Blood Pressure Education Program Coordinating Committee published its first statement on the primary prevention of hypertension in 1993. This article updates the 1993 report, using new and further evidence from the scientific litera...

Rank: 6
Document ID: 19804204
RRF score: 0.028571
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
Excerpt: BACKGROUND AND OBJECTIVES Children with chronic kidney disease (CKD) are at risk for cognitive dysfunction, and over half have hypertension. Data on the potential contribution of hypertension to CKD-associated neurocognitive deficits in children are ...

Rank: 7
Document ID: 26025820
RRF score: 0.027673
Title: Induction of AMPK activity corrects early pathophysiological alterations in the subtotal nephrectomy model of chronic kidney disease.
Excerpt: The rat kidney ablation and infarction (A/I) model of subtotal or 5/6th nephrectomy is the most commonly studied model of nondiabetic chronic kidney disease (CKD). The A/I kidney at 1 wk exhibits reductions in kidney function, as determined by glomer...

Rank: 8
Document ID: 25104843
RRF score: 0.027052
Title: Hemoperfusion-hemodialysis ineffective for paraquat removal in life-threatening poisoning?
Excerpt: We report on a patient treated with hemoperfusion-hemodialysis (HP-HD) for severe paraquat poisoning. This procedure was adopted since the combination of adsorption and dialysis may improve overall drug removal. On admission blood paraquat was 15.8 m...

Rank: 9
Document ID: 21859699
RRF score: 0.026084
Title: Successful three-way kidney paired donation with cross-country live donor allograft transport.
Excerpt: Providing transplantation opportunities for patients with incompatible live donors through kidney paired donation (KPD) is seen as one of the important strategies for easing the crisis in organ availability. It has been estimated that an additional 1...

Rank: 10
Document ID: 41298619
RRF score: 0.025904
Title: Hydroxyethyl starch (HES) versus other fluid therapies: effects on kidney function.
Excerpt: BACKGROUND Hydroxyethyl starches (HES) are synthetic colloids commonly used for fluid resuscitation, yet controversy exists about their impact on kidney function. OBJECTIVES To examine the effects of HES on kidney function compared to other fluid res...
```

Experiment Comparing

```
BM25
Dense
Hybrid with 20 candidates per system
Hybrid with 30 candidates per system
Hybrid with 50 candidates per system
```

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.compare_hybrid_retrievers --split test
Loaded 5183 documents
Evaluating 300 queries from the test split

Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 533.47it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Evaluating BM25...
Evaluating dense retrieval...

Evaluating hybrid retrieval with candidate depth 20...

Evaluating hybrid retrieval with candidate depth 30...

Evaluating hybrid retrieval with candidate depth 50...

Pipeline               Recall@10      MRR@10     nDCG@10    Latency ms
bm25                      0.7740      0.6186      0.6519         27.73
dense                     0.6393      0.4488      0.4870         20.48
hybrid_rrf_20             0.8278      0.6091      0.6543         49.24
hybrid_rrf_30             0.8171      0.6049      0.6486         47.93
hybrid_rrf_50             0.7804      0.5924      0.6311         49.98

Saved results to results/day3_test_comparison.json
```

Did hybrid improve Recall@10?
Did it improve the position of the first relevant result?
Did nDCG@10 improve?
How much latency did fusion add?
Did increasing from 30 to 50 candidates provide a meaningful benefit?

| Question                                                         | Answer                        | Evidence                                                              |
| ---------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------- |
| **1. Did hybrid improve Recall@10?**                             | ✅ **Yes**                     | BM25: **0.7740** → Hybrid-20: **0.8278**                              |
| **2. Did it improve the position of the first relevant result?** | ❌ **No**                      | MRR@10: BM25 **0.6186** → Hybrid-20 **0.6091**                        |
| **3. Did nDCG@10 improve?**                                      | ✅ **Slightly**                | BM25: **0.6519** → Hybrid-20: **0.6543**                              |
| **4. How much latency did fusion add?**                          | ≈ **2.02 ms fusion overhead** | BM25 + Dense = 30.42 + 19.51 = **49.93 ms**; Hybrid-20 = **51.95 ms** |
| **5. Did 30 → 50 candidates help?**                              | ❌ **No**                      | Recall, MRR, and nDCG all decreased                                   |

