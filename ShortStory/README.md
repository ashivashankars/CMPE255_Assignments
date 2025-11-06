# 📰 When the News Is Too New: AI for Cold-Start News Recommendations

## Abstract
A new research paper titled “Solving Cold Start in News Recommendations: A RippleNet-Based System for Large-Scale Media Outlet” takes on one of the biggest challenges in digital journalism — how to recommend brand-new news stories that have no clicks or views yet. Traditional algorithms rely on past user activity, so when a new article is published, they simply don’t know who might like it.

The researchers combine two cutting-edge AI ideas to solve this: language-model text embeddings, which help the system understand what an article is about, and RippleNet, a knowledge-graph method that connects related topics, authors, and readers. Together, they enable the recommendation engine to make smart predictions even for articles that are just minutes old.

The study was tested on real data from one of Poland’s largest media outlets. While the approach didn’t fully beat existing production models yet, it showed clear progress in handling “cold-start” situations and provided valuable insights for building smarter, faster, and fairer news recommendations. It’s a promising step toward a future where readers see relevant stories the moment they’re published.

---

This repository explores how **RippleNet-based knowledge-graph models** and **text embeddings** can solve the *cold-start problem* in large-scale news recommendation systems.  
It builds on insights from the research paper  
**“Solving Cold Start in News Recommendations: A RippleNet-Based System for Large-Scale Media Outlet” (Radziszewski et al., 2025)**  
and the accompanying Medium article:  
👉 [**When the News Is Too New: How AI Is Learning to Recommend Fresh Stories**](https://medium.com/@archana.shivashankar/when-the-news-is-too-new-how-ai-is-learning-to-recommend-fresh-stories-5d2141e8f97a)

---

## 🧭 Overview

News recommendation systems face a unique challenge — **new articles appear constantly**, while traditional models depend on historical user clicks.  
This results in the **cold-start problem**, where fresh content struggles to reach readers because it lacks interaction data.

The paper proposes a **hybrid AI architecture** that merges:

- **RippleNet** — a knowledge-graph recommender modeling relationships between users, topics, and entities.  
- **Large-Language-Model (LLM) Embeddings** — semantic text representations that help the system understand the meaning of new articles.

Together, these components enable **content-aware recommendations** for brand-new news stories, even before they receive any user engagement.

---

## 🏗️ Architecture

User History → Knowledge Graph (authors, topics, entities) → RippleNet propagation → Item scoring

New Articles → LLM Text Embeddings → Similarity Mapping → RippleNet space

---

### 🔹 Key Components
1. **Knowledge Graph Construction** – Builds entity–relation graphs from user–article metadata.  
2. **RippleNet Propagation** – Spreads user preferences through connected entities in the graph.  
3. **Cold-Start Handling** – Uses neural encoders or similarity-based proxies to embed unseen items.  
4. **Daily Retraining Pipeline** – Orchestrated with Airflow + Amazon SageMaker for production-scale learning.

---

## ⚙️ Experiments & Ablation Studies

The researchers tested two main strategies for handling unseen (cold-start) articles:

| Strategy | Description | Outcome |
|-----------|--------------|----------|
| **Neural Encoder** | Learns to map text embeddings into RippleNet’s space | Unstable in production; limited improvement |
| **Similarity-Based Replacement** | Finds the most similar known article via cosine similarity and reuses its embedding | ✅ More robust, simpler, and scalable |

This **ablation study** highlights that lightweight, interpretable approaches can outperform heavier neural solutions when deployed at scale.

---

## 📊 Metrics & Evaluation

**Offline Metrics** – measured recommendation accuracy over training and testing days.  
**Online A/B Tests** – deployed on a major Polish media outlet serving millions of readers.

| Platform | Engagement Change | Observation |
|-----------|------------------|--------------|
| Mobile | −13.77 % | Drop vs. baseline, but improved coverage for unseen items |
| Desktop | −16.21 % | Similar drop; greater diversity and fairness for new content |

While engagement metrics dipped, the system significantly increased **cold-start coverage**, giving new articles better visibility — a vital goal for modern news recommendation systems.

---

## 🧩 Key Deliverables

### 1. Medium Article  
A layperson-friendly summary and commentary on the research findings.  
📖 [**Read on Medium →**](https://medium.com/@archana.shivashankar/when-the-news-is-too-new-how-ai-is-learning-to-recommend-fresh-stories-5d2141e8f97a)

---

### 2. Slide Deck  
Presentation summarizing:
- RippleNet + LLM embedding architecture  
- Workflow and retraining pipeline  
- performance metrics  
- Future improvements and ethical reflections  

📖 [Google Slides →](https://docs.google.com/presentation/d/1eVvZXeWMD4n0Rs1oRjkR5B8w4gcXqcMV/edit?usp=sharing&ouid=103834923414205069213&rtpof=true&sd=true)

---

### 3. Video Presentation  
A 10–15 minute walkthrough covering:
- The cold-start problem and motivation  
- Architecture breakdown with visual flow  
- Real-world A/B test learnings and future ideas  

(*To be uploaded: `/video/ColdStart_Walkthrough.mp4`*)

---

## 🔍 Data Mining Perspective

This work exemplifies **data mining at scale** — discovering useful, non-obvious patterns from massive interaction data.  
RippleNet acts as a **relational pattern miner**, capturing user–item–topic relationships, while **text embeddings** serve as a **dimensionality-reduced semantic space** enabling clustering and similarity search across unseen articles.  
These methods reflect key data-mining principles such as **representation learning**, **pattern propagation**, and **knowledge-graph reasoning**.

---

## 🧠 Applications Highlighted

- 📰 **Personalized News Feeds** – Relevant articles appear instantly upon publication.  
- 🔎 **Content Discovery** – Surfaces semantically similar stories before click data accumulates.  
- ⚖️ **Fair Visibility** – Helps smaller publishers and new authors gain equal exposure.  
- ⏱️ **Temporal Analytics** – Captures short-lived interest spikes in trending news topics.  

---

## 🚀 Future Directions

- Multi-modal embeddings combining text, image, and video context.  
- Joint training to align LLM and RippleNet embedding spaces.  
- Temporal modeling to capture evolving reader interests.  
- Explainable AI for transparent, trust-building recommendations.  

---

## 📚 Research Paper Reference

> Radziszewski et al. (2025).  
> *Solving Cold Start in News Recommendations: A RippleNet-Based System for Large-Scale Media Outlet.*  
> [arXiv:2511.02052](https://arxiv.org/pdf/2511.02052)

---

## Acknowledgments

This project is based on open-access research from **arXiv (2025)** and summarized for educational use in **CMPE 255 – Data Mining**.  
All figures and ideas are credited to the original authors and used here for academic commentary and non-commercial learning.

---
