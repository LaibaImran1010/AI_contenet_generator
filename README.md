# 🤖 AI Content Generator Studio

An elegant, high-performance automated copywriting assistant built using **Streamlit** and powered by the **Google GenAI SDK (Gemini 2.5 Flash)**. This enterprise-grade tool optimizes digital marketing workflows by generating tailored, structured content strategies instantly across multiple business frameworks.

## ✨ Advanced Features

- **Omnichannel Framework Modules:** Dedicated tabs configured for specialized marketing tasks:
  - 📝 **Blog Post Draftsman:** SEO-driven article ideation with automated keyword insertion.
  - 📱 **Social Media Caption Layouts:** Format-ready text layouts for Instagram, TikTok, Facebook, and Pinterest complete with optimized hashtags and emojis.
  - 💼 **LinkedIn Thought Leadership:** Structured formats incorporating scroll-stopping hooks and actionable professional takeaways.
  - 📧 **Strategic Email Funnels:** Professional templates for client follow-ups, applications, and cold outreach.
  - 🏷️ **Conversion-Focused Product Descriptions:** Copywriting models tailored to highlight key features, specifications, and consumer benefits.
  - 📣 **High-ROI Marketing Ad Variations:** A/B testing copy layouts equipped with explicit Call-to-Actions (CTAs).
- **Dynamic Variable Ingestion:** Adjust tone matrices (Professional, Casual, Enthusiastic, Persuasive, Informative), output lengths, and target demographics via a sidebar panel.
- **Bespoke UI/UX Styling Engine:** Complete system overrides via targeted CSS injection to deliver a cohesive, pill-capsule interface design with clear, accessible input text areas and custom-styled menu layouts.
- **Markdown Data Pipeline:** Live rendered output display with direct data pipeline conversion allowing content download as native `.md` files.

## 📐 System Architecture & Workflow

1. **User Interface Layer:** Streamlit captures user intent inputs, configurations, and template choices.
2. **Context Orchestration Layer:** Python processes structural variables and injects strict guardrail system instructions.
3. **Inference Processing Engine:** The Google GenAI Client sends an API call payload to the `gemini-2.5-flash` model.
4. **Formatting & Serialization Layer:** Clean Markdown response formatting is applied to the raw model output for UI rendering and file compilation.

---

## 🛠️ Installation & Environment Setup

### 1. Repository Setup
```bash
git clone [https://github.com/YOUR_USERNAME/ai-content-generator-studio.git](https://github.com/YOUR_USERNAME/ai-content-generator-studio.git)
cd ai-content-generator-studio
