# AI Product Management for Technology Leaders

## Course Proposal for MSTM Program — Gies College of Business, UIUC

**Date:** 2026-03-22
**Course Code:** BADM 5XX (proposed)
**Credits:** 2 credit hours
**Format:** 8 weeks, half-semester module
**Placement:** Technology Management elective or concentration course
**Prerequisites:** None (designed for STEM graduates and mid-career professionals)

---

## Executive Summary

The MSTM program at Gies prepares STEM graduates and mid-career professionals to lead at the intersection of technology and business. Yet its curriculum has **no dedicated AI course** — a significant gap given that 85% of enterprise software now incorporates AI/ML features (Gartner, 2025) and AI product managers command 20-35% salary premiums over traditional PMs.

This 8-week course fills that gap. It equips students to lead AI-powered product initiatives — not by teaching them to build models, but by teaching them to **think probabilistically, evaluate AI systems critically, and ship AI products responsibly**. The course draws on Vin Vashishta's practitioner frameworks, industry toolkits from Google and Microsoft, and the emerging regulatory landscape (EU AI Act, NIST AI RMF).

### Why This Course, Why Now

1. **Market demand:** 76% of product leaders plan to increase AI integration investment; only 12% of PMs feel confident in AI/ML knowledge
2. **Program fit:** Slots naturally into the MSTM's 12 elective credits, complements existing courses (BADM 557 Business Intelligence, BADM 579 Analytics, BADM 514 Managing Innovation)
3. **Differentiation:** No comparable AI PM course exists in the current Gies portfolio — this would be a first-mover advantage among peer STEM-management programs
4. **Student demand:** MSTM graduates target roles at EY, Accenture, Deloitte, Amazon, Google, Salesforce — all companies where AI PM skills are now table stakes

---

## Course Learning Objectives

By the end of this course, students will be able to:

1. **Distinguish** AI product management from traditional PM — articulating the shift from deterministic to probabilistic product thinking
2. **Evaluate** AI/ML system capabilities and limitations using appropriate metrics (precision, recall, F1, model drift) alongside business KPIs
3. **Apply** structured frameworks (Google PAIR, Microsoft HAX) to design human-centered AI product experiences
4. **Navigate** the AI regulatory landscape (EU AI Act, NIST AI RMF) and integrate responsible AI principles into product decisions
5. **Develop** an AI product strategy — from opportunity identification through data requirements, model selection, evaluation, and go-to-market
6. **Communicate** AI product tradeoffs to cross-functional stakeholders (data scientists, engineers, executives, legal/compliance)
7. **Prototype** AI-powered product concepts using prompt engineering and no-code/low-code tools
8. **Assess** build vs. buy decisions for AI capabilities, including vendor evaluation and API integration strategies

---

## Course Architecture

### Design Principles

- **Practitioner-first:** Every session connects theory to real product decisions. No course exists in isolation — frameworks are tools for action.
- **Probabilistic thinking as foundation:** Following Vashishta's core insight, the course trains students to manage uncertainty rather than eliminate it. AI products don't have "correct" outputs — they have distributions of acceptable outcomes.
- **Cross-functional fluency:** Students practice translating between technical (data science/ML engineering) and business (strategy/finance/legal) languages — the core MSTM value proposition.
- **Hands-on evaluation:** Students interact with AI systems, evaluate outputs, and develop intuition for what "good" looks like before they try to build.

### Assessment Structure

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly case analyses | 30% | Individual written analyses of AI product decisions |
| AI Product Audit | 20% | Team project: evaluate an existing AI product using course frameworks |
| AI Product Proposal | 30% | Team capstone: full product strategy for an AI-powered product |
| Class participation | 10% | Discussion contributions, peer feedback |
| Prompt engineering lab | 10% | Hands-on exercises with LLM-based product prototyping |

---

## 8-Week Course Outline

### Week 1: The AI Product Management Paradigm Shift

**Theme:** Why AI products are fundamentally different — and what that means for how you manage them.

**Learning Objectives:**
- Articulate the shift from deterministic to probabilistic product development
- Identify where traditional PM practices break down with AI
- Map the AI product management competency landscape

**Topics:**
- The PM role evolution: from feature factories to AI-native products
- Deterministic vs. probabilistic outputs — the foundational mental model shift
- Why "requirements" work differently when outputs are probabilistic
- Data as the new product foundation (vs. feature-based roadmaps)
- The AI PM competency framework: technical literacy, strategic thinking, ethical reasoning

**Case Study:** A traditional SaaS company's first AI feature launch — what went wrong when the team applied waterfall PM practices to a probabilistic system.

**Readings:**
- Vashishta, V. "Why AI Product Managers Need a Different Playbook" (LinkedIn, 2025)
- Bratsis, I. *The AI Product Manager's Handbook*, Ch. 1-2
- AI PM Evaluation Framework overview (aipmframework.com)

**Deliverable:** Reflection paper — "Where does traditional PM thinking fail with AI?"

---

### Week 2: Understanding AI/ML Systems (for Non-Engineers)

**Theme:** Enough technical depth to ask the right questions — not enough to build models yourself.

**Learning Objectives:**
- Explain core ML paradigms (supervised, unsupervised, reinforcement learning) at a conceptual level
- Understand the transformer architecture and why LLMs changed everything
- Evaluate data requirements and quality considerations for AI products

**Topics:**
- ML paradigms: supervised, unsupervised, reinforcement learning — when each applies
- Neural networks and deep learning — the intuition, not the math
- The transformer revolution: attention mechanisms, pre-training, fine-tuning
- LLMs, foundation models, and the shift to general-purpose AI
- Data pipelines: collection, labeling, storage, quality — the PM's data checklist
- RAG (Retrieval-Augmented Generation) and agentic architectures — emerging patterns

**Guest Speaker Opportunity:** UIUC CS/Data Science faculty on transformer architectures

**Readings:**
- Ananthaswamy, A. *Why Machines Learn*, selected chapters
- "What Every PM Should Know About LLMs" — industry primer
- Google PAIR Guidebook, Chapter: "Data Collection and Evaluation"

**Deliverable:** Technical concept map — visual diagram explaining how a specific AI product works (e.g., ChatGPT, GitHub Copilot, Spotify Discover Weekly)

---

### Week 3: AI Product Metrics and Evaluation

**Theme:** You can't manage what you can't measure — and AI measurement is fundamentally different.

**Learning Objectives:**
- Select appropriate evaluation metrics for different AI product types
- Design evaluation strategies that combine automated and human assessment
- Understand model drift and post-launch monitoring requirements

**Topics:**
- Beyond accuracy: precision, recall, F1 score, AUC-ROC — when each matters
- Business metrics vs. model metrics: building the bridge
- Evaluation strategies for LLM products: "LLM as a Judge," human evaluation, A/B testing
- The evaluation stack: offline evaluation → shadow mode → canary release → full deployment
- Model drift: why AI products degrade over time and how to detect it
- Cost metrics: token usage, inference latency, compute costs — the AI product P&L

**Case Study:** How a recommendation system's accuracy improved while user satisfaction declined — the metric alignment problem.

**Lab Exercise:** Evaluate outputs from three different LLMs on the same task. Score for accuracy, relevance, safety, and cost. Present findings to class.

**Readings:**
- Langfuse blog: "LLM Product Management" (2024)
- Vashishta, V. "Measuring What Matters in AI Products" (2025)
- Shi, Cai, Rong. *Reimagined: Building Products with Generative AI*, Ch. on evaluation

**Deliverable:** Evaluation framework design — propose a metric dashboard for a specific AI product

---

### Week 4: Human-Centered AI Design

**Theme:** The best AI is invisible — it enhances human capability without demanding attention.

**Learning Objectives:**
- Apply Google PAIR and Microsoft HAX frameworks to AI product design decisions
- Design for appropriate user trust calibration
- Handle AI errors and uncertainty in UX gracefully

**Topics:**
- Google PAIR Guidebook: designing AI products that serve people
  - Calibrating user trust and expectations
  - Explaining AI decisions to users
  - Designing for errors and edge cases
- Microsoft HAX Toolkit: 18 guidelines for human-AI interaction
  - Before interaction: setting expectations
  - During interaction: providing appropriate feedback
  - When wrong: graceful error recovery
  - Over time: adapting to user patterns
- Apple's ML Human Interface Guidelines: designing invisible intelligence
- Mental models for AI uncertainty: how users interpret probabilistic outputs
- The "automation surprise" problem and how to prevent it

**Workshop:** HAX Workbook exercise — cross-functional team (PM, designer, engineer roles) works through the Microsoft HAX planning process for a proposed AI feature.

**Readings:**
- Google PAIR Guidebook (pair.withgoogle.com/guidebook)
- Microsoft HAX Guidelines for Human-AI Interaction
- Apple Human Interface Guidelines, Machine Learning section
- Lipenkova, J. *The Art of AI Product Development*, Ch. on UX design

**Deliverable:** UX audit — apply PAIR + HAX frameworks to evaluate an existing AI product's user experience. Identify 3 specific improvements.

---

### Week 5: Responsible AI and Governance

**Theme:** Ethics isn't a checkbox — it's a product management discipline.

**Learning Objectives:**
- Navigate the EU AI Act risk classification and compliance requirements
- Apply the NIST AI Risk Management Framework to product decisions
- Identify and mitigate bias, fairness, and safety risks in AI products

**Topics:**
- The responsible AI landscape: FATE (Fairness, Accountability, Transparency, Explainability)
- EU AI Act deep dive:
  - Risk classification: unacceptable, high-risk, general-purpose AI
  - GPAI requirements (effective August 2025)
  - High-risk obligations (effective August 2026)
  - Penalties: up to €35M or 7% global turnover
- NIST AI Risk Management Framework: Govern, Map, Measure, Manage
- ISO/IEC 42001: AI management systems standard
- Bias detection and mitigation: practical approaches for PMs
- AI safety: alignment, hallucination management, adversarial robustness
- Building AI governance into the product development lifecycle (not bolting it on after)

**Case Study:** A healthcare AI product navigating EU AI Act high-risk classification — the product decisions that changed (and the ones that didn't).

**Readings:**
- NIST AI Risk Management Framework (nist.gov)
- EU AI Act summary and PM implications
- Nika, M. & Granados, D. *The AI Product Playbook*, Ch. on ethics and governance
- Vashishta, V. "Responsible AI Is a Product Problem, Not a Research Problem" (2025)

**Deliverable:** Regulatory impact assessment — for your team's target AI product, classify its risk level under EU AI Act and identify the top 5 compliance requirements that affect product decisions.

---

### Week 6: AI Product Strategy and Roadmapping

**Theme:** From opportunity to roadmap — how to build an AI product strategy that accounts for uncertainty.

**Learning Objectives:**
- Identify high-value AI product opportunities using structured frameworks
- Make build vs. buy vs. API decisions for AI capabilities
- Create AI-specific product roadmaps that account for data and model dependencies

**Topics:**
- Opportunity identification: where does AI create genuine value vs. hype?
- The AI product strategy canvas: problem → data → model → UX → business model
- Build vs. buy vs. API: decision framework for AI capabilities
  - When to use foundation model APIs (OpenAI, Anthropic, Google)
  - When to fine-tune
  - When to build custom models
  - Vendor evaluation criteria
- AI-specific roadmapping challenges:
  - Data dependency: you can't ship the feature until the data pipeline works
  - Model uncertainty: you don't know if the model will work until you try
  - Continuous improvement: AI products are never "done"
- Vashishta's practitioner framework: moving from experimentation to production
- Stakeholder communication: translating AI uncertainty into executive-friendly language

**Workshop:** AI Product Strategy Canvas — teams develop a complete strategy canvas for their capstone product proposal.

**Readings:**
- Vashishta, V. "The AI Product Strategy Framework" (2025)
- Perri, M. *Escaping the Build Trap*, Ch. on strategy (adapted for AI context)
- Cagan, M. *Transformed*, sections on AI-era product organizations
- Moore, G. *Crossing the Chasm* — technology adoption lifecycle applied to AI products

**Deliverable:** Draft AI Product Strategy Canvas for capstone project (team submission)

---

### Week 7: Prompt Engineering and LLM Product Development

**Theme:** Prompt engineering is the new product specification — learn to think in prompts.

**Learning Objectives:**
- Apply systematic prompt engineering techniques to product use cases
- Design prompt pipelines for production AI products
- Evaluate and iterate on prompt-based product features

**Topics:**
- Prompt engineering as a PM discipline (not just a developer tool)
- Core techniques: zero-shot, few-shot, chain-of-thought, ReAct, tree-of-thought
- System prompts as product specifications: defining AI product behavior
- Prompt pipelines: chaining, routing, and orchestrating multi-step AI workflows
- Multi-agent architectures: when one LLM isn't enough
- LLMOps for PMs: monitoring, evaluation, and iteration in production
  - Tools landscape: LangChain, Langfuse, PromptLayer
  - Cost management: token optimization, caching strategies
- The "LLM Product Manager" role: emerging responsibilities and skills

**Lab Exercise:** Prompt engineering workshop
- Design a system prompt for a customer service AI assistant
- Iterate through 3 versions based on evaluation criteria
- Compare outputs across models (GPT-4, Claude, Gemini)
- Document the prompt development process as a product spec

**Readings:**
- PromptLayer blog: "Product Manager Levels — LLM Competency" (2024)
- Langfuse blog: "LLM Product Management" (2024)
- 58 prompting techniques taxonomy (research overview)

**Deliverable:** Prompt engineering portfolio — documented prompt development for 2 product use cases, including iteration history and evaluation results

---

### Week 8: Capstone Presentations and the Future of AI PM

**Theme:** Ship it — present your AI product strategy and look ahead.

**Learning Objectives:**
- Present a complete AI product strategy to a cross-functional audience
- Synthesize course frameworks into a coherent product management approach
- Identify personal development priorities for an AI PM career

**Topics (first half):**
- The future of AI product management:
  - Agentic AI: products that act autonomously
  - Multimodal AI: products that see, hear, read, and speak
  - On-device AI: privacy-first product architectures
  - AI-native organizations: how product teams are restructuring
- Career pathways: AI PM roles, compensation trends, skill development
- The AI PM's continuous learning toolkit

**Capstone Presentations (second half):**
- Each team presents their AI Product Proposal (15 min + 5 min Q&A)
- Evaluation by instructor + industry judges (if available)
- Peer feedback using course evaluation frameworks

**Deliverable:** Final AI Product Proposal (team) — complete document including:
- Problem statement and opportunity assessment
- AI Product Strategy Canvas
- Data requirements and feasibility analysis
- Evaluation framework and success metrics
- UX design informed by PAIR/HAX frameworks
- Regulatory assessment (EU AI Act / NIST AI RMF)
- Go-to-market strategy and roadmap
- Risk analysis and mitigation plan

---

## Recommended Textbooks and Resources

### Primary Texts
| Book | Author(s) | Year | Role in Course |
|------|-----------|------|----------------|
| *The AI Product Playbook* | Dr. Marily Nika & Diego Granados | 2025 | Primary reference — frameworks, ethics, career |
| *Reimagined: Building Products with Generative AI* | Shi, Cai, Rong | 2024 | GenAI product strategy, 30+ case studies |

### Supplementary Texts
| Book | Author(s) | Year | Role in Course |
|------|-----------|------|----------------|
| *The AI Product Manager's Handbook* | Irene Bratsis | 2023 | AI concepts and integration fundamentals |
| *The Art of AI Product Development* | Dr. Janna Lipenkova | 2024 | First-time AI product builder framework |
| *Why Machines Learn* | Anil Ananthaswamy | 2024 | ML intuition for non-specialists (Week 2) |

### Industry Frameworks (Free)
- [Google PAIR Guidebook](https://pair.withgoogle.com/guidebook/) — human-centered AI design
- [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/) — human-AI interaction guidelines
- [Apple ML Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/machine-learning)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [AI PM Evaluation Framework](https://aipmframework.com/) — open-source competency assessment

### Practitioner Content
- Vin Vashishta's AI PM articles (LinkedIn/blog) — practitioner frameworks on probabilistic thinking, AI strategy, responsible AI
- Langfuse blog on LLM Product Management
- PromptLayer blog on PM LLM Competency
- Product School AI Learning Roadmap

---

## Fit Within MSTM Curriculum

### Complementary Existing Courses
| Existing Course | Relationship to AI PM Course |
|----------------|------------------------------|
| BADM 557 — Topics in Business Intelligence | Provides data/analytics foundation; AI PM builds on this with product strategy layer |
| BADM 579 — Analytics for Management Decision Making | Teaches analytical frameworks; AI PM extends to AI-specific metrics and evaluation |
| BADM 514 — Managing Innovation | Covers innovation management theory; AI PM applies it to AI product development |
| BADM 543 — Technology Strategy | Strategic context; AI PM provides tactical AI product execution skills |
| BADM 589 — Project Management | Project execution skills; AI PM addresses unique AI project challenges (data dependency, model uncertainty) |

### Concentration Alignment
- **Business Data Analytics:** Direct complement — adds product strategy to data skills
- **Consumer Centric Innovation and Design:** PAIR/HAX frameworks bridge AI capabilities with human-centered design
- **Information Technology & Control:** AI governance and responsible AI extend IT control frameworks
- **Supply Chain Management:** AI-powered supply chain products are a natural capstone project domain

### Suggested Placement
- **Semester:** Spring (after students have taken BADM 557 and BADM 579 in Fall)
- **Schedule:** 2-credit, half-semester intensive module (8 weeks)
- **Cohort:** Open to both Graduate and Professional/Advancement cohorts

---

## Appendix: Instructor Notes

### Guest Speaker Pipeline
- UIUC CS/Data Science faculty (Week 2: technical foundations)
- Gies alumni in AI PM roles at Amazon, Google, Salesforce (Week 6: strategy)
- AI ethics/policy researchers (Week 5: responsible AI)
- Local/regional AI startup founders (Week 8: capstone judges)

### Assessment Rubrics
Each deliverable should be evaluated on:
1. **Framework application** — correct and thoughtful use of course frameworks
2. **Business reasoning** — commercial viability and strategic clarity
3. **Technical grounding** — appropriate level of technical understanding (not too shallow, not overreaching)
4. **Stakeholder communication** — ability to explain AI decisions to non-technical audiences
5. **Ethical consideration** — integration of responsible AI principles (not as an afterthought)

### Course Evolution
This course should be updated annually. Key areas to refresh:
- Model capabilities and benchmarks (changes quarterly)
- Regulatory landscape (EU AI Act milestones, state-level AI legislation)
- Industry case studies (replace with most recent examples)
- Tool landscape (LLMOps, prompt engineering platforms)
- Compensation and career data

---

*Prepared by Vishal Sachdev, leveraging research from Vin Vashishta's AI PM practitioner frameworks, Gies MSTM program analysis, and comprehensive AI PM landscape review.*
