### Day 2

dense latency measured by `evaluate()` is Query encoding + FAISS search.

For BM25, Query tokenization + BM25 scoring + top-K selection.

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.compare_retrievers
Loaded 5183 documents
Evaluating 300 test queries

Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|███████████| 103/103 [00:00<00:00, 684.58it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Evaluating BM25...
Evaluating dense retrieval...

Results
Pipeline       Recall@10      MRR@10     nDCG@10       Latency
bm25              0.7740      0.6186      0.6519      26.89 ms
dense             0.6393      0.4488      0.4870      19.06 ms

Saved comparison to results/retrieval_comparison.json
```

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_search "High blood pressure damages kidney function"

Rank: 1
Document ID: 8318922
Score: 17.3625
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 6157837
Score: 15.8316
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 3
Document ID: 25974070
Score: 15.1101
Title: Dietary saturated and unsaturated fats as determinants of blood pressure and vascular function.
Excerpt: The amount and type of dietary fat have long been associated with the risk of CVD. Arterial stiffness and endothelial dysfunction are important risk factors in the aetiology of CHD. A range of methods exists to assess vascular function that may be us...

Rank: 4
Document ID: 24998764
Score: 15.0097
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 5
Document ID: 11071351
Score: 14.9783
Title: Primary prevention of hypertension: clinical and public health advisory from The National High Blood Pressure Education Program.
Excerpt: The National High Blood Pressure Education Program Coordinating Committee published its first statement on the primary prevention of hypertension in 1993. This article updates the 1993 report, using new and further evidence from the scientific litera...

Rank: 6
Document ID: 4506414
Score: 14.6509
Title: Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1·25 million people
Excerpt: BACKGROUND The associations of blood pressure with the different manifestations of incident cardiovascular disease in a contemporary population have not been compared. In this study, we aimed to analyse the associations of blood pressure with 12 diff...

Rank: 7
Document ID: 54490092
Score: 14.6036
Title: Impact of blood pressure variability on cardiovascular events in elderly patients with hypertension.
Excerpt: Blood pressure variability is one of the characteristic features of hypertension in the elderly. However, its clinical significance remains to be determined. We therefore examined the impact of blood pressure variability on the development of cardiov...

Rank: 8
Document ID: 27466734
Score: 14.5182
Title: Development and validation of QRISK3 risk prediction algorithms to estimate future risk of cardiovascular disease: prospective cohort study
Excerpt: Objectives To develop and validate updated QRISK3 prediction algorithms to estimate the 10 year risk of cardiovascular disease in women and men accounting for potential new risk factors. Design Prospective open cohort study. Setting General practices...

Rank: 9
Document ID: 202259
Score: 13.9661
Title: Effect of lowering blood pressure on cardiovascular events and mortality in patients on dialysis: a systematic review and meta-analysis of randomised controlled trials
Excerpt: BACKGROUND Patients undergoing dialysis have a substantially increased risk of cardiovascular mortality and morbidity. Although several trials have shown the cardiovascular benefits of lowering blood pressure in the general population, there is uncer...

Rank: 10
Document ID: 19804204
Score: 13.5386
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
Excerpt: BACKGROUND AND OBJECTIVES Children with chronic kidney disease (CKD) are at risk for cognitive dysfunction, and over half have hypertension. Data on the potential contribution of hypertension to CKD-associated neurocognitive deficits in children are ...
```

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_dense_search "High blood pressure damages kidney function"
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|███████████| 103/103 [00:00<00:00, 958.10it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Rank: 1
Document ID: 8318922
Cosine similarity: 0.4842
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 43557480
Cosine similarity: 0.4487
Title: Arterial hypertension and progression of chronic kidney disease in children during 10-year ambulatory observation.
Excerpt: The aim of this study was the long-term retrospective analysis of chronic kidney disease (CKD) progression in children, especially with regard to the presence of hypertension (HTN). The average rate of progression of CKD was higher in patients with H...

Rank: 3
Document ID: 202259
Cosine similarity: 0.4471
Title: Effect of lowering blood pressure on cardiovascular events and mortality in patients on dialysis: a systematic review and meta-analysis of randomised controlled trials
Excerpt: BACKGROUND Patients undergoing dialysis have a substantially increased risk of cardiovascular mortality and morbidity. Although several trials have shown the cardiovascular benefits of lowering blood pressure in the general population, there is uncer...

Rank: 4
Document ID: 26025820
Cosine similarity: 0.4341
Title: Induction of AMPK activity corrects early pathophysiological alterations in the subtotal nephrectomy model of chronic kidney disease.
Excerpt: The rat kidney ablation and infarction (A/I) model of subtotal or 5/6th nephrectomy is the most commonly studied model of nondiabetic chronic kidney disease (CKD). The A/I kidney at 1 wk exhibits reductions in kidney function, as determined by glomer...

Rank: 5
Document ID: 21616324
Cosine similarity: 0.4189
Title: Systemic arterial hypertension in children following renal transplantation: prevalence and risk factors.
Excerpt: BACKGROUND Control of blood pressure (BP) following renal transplantation may improve allograft and patient survival. Our aims were (i) to describe the distribution of BP and the prevalence of systolic and/or diastolic hypertension in children over t...

Rank: 6
Document ID: 41298619
Cosine similarity: 0.4185
Title: Hydroxyethyl starch (HES) versus other fluid therapies: effects on kidney function.
Excerpt: BACKGROUND Hydroxyethyl starches (HES) are synthetic colloids commonly used for fluid resuscitation, yet controversy exists about their impact on kidney function. OBJECTIVES To examine the effects of HES on kidney function compared to other fluid res...

Rank: 7
Document ID: 6157837
Cosine similarity: 0.3951
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 8
Document ID: 25104843
Cosine similarity: 0.3905
Title: Hemoperfusion-hemodialysis ineffective for paraquat removal in life-threatening poisoning?
Excerpt: We report on a patient treated with hemoperfusion-hemodialysis (HP-HD) for severe paraquat poisoning. This procedure was adopted since the combination of adsorption and dialysis may improve overall drug removal. On admission blood paraquat was 15.8 m...

Rank: 9
Document ID: 24998764
Cosine similarity: 0.3871
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 10
Document ID: 19804204
Cosine similarity: 0.3769
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
```

Does BM25 retrieve documents with more exact vocabulary?
- No.
Does dense retrieval find synonyms or paraphrases?
- Yes.
Does dense retrieval return topically similar but irrelevant documents?
- Yes.


Query `Vitamin D protects against respiratory infection`

BM25:
```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_search "V
itamin D protects against respiratory infection"

Rank: 1
Document ID: 6182947
Score: 18.3930
Title: Nrf2 protects human alveolar epithelial cells against injury induced by influenza A virus
Excerpt: BACKGROUND Influenza A virus (IAV) infection primarily targets respiratory epithelial cells and produces clinical outcomes ranging from mild upper respiratory infection to severe pneumonia. Recent studies have shown the importance of lung antioxidant...

Rank: 2
Document ID: 30720103
Score: 17.2351
Title: Vitamin D status: measurement, interpretation, and clinical application.
Excerpt: Vitamin D, the sunshine vitamin, is now recognized not only for its importance in promoting bone health in children and adults but also for other health benefits, including reducing the risk of chronic diseases such as autoimmune diseases, common can...

Rank: 3
Document ID: 23267371
Score: 17.0561
Title: Vitamin D: The "sunshine" vitamin.
Excerpt: Vitamin D insufficiency affects almost 50% of the population worldwide. An estimated 1 billion people worldwide, across all ethnicities and age groups, have a vitamin D deficiency (VDD). This pandemic of hypovitaminosis D can mainly be attributed to ...

Rank: 4
Document ID: 21553394
Score: 16.8844
Title: Vitamin D and obesity: current perspectives and future directions.
Excerpt: In recent years, new functional roles of vitamin D beyond its traditional role in calcium homoeostasis and bone metabolism have emerged linking the fat-soluble vitamin to various non-communicable diseases. Vitamin D deficiency (25-hydroxyvitamin D (2...

Rank: 5
Document ID: 36960449
Score: 16.8760
Title: Estimation of the dietary requirement for vitamin D in healthy adults.
Excerpt: BACKGROUND Knowledge gaps have contributed to considerable variation among international dietary recommendations for vitamin D.   OBJECTIVE We aimed to establish the distribution of dietary vitamin D required to maintain serum 25-hydroxyvitamin D [25...

Rank: 6
Document ID: 12074066
Score: 16.8754
Title: Vitamin D and prevention of colorectal cancer.
Excerpt: BACKGROUND Inadequate photosynthesis or oral intake of Vitamin D are associated with high incidence rates of colorectal cancer, but the dose-response relationship has not been adequately studied. METHODS Dose-response gradients from observational stu...

Rank: 7
Document ID: 22843838
Score: 16.7670
Title: [Vitamin D and latitude as environmental factors in multiple sclerosis].
Excerpt: Multiple sclerosis (MS) shows a multifold increase in prevalence with an increase in latitudes, both north and south of the equator. One of the potential factors related to the difference of the prevalence is vitamin D, because the strength of ambien...

Rank: 8
Document ID: 16256507
Score: 16.5760
Title: Relationship between serum parathyroid hormone levels, vitamin D sufficiency, and calcium intake.
Excerpt: CONTEXT Adequate vitamin D status for optimum bone health has received increased recognition in recent years; however, the ideal intake is not known. Serum 25-hydroxyvitamin D is the generally accepted indicator of vitamin D status, but no universal ...

Rank: 9
Document ID: 38551172
Score: 16.2370
Title: Mammographic density, plasma vitamin D levels and risk of breast cancer in postmenopausal women.
Excerpt: Mammographic density is a strong risk factor for breast cancer, but the underlying biology for this association is unknown. Studies suggest that vitamin D may reduce breast cancer risk and dietary vitamin D intake has been associated with reduced bre...

Rank: 10
Document ID: 4462079
Score: 16.1773
Title: Estimation of optimal serum concentrations of 25-hydroxyvitamin D for multiple health outcomes.
```
Dense:
```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_dense_search "Vitamin D protects against respiratory infection"
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 450.99it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Rank: 1
Document ID: 23267371
Cosine similarity: 0.5889
Title: Vitamin D: The "sunshine" vitamin.
Excerpt: Vitamin D insufficiency affects almost 50% of the population worldwide. An estimated 1 billion people worldwide, across all ethnicities and age groups, have a vitamin D deficiency (VDD). This pandemic of hypovitaminosis D can mainly be attributed to ...

Rank: 2
Document ID: 30720103
Cosine similarity: 0.5188
Title: Vitamin D status: measurement, interpretation, and clinical application.
Excerpt: Vitamin D, the sunshine vitamin, is now recognized not only for its importance in promoting bone health in children and adults but also for other health benefits, including reducing the risk of chronic diseases such as autoimmune diseases, common can...

Rank: 3
Document ID: 22843838
Cosine similarity: 0.4689
Title: [Vitamin D and latitude as environmental factors in multiple sclerosis].
Excerpt: Multiple sclerosis (MS) shows a multifold increase in prevalence with an increase in latitudes, both north and south of the equator. One of the potential factors related to the difference of the prevalence is vitamin D, because the strength of ambien...

Rank: 4
Document ID: 6182947
Cosine similarity: 0.4617
Title: Nrf2 protects human alveolar epithelial cells against injury induced by influenza A virus
Excerpt: BACKGROUND Influenza A virus (IAV) infection primarily targets respiratory epithelial cells and produces clinical outcomes ranging from mild upper respiratory infection to severe pneumonia. Recent studies have shown the importance of lung antioxidant...

Rank: 5
Document ID: 275294
Cosine similarity: 0.4557
Title: Environmental factors that influence the cutaneous production of vitamin D
Excerpt: All vertebrates, including humans, obtain most of their daily vitamin D requirement from casual exposure to sunlight. During exposure to sunlight, the solar ultraviolet B photons (290-315 nm) penetrate into the skin where they cause the photolysis of...

Rank: 6
Document ID: 21553394
Cosine similarity: 0.4495
Title: Vitamin D and obesity: current perspectives and future directions.
Excerpt: In recent years, new functional roles of vitamin D beyond its traditional role in calcium homoeostasis and bone metabolism have emerged linking the fat-soluble vitamin to various non-communicable diseases. Vitamin D deficiency (25-hydroxyvitamin D (2...

Rank: 7
Document ID: 12009265
Cosine similarity: 0.4471
Title: Vitamins E and C in the prevention of prostate and total cancer in men: the Physicians' Health Study II randomized controlled trial.
Excerpt: CONTEXT Many individuals take vitamins in the hopes of preventing chronic diseases such as cancer, and vitamins E and C are among the most common individual supplements. A large-scale randomized trial suggested that vitamin E may reduce risk of prost...

Rank: 8
Document ID: 12074066
Cosine similarity: 0.4442
Title: Vitamin D and prevention of colorectal cancer.
Excerpt: BACKGROUND Inadequate photosynthesis or oral intake of Vitamin D are associated with high incidence rates of colorectal cancer, but the dose-response relationship has not been adequately studied. METHODS Dose-response gradients from observational stu...

Rank: 9
Document ID: 36960449
Cosine similarity: 0.4324
Title: Estimation of the dietary requirement for vitamin D in healthy adults.
Excerpt: BACKGROUND Knowledge gaps have contributed to considerable variation among international dietary recommendations for vitamin D.   OBJECTIVE We aimed to establish the distribution of dietary vitamin D required to maintain serum 25-hydroxyvitamin D [25...

Rank: 10
Document ID: 9555784
Cosine similarity: 0.4161
Title: Vitamin d deficiency in postmenopausal women - biological correlates.
Excerpt: INTRODUCTION Low vitamin D (VD) is associated with secondary hyperparathyroidism and both contribute to deleterious consequences (reduced bone mineral density (BMD), risk of fractures and falls). OBJECTIVE To study the VD status and biological correl...
```

Document qrels script in `scripts.debug_dense_query`

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.debug_dense_query
Loaded 5183 documents
Evaluating 300 test queries
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 667.51it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()

Query ID: 1
Query: 0-dimensional biomaterials show inductive properties.
Relevant document IDs: {'31715818'}

Rank 1: Document 54561709 | Score 0.4466
Rank 2: Document 10342807 | Score 0.4258
Rank 3: Document 37437064 | Score 0.4155
Rank 4: Document 38037690 | Score 0.4101
Rank 5: Document 6863070 | Score 0.4095
Rank 6: Document 121581019 | Score 0.3948
Rank 7: Document 40254495 | Score 0.3917
Rank 8: Document 4489217 | Score 0.3909
Rank 9: Document 59453688 | Score 0.3895
Rank 10: Document 2402323 | Score 0.3880
```

1. Does BM25 retrieve documents with more exact vocabulary?
Usually yes. BM25 strongly rewards matching words such as “blood pressure,” “kidney,” and “function.”

2. Does dense retrieval find synonyms or paraphrases?
Usually yes. For example, it may connect:
“high blood pressure” with “hypertension”
“kidney” with “renal”

3. Does dense retrieval return topically similar but irrelevant documents?
Sometimes yes. It may retrieve a document about kidney function that does not actually provide evidence for the particular claim.
