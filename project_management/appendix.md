# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Project Management Templates

### A.1 Project Charter Template

```text
PROJECT CHARTER
===============
Project Name: ___________________________
Project Sponsor: _________________________
Project Manager: ________________________
Date: ___________________________________

OBJECTIVE
---------
What problem are we solving, and what is the measurable outcome?
[1-3 sentences, quantifiable where possible]

SCOPE
-----
In Scope:
  - ...
  - ...
Out of Scope:
  - ...
  - ...

DELIVERABLES
------------
1. ...
2. ...
3. ...

TIMELINE
--------
Milestone 1: [Description] — Target Date: ____
Milestone 2: [Description] — Target Date: ____
Final Delivery: ____

ASSUMPTIONS
-----------
- ...
- ...

CONSTRAINTS
-----------
- Budget: ___
- Team size: ___
- Fixed deadlines: ___

SUCCESS METRICS
---------------
- [Metric 1]: [Target value]
- [Metric 2]: [Target value]

APPROVALS
---------
Sponsor: ________________________ Date: ____
PM:      ________________________ Date: ____
```

### A.2 Sprint Planning Template

```text
SPRINT PLANNING
===============
Sprint Number: ___   Duration: ___ days
Sprint Goal: ___________________________
Team Capacity: ___ story points (or ___ hours)

BACKLOG ITEMS FOR THIS SPRINT
------------------------------
ID    | Description                        | Points | Owner     | Risk
------|------------------------------------|--------|-----------|------
US-01 | ...                                | 3      | @alice    | Low
US-02 | ...                                | 5      | @bob      | Med

DEPENDENCIES
------------
- US-02 depends on API being ready from Team X by Day 3
- ...

RISKS / BLOCKERS
----------------
1. [Risk description] — Mitigation: ...
2. ...

DEFINITION OF DONE (applies to all items)
------------------------------------------
□ Code reviewed and approved
□ Tests written and passing
□ Deployed to staging
□ Acceptance criteria verified by PM or QA
□ Documentation updated
```

### A.3 Risk Register Template

```text
RISK REGISTER
=============
Project: _______________   Last Updated: ____

ID  | Description           | Prob | Impact | Score | Owner  | Mitigation          | Contingency
----|-----------------------|------|--------|-------|--------|---------------------|------------
R01 | Third-party API outage| Med  | High   | High  | @alice | Implement fallback  | Use cached data
R02 | Key dev leaves team   | Low  | High   | Med   | PM     | Document all work   | Hire contractor
R03 | Scope creep           | High | Med    | High  | PM     | Change control proc | Buffer sprint

Probability: Low / Medium / High
Impact: Low / Medium / High
Score = Prob × Impact (Low=1, Med=2, High=3) → 1-3=Low, 4-6=Med, 7-9=High
```

### A.4 Status Report Template

```text
STATUS REPORT — WEEK OF ____________
=====================================
Project: _______________
PM: ____________________
Overall Status: 🟢 Green / 🟡 Yellow / 🔴 Red

PROGRESS THIS WEEK
------------------
- Completed: [Items delivered]
- In Progress: [Items currently being worked on]
- % Complete (overall): ___%

METRICS
-------
- Scope: [X of Y planned features delivered]
- Schedule: [On track / X days behind]
- Budget: [$X spent of $Y budget]

KEY DECISIONS MADE
------------------
1. ...

BLOCKERS & RISKS
----------------
1. [Blocker] — Owner: ___ — Resolution by: ____

NEXT WEEK PLAN
--------------
- ...

DECISIONS REQUIRED
------------------
1. [Decision needed] — Deadline: ____
```

### A.5 Retrospective Template (4Ls Format)

```text
SPRINT RETROSPECTIVE — Sprint ___
===================================
Date: ___   Facilitator: ___

LIKED (What went well?)
-----------------------
- ...

LEARNED (What did we learn?)
-----------------------------
- ...

LACKED (What was missing or could improve?)
--------------------------------------------
- ...

LONGED FOR (What do we wish we had?)
--------------------------------------
- ...

ACTION ITEMS
------------
Action                          | Owner   | Due Date
-------------------------------|---------|----------
...                             | @name   | [date]
```

---

## Appendix B: Glossary

**Agile**
An iterative approach to project management and software development. Work is delivered in short cycles called sprints or iterations. Key values: working software over documentation, customer collaboration over contracts, responding to change over following a plan.

**Sprint**
A fixed-length development cycle (typically 1-4 weeks) in Scrum. At the end, the team delivers a potentially shippable increment of work. Sprint length should be consistent across the project.

**Scrum**
A specific Agile framework with defined roles (Product Owner, Scrum Master, Development Team), ceremonies (Sprint Planning, Daily Standup, Sprint Review, Retrospective), and artifacts (Product Backlog, Sprint Backlog, Increment).

**Kanban**
A workflow visualization method. Work items are represented as cards on a board with columns representing states (To Do, In Progress, Done). Work-in-progress (WIP) limits prevent teams from taking on too much at once.

**WIP (Work in Progress)**
The number of tasks a team or individual is actively working on. Limiting WIP prevents context-switching overhead and reveals bottlenecks.

**Velocity**
The amount of work (measured in story points) a Scrum team completes in a sprint. Used for sprint planning and release forecasting. Not a productivity metric — only meaningful within a single team.

**Story Points**
A relative unit for estimating effort and complexity of user stories. Not hours. Teams assign points using techniques like Planning Poker. Common scales: Fibonacci (1, 2, 3, 5, 8, 13...).

**User Story**
A brief description of a feature from the user's perspective: "As a [type of user], I want [goal] so that [reason]." Acceptance criteria define when the story is done.

**Acceptance Criteria**
Specific, testable conditions that define when a user story is complete and correct. Agreed upon before development starts.

**Definition of Done (DoD)**
Team-level standards that every increment must meet before it is considered "done." Typically includes code review, tests passing, documentation updated, deployed to staging.

**Backlog**
An ordered list of work items (features, bug fixes, improvements) for a product. Maintained and prioritized by the Product Owner.

**Backlog Refinement / Grooming**
The ongoing process of reviewing, estimating, and prioritizing backlog items before they enter a sprint. Ensures the backlog is ready, small enough items are broken down, and items are estimated.

**Epic**
A large body of work that can be broken down into multiple user stories. Usually represents a significant feature or initiative.

**Burndown Chart**
A graph showing remaining work (y-axis) over time (x-axis) within a sprint or release. A healthy burndown trends toward zero by the sprint end.

**RACI Matrix**
Responsibility assignment matrix. For each task or decision, defines who is: **R**esponsible (does the work), **A**ccountable (owns the outcome), **C**onsulted (provides input), **I**nformed (notified of outcome).

**Critical Path**
The longest sequence of dependent tasks in a project. Delays on the critical path delay the entire project. Non-critical path tasks have "float" (slack time).

**MVP (Minimum Viable Product)**
The simplest version of a product that delivers value to users and enables learning. Not a buggy half-built product — a complete (small) solution to a real problem.

**OKRs (Objectives and Key Results)**
A goal-setting framework. An Objective is a qualitative, inspirational goal. Key Results are specific, measurable outcomes that indicate whether the Objective is achieved.

**KPI (Key Performance Indicator)**
A quantifiable metric used to evaluate progress toward a business objective. Unlike OKR Key Results, KPIs are ongoing metrics (e.g., monthly active users, deployment frequency).

---

## Appendix C: Certification Roadmaps

| Certification | Focus | Best For | Prerequisites |
|---------------|-------|----------|---------------|
| **PMI-ACP** | Agile practices (Scrum, Kanban, SAFe, XP) | Agile PMs, Scrum Masters | 21 hours Agile training, project experience |
| **PMP** | Traditional + Agile project management | Experienced PMs | 36+ months PM experience |
| **CSM** (Certified Scrum Master) | Scrum fundamentals | Team leads, developers new to Scrum | 2-day training course |
| **CSPO** (Certified Scrum Product Owner) | Product ownership, backlog management | Product owners | 2-day training course |
| **PSM I** (Professional Scrum Master) | Scrum framework | Anyone | None (exam-only path) |
| **PRINCE2 Foundation** | Structured project method | UK/EU public sector, large orgs | None |
| **SAFe Agilist (SA)** | Scaled Agile Framework | Enterprise Agile | 1-day training |

---

## Appendix D: Tools Comparison

| Category | Options | Notes |
|----------|---------|-------|
| **Issue tracking** | Jira, Linear, GitHub Issues, Azure DevOps | Jira: enterprise-grade; Linear: fast and opinionated; GitHub Issues: great for OSS |
| **Documentation** | Confluence, Notion, Obsidian, GitHub Wiki | Confluence pairs with Jira; Notion flexible; Obsidian local-first |
| **Communication** | Slack, Microsoft Teams, Discord | Teams: Microsoft ecosystem; Slack: more integrations |
| **Diagramming** | Miro, Lucidchart, Draw.io, Excalidraw | Excalidraw: free, collaborative; Miro: whiteboard-focused |
| **Roadmap planning** | Productboard, Aha!, Jira Roadmaps | Depends on team size and Agile maturity |
| **Time tracking** | Toggl, Harvest, Clockify | Clockify: free tier; Toggl: UX-friendly |
