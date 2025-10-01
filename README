# LangChain Tools & Agents: Overcoming Knowledge Cutoff

This repository demonstrates how to handle the **knowledge cutoff limitation of LLMs** using simple LangChain agents and tools. It shows how to integrate a **time tool** and a **web search tool** to fetch up-to-date information.

---

## Overview

Large language models like GPT-4.1-mini have a **knowledge cutoff**, meaning they only know information up to a certain date. To handle queries about recent events or real-time data, we can combine the LLM with external tools:

- **Time Tool**: Returns current date for time-sensitive queries.
- **Web Search Tool**: Fetches current information from the web (DuckDuckGo Search Engine SDK as a tool in this demo).

This repo demonstrates the difference between:

1. **Direct LLM invocation** (cannot access real-time info beyond the knowledge cutoff).  
2. **Agent with tools** (can use tools to retrieve fresh information and provide accurate answers).

---

## Scripts

### 1. `knowledge_cut_off_demo.py` – Direct LLM Call

- Uses `ChatOpenAI` directly.
- Shows how the LLM responds with **only pre-trained knowledge**.
- Limitations:
  - Cannot provide recent updates.
  - May give outdated or incomplete answers.

### 2. `time_and_websearch_tools.py` – Agent with Tools

- Defines two tools using the `@tool` decorator:
  1. **Time Tool** – Returns today’s date.
  2. **Web Search Tool** – Uses DuckDuckGo to fetch recent information.
- Initializes a **Zero-Shot ReAct agent** (`AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION`) to:
  - Decide which tool to use for a given query.
  - Combine the LLM’s reasoning with external tool outputs.
- Benefits:
  - Overcomes knowledge cutoff by fetching up-to-date data.
  - Handles time-sensitive queries accurately.
  - Demonstrates agent reasoning and tool orchestration.

---

## To install and run:

```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python knowledge_cut_off_demo.py
    python time_and_websearch_tools.py
