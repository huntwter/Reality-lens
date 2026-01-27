# RealityLens — Cognitive Firewall

[![Live Demo](https://img.shields.io/badge/Live_Demo-realitylens.domain.com-C5A059?style=for-the-badge&logo=google-chrome&logoColor=white)](https://realitylens.domain.com)
[![License](https://img.shields.io/badge/License-MIT-333?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Powered By](https://img.shields.io/badge/AI-Gemini_3_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)

**RealityLens** is a next-generation **Cognitive Firewall**. It is a real-time AI logic engine designed to analyze text, detect rhetorical manipulation, and expose logical fallacies using a multi-agent reasoning system.

---

## 🚀 Live Deployment

Access the live application here: **[realitylens.domain.com](https://realitylens.domain.com)**

---

## 🧠 Core Architecture

RealityLens operates on a **Semantic Triage Architecture**, splitting every query into three distinct cognitive dimensions handled by specialized agents:

1.  **The Logician (Logos)**: Analyzes internal consistency, valid syllogisms, and logical fallacies.
2.  **The Historian (Ethos)**: Traces the etymological roots, historical context, and factual verification of the claim using Google Search Grounding.
3.  **The Profiler (Pathos)**: Decodes the emotional intent, rhetorical intensity, and persuasive techniques used in the text.

### Robust Graceful Fallback
To ensure 100% reliability during high-stakes demonstrations, RealityLens features a **Hybrid-Offline Mode**:
*   **Live Mode**: Default. Uses **Gemini 3 Flash** via the `google-genai` SDK for real-time, ground-truth analysis.
*   **Cached Fallback**: If the API experiences latency or quota limits, the system transparently serves pre-computed, high-fidelity analyses from a local cache of 100+ common misconceptions, ensuring the UX remains fluid and uninterrupted.

---

## 🛠️ Technical Stack

*   **Backend**: Python FastAPI (Async/Await)
*   **AI Engine**: Google GenAI SDK (`gemini-3-flash-preview`)
*   **Frontend**: Vanilla ES6 JavaScript + TailwindCSS
*   **Design System**: Custom "Quiet Luxury" Semantic Glassmorphism
*   **Transport**: Server-Sent Events (SSE) for millisecond-latency streaming

---

## 📦 Installation & Setup

### Prerequisites
*   Python 3.10+
*   Google Gemini API Key

### 1. Clone Repository
```bash
git clone https://github.com/huntwter/Reality-lens.git
cd Reality-lens
```

### 2. Environment Setup
Create a `.env` file in the root directory:
```ini
GEMINI_API_KEY=your_api_key_here
PROJECT_NAME="RealityLens"
VERSION="1.0.0"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
# Development Server
python main.py

# Production Server
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <small>Designed & Engineered with Precision.</small>
</p>
