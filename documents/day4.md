```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_reranked_search "High blood pressure damages kidney function"
Loaded 5183 documents
Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 630.65it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()
Loading cross-encoder...
config.json: 100%|███████████████████████████████████| 794/794 [00:00<00:00, 1.16MB/s]
model.safetensors: downloading bytes: ████████████████████████████| 86.0MB, 5.87MB/s
model.safetensors: reconstructing file: 100%|████████████| 90.9MB / 90.9MB, 7.56MB/s
Loading weights: 100%|█████████████████████████████| 105/105 [00:00<00:00, 794.91it/s]
tokenizer_config.json: 100%|█████████████████████| 1.33k/1.33k [00:00<00:00, 2.07MB/s]
vocab.txt: 100%|███████████████████████████████████| 232k/232k [00:00<00:00, 9.97MB/s]
tokenizer.json: 100%|██████████████████████████████| 711k/711k [00:00<00:00, 39.7MB/s]
special_tokens_map.json: 100%|████████████████████████| 132/132 [00:00<00:00, 564kB/s]

Total online latency: 2534.44 ms
Reranked 20 hybrid candidates into 10 results

Rank: 1
Document ID: 8318922
Cross-encoder score: 0.711435
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 24998764
Cross-encoder score: 0.624641
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 3
Document ID: 19804204
Cross-encoder score: 0.350599
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
Excerpt: BACKGROUND AND OBJECTIVES Children with chronic kidney disease (CKD) are at risk for cognitive dysfunction, and over half have hypertension. Data on the potential contribution of hypertension to CKD-associated neurocognitive deficits in children are ...

Rank: 4
Document ID: 6157837
Cross-encoder score: 0.237503
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 5
Document ID: 43557480
Cross-encoder score: 0.030747
Title: Arterial hypertension and progression of chronic kidney disease in children during 10-year ambulatory observation.
Excerpt: The aim of this study was the long-term retrospective analysis of chronic kidney disease (CKD) progression in children, especially with regard to the presence of hypertension (HTN). The average rate of progression of CKD was higher in patients with H...

Rank: 6
Document ID: 21616324
Cross-encoder score: 0.021973
Title: Systemic arterial hypertension in children following renal transplantation: prevalence and risk factors.
Excerpt: BACKGROUND Control of blood pressure (BP) following renal transplantation may improve allograft and patient survival. Our aims were (i) to describe the distribution of BP and the prevalence of systolic and/or diastolic hypertension in children over t...

Rank: 7
Document ID: 4506414
Cross-encoder score: 0.014969
Title: Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1·25 million people
Excerpt: BACKGROUND The associations of blood pressure with the different manifestations of incident cardiovascular disease in a contemporary population have not been compared. In this study, we aimed to analyse the associations of blood pressure with 12 diff...

Rank: 8
Document ID: 23377475
Cross-encoder score: 0.006635
Title: Acute kidney injury and chronic kidney disease: an integrated clinical syndrome.
Excerpt: The previous conventional wisdom that survivors of acute kidney injury (AKI) tend to do well and fully recover renal function appears to be flawed. AKI can cause end-stage renal disease (ESRD) directly, and increase the risk of developing incident ch...

Rank: 9
Document ID: 41298619
Cross-encoder score: 0.004561
Title: Hydroxyethyl starch (HES) versus other fluid therapies: effects on kidney function.
Excerpt: BACKGROUND Hydroxyethyl starches (HES) are synthetic colloids commonly used for fluid resuscitation, yet controversy exists about their impact on kidney function. OBJECTIVES To examine the effects of HES on kidney function compared to other fluid res...

Rank: 10
Document ID: 25974070
Cross-encoder score: 0.002505
Title: Dietary saturated and unsaturated fats as determinants of blood pressure and vascular function.
Excerpt: The amount and type of dietary fat have long been associated with the risk of CVD. Arterial stiffness and endothelial dysfunction are important risk factors in the aetiology of CHD. A range of methods exists to assess vascular function that may be us...
```

```
(.venv) psych@DESKTOP-PLHPE5G:~/hybrid-evidence-search$ python -m scripts.run_reranked_search "High blood pressure damages kidney function" --top-k 20
Loaded 5183 documents
Building BM25 retriever...
Loading dense retriever...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████| 103/103 [00:00<00:00, 776.13it/s]
/home/psych/hybrid-evidence-search/src/dense_retriever.py:33: FutureWarning: The `get_sentence_embedding_dimension` method has been renamed to `get_embedding_dimension`.
  model_dimension = self.model.get_sentence_embedding_dimension()
Loading cross-encoder...
Loading weights: 100%|█████████████████████████████| 105/105 [00:00<00:00, 773.48it/s]

Total online latency: 2518.67 ms
Reranked 20 hybrid candidates into 20 results

Rank: 1
Document ID: 8318922
Cross-encoder score: 0.711435
Title: Relationship of ambulatory blood pressure and the heart rate profile with renal function parameters in hypertensive patients with chronic kidney disease.
Excerpt: Strict blood pressure (BP) control is reportedly important for the management of hypertensive patients with chronic kidney disease (CKD). The purpose of this cross-sectional study was to examine whether the variables of ambulatory BP and the heart ra...

Rank: 2
Document ID: 24998764
Cross-encoder score: 0.624641
Title: Relation between renal function within the normal range and central and peripheral arterial stiffness in hypertension.
Excerpt: Chronic kidney disease is accompanied by increased large-artery stiffness, but the relation between glomerular filtration rate within the reference range and central or peripheral arterial stiffness has been understudied. The link between renal funct...

Rank: 3
Document ID: 19804204
Cross-encoder score: 0.350599
Title: Casual blood pressure and neurocognitive function in children with chronic kidney disease: a report of the children with chronic kidney disease cohort study.
Excerpt: BACKGROUND AND OBJECTIVES Children with chronic kidney disease (CKD) are at risk for cognitive dysfunction, and over half have hypertension. Data on the potential contribution of hypertension to CKD-associated neurocognitive deficits in children are ...

Rank: 4
Document ID: 6157837
Cross-encoder score: 0.237503
Title: Renal considerations in angiotensin converting enzyme inhibitor therapy: a statement for healthcare professionals from the Council on the Kidney in Cardiovascular Disease and the Council for High Blood Pressure Research of the American Heart Association.
Excerpt: Angiotensin converting enzyme (ACE) inhibitors are now one of the most frequently used classes of antihypertensive drugs. Beyond their utility in the management of hypertension, their use has been extended to the long-term management of patients with...

Rank: 5
Document ID: 43557480
Cross-encoder score: 0.030747
Title: Arterial hypertension and progression of chronic kidney disease in children during 10-year ambulatory observation.
Excerpt: The aim of this study was the long-term retrospective analysis of chronic kidney disease (CKD) progression in children, especially with regard to the presence of hypertension (HTN). The average rate of progression of CKD was higher in patients with H...

Rank: 6
Document ID: 21616324
Cross-encoder score: 0.021973
Title: Systemic arterial hypertension in children following renal transplantation: prevalence and risk factors.
Excerpt: BACKGROUND Control of blood pressure (BP) following renal transplantation may improve allograft and patient survival. Our aims were (i) to describe the distribution of BP and the prevalence of systolic and/or diastolic hypertension in children over t...

Rank: 7
Document ID: 4506414
Cross-encoder score: 0.014969
Title: Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1·25 million people
Excerpt: BACKGROUND The associations of blood pressure with the different manifestations of incident cardiovascular disease in a contemporary population have not been compared. In this study, we aimed to analyse the associations of blood pressure with 12 diff...

Rank: 8
Document ID: 23377475
Cross-encoder score: 0.006635
Title: Acute kidney injury and chronic kidney disease: an integrated clinical syndrome.
Excerpt: The previous conventional wisdom that survivors of acute kidney injury (AKI) tend to do well and fully recover renal function appears to be flawed. AKI can cause end-stage renal disease (ESRD) directly, and increase the risk of developing incident ch...

Rank: 9
Document ID: 41298619
Cross-encoder score: 0.004561
Title: Hydroxyethyl starch (HES) versus other fluid therapies: effects on kidney function.
Excerpt: BACKGROUND Hydroxyethyl starches (HES) are synthetic colloids commonly used for fluid resuscitation, yet controversy exists about their impact on kidney function. OBJECTIVES To examine the effects of HES on kidney function compared to other fluid res...

Rank: 10
Document ID: 25974070
Cross-encoder score: 0.002505
Title: Dietary saturated and unsaturated fats as determinants of blood pressure and vascular function.
Excerpt: The amount and type of dietary fat have long been associated with the risk of CVD. Arterial stiffness and endothelial dysfunction are important risk factors in the aetiology of CHD. A range of methods exists to assess vascular function that may be us...

Rank: 11
Document ID: 202259
Cross-encoder score: 0.002391
Title: Effect of lowering blood pressure on cardiovascular events and mortality in patients on dialysis: a systematic review and meta-analysis of randomised controlled trials
Excerpt: BACKGROUND Patients undergoing dialysis have a substantially increased risk of cardiovascular mortality and morbidity. Although several trials have shown the cardiovascular benefits of lowering blood pressure in the general population, there is uncer...

Rank: 12
Document ID: 24049225
Cross-encoder score: 0.000899
Title: No net renal extraction of homocysteine in fasting humans.
Excerpt: BACKGROUND The pathophysiological mechanism of hyperhomocysteinemia in chronic renal failure in humans is unknown. The loss of a putative renal homocysteine extraction in chronic renal failure has been hypothesized as significant homocysteine uptake ...

Rank: 13
Document ID: 26025820
Cross-encoder score: 0.000896
Title: Induction of AMPK activity corrects early pathophysiological alterations in the subtotal nephrectomy model of chronic kidney disease.
Excerpt: The rat kidney ablation and infarction (A/I) model of subtotal or 5/6th nephrectomy is the most commonly studied model of nondiabetic chronic kidney disease (CKD). The A/I kidney at 1 wk exhibits reductions in kidney function, as determined by glomer...

Rank: 14
Document ID: 27466734
Cross-encoder score: 0.000833
Title: Development and validation of QRISK3 risk prediction algorithms to estimate future risk of cardiovascular disease: prospective cohort study
Excerpt: Objectives To develop and validate updated QRISK3 prediction algorithms to estimate the 10 year risk of cardiovascular disease in women and men accounting for potential new risk factors. Design Prospective open cohort study. Setting General practices...

Rank: 15
Document ID: 54490092
Cross-encoder score: 0.000786
Title: Impact of blood pressure variability on cardiovascular events in elderly patients with hypertension.
Excerpt: Blood pressure variability is one of the characteristic features of hypertension in the elderly. However, its clinical significance remains to be determined. We therefore examined the impact of blood pressure variability on the development of cardiov...

Rank: 16
Document ID: 39368721
Cross-encoder score: 0.000786
Title: Glucose tolerance and blood pressure: long term follow up in middle aged men.
Excerpt: OBJECTIVE to investigate the role of glucose tolerance in the development of hypertension. DESIGN Retrospective analysis of the results of a health check up in a group of clinically healthy middle aged men in the late 1960s (median year 1968). The su...

Rank: 17
Document ID: 11071351
Cross-encoder score: 0.000326
Title: Primary prevention of hypertension: clinical and public health advisory from The National High Blood Pressure Education Program.
Excerpt: The National High Blood Pressure Education Program Coordinating Committee published its first statement on the primary prevention of hypertension in 1993. This article updates the 1993 report, using new and further evidence from the scientific litera...

Rank: 18
Document ID: 25104843
Cross-encoder score: 0.000218
Title: Hemoperfusion-hemodialysis ineffective for paraquat removal in life-threatening poisoning?
Excerpt: We report on a patient treated with hemoperfusion-hemodialysis (HP-HD) for severe paraquat poisoning. This procedure was adopted since the combination of adsorption and dialysis may improve overall drug removal. On admission blood paraquat was 15.8 m...

Rank: 19
Document ID: 53779698
Cross-encoder score: 0.000071
Title: Exercise as a therapeutic approach to improve blood pressure in patients with peripheral arterial disease: current literature and future directions.
Excerpt: INTRODUCTION Patients with symptomatic peripheral artery disease (PAD) exhibit reduced functional capacity and increased mortality due to cardiovascular disease. Although exercise has been a cornerstone for clinical treatment to improve walking capac...

Rank: 20
Document ID: 21859699
Cross-encoder score: 0.000020
Title: Successful three-way kidney paired donation with cross-country live donor allograft transport.
Excerpt: Providing transplantation opportunities for patients with incompatible live donors through kidney paired donation (KPD) is seen as one of the important strategies for easing the crisis in organ availability. It has been estimated that an additional 1...
```

Comparison results for Reranker
```
Pipeline                 Recall@10      MRR@10     nDCG@10    Latency ms
bm25                        0.7740      0.6186      0.6519         26.69
dense                       0.6393      0.4488      0.4870         19.47
hybrid                      0.8171      0.6049      0.6486         49.19
hybrid_reranker             0.8328      0.6676      0.6998       2242.08
```
