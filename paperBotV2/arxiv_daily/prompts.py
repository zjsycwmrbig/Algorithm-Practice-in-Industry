#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存储所有用于分析和排序论文的prompt模板
"""

# 粗排prompt模板
PRERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in Large Language Models (LLMs) and Large-Scale Recommendation Systems, with deep knowledge of the search, recommendation, and advertising domains.

# My Current Focus

- **Recommendation Systems:** recommendation, ranking, retrieval, user modeling, matching, multi-stage recommendation, CTR/CVR, sequential recommendation, multi-task learning for recommendation.
- **Computer Networks and Systems:** satellite networks, RDMA, datacenter networks, congestion control, transport protocols, routing, traffic engineering, network measurement, distributed communication systems, cluster communication optimization.
- **Practical Systems for Networking:** system-level innovations with clear implications for network performance, reliability, latency, throughput, or resource efficiency.

# Irrelevant Topics
- Physical-layer innovations, including radio signal design, modulation, coding, antenna design, beamforming at the PHY layer, channel estimation, waveform design, RF circuit design, optical device innovation
- Pure communication theory without clear systems or networking implications
- Purely hardware/device/material innovations
- Medical, Biology, Chemistry, Physics or other domain-specific applications
- Purely theoretical papers without clear practical implications
- Purely Vision, 3D Vision, Graphic or Speech papers
- Purely NLP-centric topics, AIGC, summarization, hallucination, or general LLM application papers unrelated to recommendation or networking
- Security, privacy, fairness, ethics, federated learning unless directly tied to recommendation or networking performance

# Goal
Screen new papers based on my focus. **DO NOT include irrelevant topics**.

# Task
Based ONLY on the paper's title, provide a quick evaluation.
1. **Academic Translation**: Translate the title into professional Chinese, prioritizing accurate technical terms and faithful meaning.
2. **Relevance Score (1-10)**: How relevant is it to **My Current Focus**?
3. **Reasoning**: A 2-3 sentence explanation for your score. **For "Enabling Tech" papers, you MUST explain their potential application in RecSys/Search/Ads.**

# Input Paper
- **Title**: {title}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "translation": "...",
  "relevance_score": <integer>,
  "reasoning": "..."
}}
"""

# 精排prompt模板
FINERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in Large Language Models (LLMs) and Large-Scale Recommendation Systems, with deep knowledge of the search, recommendation, and advertising domains.

# My Current Focus

- **Core Domain Advances:** Core advances within RecSys, Search, or Ads itself, even if they do not involve LLMs.
- **Enabling LLM Tech:** Trends and Foundational progress in the core LLM which must have potential applications in RecSys, Search or Ads.
- **Enabling Transformer Tech: Advances in Transformer architecture (e.g., efficiency, new attention mechanisms, MoE, etc.).
- **Direct LLM Applications:* Novel ideas and direct applications of LLM technology for RecSys, Search or Ads.
- **VLM Analogy for Heterogeneous Data:** Ideas inspired by **Vision-Language Models** that treat heterogeneous data (like context features and user sequences) as distinct modalities for unified modeling. 

# Goal
Perform a detailed analysis of the provided paper based on its title and abstract. Identify its core contributions and relevance to my focus areas.

# Task
Based on the paper's **Title** and **Abstract**, provide a comprehensive analysis.
1.  **Relevance Score (1-10)**: Re-evaluate the relevance score (1-10) based on the detailed information in the abstract.
2.  **Reasoning**: A 1-2 sentence explanation for your score in Chinese, direct and compact, no filter phrases.
3.  **Summary**: Generate a 1-2 sentence, ultra-high-density Chinese summary focusing solely on the paper's core idea, to judge if its "idea" is interesting. The summary must precisely distill and answer these two questions:
    1.  **Topic:** What core problem is the paper studying or solving?
    2.  **Core Idea:** What is its core method, key idea, or main analytical conclusion?
    **STRICTLY IGNORE EXPERIMENTAL RESULTS:** Do not include any information about performance, SOTA, dataset metrics, or numerical improvements.
    **FOCUS ON THE "IDEA":** Your sole purpose is to clearly convey the paper's "core idea," not its "experimental achievements."

# Input Paper
- **Title**: {title}
- **Abstract**: {summary}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "rerank_relevance_score": <integer>,
  "rerank_reasoning": "...",
  "summary": "..."
}}
"""
