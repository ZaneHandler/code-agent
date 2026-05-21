# Autonomous Coding Agent

An AI-powered Multi-Agent software engineering workflow system capable of autonomous planning, coding, testing, reviewing, and iterative fixing.

---

# Overview

Autonomous Coding Agent is a lightweight autonomous software engineering framework designed to simulate how modern AI Agents collaborate to complete real-world software development tasks.

The project focuses on:

- Multi-Agent Collaboration
- Long-Context Reasoning
- Autonomous Workflow Execution
- Tool Calling
- Memory-based RAG
- Self-healing Coding Loop

Unlike traditional AI coding assistants that only generate snippets, this project demonstrates a complete AI-driven engineering workflow.

---

# Core Problem

Traditional AI coding assistants suffer from several limitations:

- Unable to autonomously complete complex engineering tasks
- Weak long-context understanding
- No persistent task planning
- No autonomous debugging/testing loop
- Heavy human intervention required

This project addresses these issues by introducing a Multi-Agent orchestration system.

---

# Architecture

```text
User Task
   ↓
Planner Agent
   ↓
Coding Agent
   ↓
Testing Agent
   ↓
Reviewer Agent
   ↓
Auto Fix Loop
   ↓
GitHub PR
