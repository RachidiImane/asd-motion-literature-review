# ASD-motion-literature-review

This repository contains the **data and scripts used to screen and analyze literature** on the use of **Artificial Intelligence (AI), Machine Learning (ML), and Computer Vision for motion and motor behavior analysis in Autism Spectrum Disorder (ASD).**

The goal of this repository is to provide a **reproducible workflow for literature screening starting from raw database exports**.

---

# Repository Contents

## Data

The repository contains **three raw text files exported from scientific databases**:

- **scopus_export.txt**  
  Plain-text export of search results from **Scopus**.

- **pubmed_export.txt**  
  Plain-text export of search results from **PubMed**.

- **ieee_export.txt**  
  Plain-text export of search results from **IEEE Xplore**.

These files contain the **initial search results obtained from the literature query**.

---

# Scripts

Three Python scripts are provided to process the literature search results.

---

## 1. Parse database exports

**parse_records.py**

This script reads the **raw database exports** and extracts the relevant information for each paper, including:

- **Title**
- **DOI**
- **PMID** (when available)
- **Source database**

The script produces a **combined screening sheet** containing all retrieved records.

### Output 

autism_ai_screening_sheet_ALL168.xlsx

This file contains **all records from the three databases (168 papers)** with duplicates preserved.

---

## 2. Identify duplicate records

**identify_duplicates.py**

This script identifies **duplicate records across databases** using the **DOI as the primary identifier**.

If DOI is missing, the script can optionally use **PMID or normalized titles** to detect duplicates.

The script creates a **duplicate report** indicating:

- Duplicate groups
- Number of occurrences
- Records sharing the same DOI

### Output
duplicates_report_by_doi.xlsx



---

## 3. Apply exclusion criteria and score papers

**screen_papers.py**

This script performs **automatic title-level screening** using predefined **inclusion and exclusion criteria**.

The screening rules remove papers that are **not relevant to the research topic**.

### Exclusion Criteria

- Studies **not related to autism spectrum disorder**
- Studies where **ASD refers to another condition** (e.g., adult spinal deformity)
- **Animal or preclinical studies**
- Studies without **machine learning, deep learning, or computer vision methods**
- Studies **not analyzing motor behavior** (e.g., gait, movement patterns, stereotyped movements)
- Studies not focused on **autism detection, classification, screening, or behavioral characterization**
- **Editorials, commentaries, letters, or conference summaries** without original results
- Studies **without accessible full text**
- **Non-English publications**

The script assigns a **relevance score** based on the presence of keywords related to:

- **autism**
- **motor behavior**
- **AI / machine learning**

### Output

---

## 3. Apply exclusion criteria and score papers

**screen_papers.py**

This script performs **automatic title-level screening** using predefined **inclusion and exclusion criteria**.

The screening rules remove papers that are **not relevant to the research topic**.

### Exclusion Criteria

- Studies **not related to autism spectrum disorder**
- Studies where **ASD refers to another condition** (e.g., adult spinal deformity)
- **Animal or preclinical studies**
- Studies without **machine learning, deep learning, or computer vision methods**
- Studies **not analyzing motor behavior** (e.g., gait, movement patterns, stereotyped movements)
- Studies not focused on **autism detection, classification, screening, or behavioral characterization**
- **Editorials, commentaries, letters, or conference summaries** without original results
- Studies **without accessible full text**
- **Non-English publications**

The script assigns a **relevance score** based on the presence of keywords related to:

- **autism**
- **motor behavior**
- **AI / machine learning**

### Output
screened_autism_ai_scored.xlsx


This file contains:

- **screening decisions**
- **exclusion reasons**
- **relevance scores**

---

# Workflow

The repository follows the screening workflow below:

1. **Collect database search results**
2. **Parse raw exports**
3. **Merge records into a screening sheet**
4. **Identify duplicate papers**
5. **Apply exclusion criteria**
6. **Score and prioritize relevant papers**

---
---

# Literature Search Queries

The following queries were used to retrieve the initial set of papers from the scientific databases limited to 2016-2026.

## PubMed

**Query**

( ("autism spectrum disorder"[Title/Abstract] OR autism[Title/Abstract] OR ASD[Title/Abstract]) )
AND
( "gait"[Title/Abstract] OR "gait analysis"[Title/Abstract] OR "motor stereotyp*"[Title/Abstract] OR "repetitive motor"[Title/Abstract] OR "repetitive movement*"[Title/Abstract] OR "stereotyped behavior"[Title/Abstract] OR "motor pattern*"[Title/Abstract] OR "movement disorder*"[Title/Abstract] )
AND
( "machine learning"[Title/Abstract] OR "deep learning"[Title/Abstract] OR "computer vision"[Title/Abstract] OR "pose estimation"[Title/Abstract] OR "skeleton tracking"[Title/Abstract] OR "neural network"[Title/Abstract] )


**Results**

36 papers retrieved.

---

## Scopus

**Query**
TITLE-ABS-KEY(
("autism spectrum disorder" OR autism OR ASD)
AND
(gait OR "gait analysis" OR stereotypy OR stereotypies
OR "repetitive motor" OR "repetitive movement"
OR "stereotyped behavior" OR "motor pattern"
OR "movement disorder")
AND
("machine learning" OR "deep learning"
OR "computer vision" OR "pose estimation"
OR "skeleton tracking" OR "neural network")
)


**Results**

150 papers retrieved.

After applying database filters: Limited to Computer Science, Engineering, Medicine, Psychology, Health Professions

119 papers remained.

---

## IEEE Xplore

**Query**

("All Metadata":"autism" OR "All Metadata":"autism spectrum disorder")
AND
("All Metadata":"gait analysis" OR "All Metadata":"motor stereotypy" OR "All Metadata":"repetitive movement" OR "All Metadata":"stereotypical behavior")
AND
("All Metadata":"machine learning" OR "All Metadata":"deep learning" OR "All Metadata":"computer vision" OR "All Metadata":"neural network")

13 papers retrieved.

# Purpose

This repository supports a **reproducible literature review process** for research on:

**AI-based analysis of motor behavior and gait in Autism Spectrum Disorder (ASD).**

The scripts help streamline the **initial screening phase of systematic or scoping reviews**.

