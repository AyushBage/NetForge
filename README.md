# 🛡️ NetForge

> **Intelligent Firewall Rule Analysis & Conflict Detection System**

NetForge is a cybersecurity tool designed to analyze firewall rules and detect **conflicting, shadowed, overlapping, and redundant rules** using **Set Theory, Boolean Logic, and rule-based analysis**.

## 🚀 Features

* 🔍 Detect conflicting firewall rules
* 👻 Identify shadowed rules
* ♻️ Detect redundant rules
* 🔗 Find overlapping rules
* 🧠 Analyze rules using Set Theory and Boolean Logic
* 📊 Generate a detailed rule analysis report
* ⚡ Provide recommendations for improving rule ordering

## 🧠 Core Concepts

NetForge applies concepts from **Discrete Structures and Computational Theory (DSCT)**:

* Set Theory
* Set Intersection & Union
* Subsets
* Boolean Algebra
* Propositional Logic
* Relations
* Graph Theory
* Algorithmic Rule Analysis

## ⚙️ How It Works

```text
Firewall Rules
      ↓
Rule Parser
      ↓
Rule Normalization
      ↓
Set & Logic Analysis
      ↓
Conflict Detection
      ↓
Shadow / Redundancy Detection
      ↓
Security Report
```

## 🔥 Example

### Rule 1

```text
Source:   192.168.1.0/24
Port:     80
Protocol: TCP
Action:   ALLOW
```

### Rule 2

```text
Source:   192.168.1.50
Port:     80
Protocol: TCP
Action:   DENY
```

Since:

```text
192.168.1.50 ∈ 192.168.1.0/24
```

the two rules overlap and may create a **firewall rule conflict**.

### NetForge Output

```text
⚠ CONFLICT DETECTED

Rule 1 → ALLOW
Rule 2 → DENY

Relationship → OVERLAP
Risk → HIGH
```

## 🏗️ Project Architecture

```text
                ┌─────────────────┐
                │  Firewall Rules │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │  Rule Parser   │
                └────────┬────────┘
                         ↓
              ┌─────────────────────┐
              │ Set & Logic Engine  │
              └──────────┬──────────┘
                         ↓
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Conflicts       Shadowed       Redundant
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                 Security Report
```

## 🛠️ Tech Stack

* **Language:** [Add your language]
* **Backend:** [Add if applicable]
* **Frontend:** [Add if applicable]
* **Database:** [Add if applicable]
* **Core:** Set Theory, Boolean Logic & Rule Analysis


## 🎯 Future Scope

* AI-assisted firewall rule optimization
* Visual rule conflict graph
* Automatic rule ordering recommendations
* Risk scoring for firewall policies
* Support for multiple firewall rule formats
* Real-time firewall configuration analysis

## 📄 License

This project is developed for **educational and cybersecurity research purposes**.
.