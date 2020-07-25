# Writing technical specification

*This note is based on [an article by Zara Cooper][article].*

Writing code before writing a good technical spec document can be disastrous to the project being worked on.
The idea of writing code *and* figuring out the “what and how” of a solution to a given problem is irresponsible.

- [Why write such a document](#why-write-such-a-document)
- [Benefits](#benefits)
- [Gathering data](#gathering-data)
- [Document contents](#document-contents)
  - [1. Front cover](#1-front-cover)
  - [2. Introduction](#2-introduction)
    - [2.1 Overview](#21-overview)
    - [2.2 Terminology](#22-terminology)
    - [2.3 Context](#23-context)
    - [2.4 Technical requirements](#24-technical-requirements)
    - [2.5 User wish-list](#25-user-wish-list)
    - [2.6 Out of scope](#26-out-of-scope)
    - [2.7 Future goals](#27-future-goals)
  - [3. Solutions](#3-solutions)
    - [3.1 Current handling of the problem](#31-current-handling-of-the-problem)
    - [3.2 Proposed solution](#32-proposed-solution)
    - [3.3 Test Plan](#33-test-plan)
    - [3.4 Monitoring and altering plans](#34-monitoring-and-altering-plans)
    - [3.5 Deployment plans](#35-deployment-plans)
    - [3.6 Rollback plan](#36-rollback-plan)
    - [3.7 Alternate solutions](#37-alternate-solutions)
  - [4. Further Considerations](#4-further-considerations)
    - [4.1 Impact on other teams](#41-impact-on-other-teams)
    - [4.2 Third-party services and platforms considerations](#42-third-party-services-and-platforms-considerations)
    - [4.3 Cost analysis](#43-cost-analysis)
    - [4.4 Security considerations](#44-security-considerations)
    - [4.5 Privacy considerations](#45-privacy-considerations)
    - [4.6 Regional considerations](#46-regional-considerations)
    - [4.7 Accessibility considerations](#47-accessibility-considerations)
    - [4.8 Operational considerations](#48-operational-considerations)
    - [4.9 Risks](#49-risks)
    - [4.10 Support considerations](#410-support-considerations)
  - [5. Success Evaluation](#5-success-evaluation)
    - [5.1 Impact](#51-impact)
    - [5.2 Metrics](#52-metrics)
  - [6. Work cost](#6-work-cost)
    - [6.1 Work estimates and timelines](#61-work-estimates-and-timelines)
    - [6.2 Prioritization](#62-prioritization)
    - [6.3 Milestones](#63-milestones)
    - [6.4 Future work](#64-future-work)
  - [7. Deliberation](#7-deliberation)
    - [7.1 Discussion](#71-discussion)
    - [7.2 Open questions](#72-open-questions)
  - [8. End cover](#8-end-cover)
    - [8.1 Related work](#81-related-work)
    - [8.2 References](#82-references)
    - [8.3 Acknowledgements](#83-acknowledgements)
- [Source](#source)

## Why write such a document

One can think of such spec document as the *model* of the solution to the given problem, meaning the shape of the programs and other utilities that will be crafted during the implementation process. It is the first mock-up that is the foundation of later iterations of a proposed solution. A draft that is later perfected, *a first input solution that we inject into the metaheuristic algorithm that the team working on a solution is.*

In simpler terms: a set of guidelines that enables the creators of the project to converge towards the perfect solution.

## Benefits

This spec document can be beneficial to *all* members of the team working on given project.

Engineers are forced to fully understand the topic and better prepare for creating an appropriate solution.

It is still a technical way of describing given problem, but much more understandable (human-readable text instead of pure code) for the other non-engineer members of the team.

The document sums up the purpose of the project and the proposed solution to the problem.

## Gathering data

The spec document also gives an opportunity to gather as much vital (both about the problem and about possible solutions) information, compile it and avail it to all members of the team.

Afterwards, feedback can be acquired from members of the team or from external sources.

## Document contents

### 1. Front cover

- Title
- Author(s)
- Team
- Reviewers
- Date (creation and last modification)

### 2. Introduction

#### 2.1 Overview

*Problem description, summary, abstract*

High-level abstract description (from the perspective of a standard user). Gives information about the “what and how” in simple terms, the context and a proposed solution to the problem.

#### 2.2 Terminology

*Set of definitions specific to this project*

For better communication between various users and creators of the solution a set of terms and their clear definitions should be established.

#### 2.3 Context

- Reason(s) to why the problem is worth solving
- Origin of the problem
- How the problem affects others
- If there were any: past efforts made to solve the solution and why they were not sufficient
- How the proposed solution fits the problem

#### 2.4 Technical requirements

List of all technical utilities that are necessary to create a solution to the problem. These include both what hardware and software has to be used to accomplish tasks set out in the proposed solution.

#### 2.5 User wish-list

A set of stories, requirements and wish-lists of the actual to-be-users of this solution.

#### 2.6 Out of scope

List of all goals that will not be achieved.

#### 2.7 Future goals

Future research that can be conducted on the problem and list of all concerns that may be a problem after the solution is implemented.

### 3. Solutions

#### 3.1 Current handling of the problem

- Current solution description
- Advantages and drawbacks of the currently utilised solution or half-solution

#### 3.2 Proposed solution

- External components that the solution will interact with and that it will alter
- Advantages and drawbacks of the proposed solution
- Data model/schemas
  - Data model definition
  - Data validation methods
- Business Logic
  - API changes
  - Pseudocode
  - Flowcharts
  - Error states
  - Failure scenarios
  - Conditions that lead to errors and failures
  - Limitations
- Presentation layer
  - User requirements
  - UX and UI changes
  - Wireframes with descriptions
  - Links to UI/UX designer’s work
  - Concerns about usability on other platforms e.g. mobile, web
  - UI states
  - Error handling
- Questionnaire
  - How will the solution scale?
  - What are the limitations of the solution?
  - How ill it recover in the event of a failure?
  - How will it cope with future requirements?
    - Is it maintainable?
    - Is it modular? (easy upgrades step-by-step)

#### 3.3 Test Plan

- Explanations of how the tests will make sure user requirements are met
- Unit tests
- Integration tests
- Quality Assurance

#### 3.4 Monitoring and altering plans

- Logging and monitoring plans and tools
- Metrics to be used to measure health
- How to ensure observability?
- Altering plan and tools

#### 3.5 Deployment plans

- Deployment architecture
- Deployment environments
- Phased roll-out plan e.g. using feature flags
- Plan outlining how to communicate changes to the users, for example, with release notes

#### 3.6 Rollback plan

- Detailed and specific liabilities
- Plan to reduce liabilities
- Plan describing how to prevent other components, services, and systems from being affected

#### 3.7 Alternate solutions

- Short summery statement for each alternative solution
- Advantages and drawback for each alternative solution
- Reasons why each solution is not applicable
- Ways in which alternatives were inferior to the proposed solution
- Migration plan to next best alternative in case the proposed solution isn’t sufficient

### 4. Further Considerations

#### 4.1 Impact on other teams

How will this increase the work of other people?

#### 4.2 Third-party services and platforms considerations

- Is it really worth i compared to building the service in-house?
- What are some of the security and privacy concerns associated with the services/platoforms?
- How much will it cost?
- How will it scale?
- What possible future issues are anticipated?

#### 4.3 Cost analysis

- What is the cost to run the solution per day?
- What does it cost to roll it out?

#### 4.4 Security considerations

- What are the potential threats?
- How will they be mitigated?
- How will the solution affect the security of other components, services and systems?

#### 4.5 Privacy considerations

- Does the solution follow local laws and legal policies on data privacy?
- How does the solution protect users’ data privacy?
- What are some of the trade-offs between personalization and privacy in the solution?

#### 4.6 Regional considerations

- What is the impact of the internationalization and localization on the solution?
- What are the latency issues?
- What are the legal concerns?
- What is the state of service availability?
- How will data transfer across regions be achieved and what are the concerns here?

#### 4.7 Accessibility considerations

- How accessible is the solution?
- What tools will you use the evaluate its accessibility?
- Are there users that will need other means of communicating/interacting with the proposed solution?

#### 4.8 Operational considerations

- Does this solution cause adverse after-effects?
- How will data be recovered in case of failure?
- How will the solution recover in case of a failure?
- How will operational costs be kept low while delivering increased value to the users?

#### 4.9 Risks

- What risks are being undertaken with this solution?
- Are there risks once taken can’t be walked back?
- What is the cost-benefit analysis of taking these risks?

#### 4.10 Support considerations

- How will the support team get across information to users about common issue they may face while interacting with the changes?
- How will we ensure that the users are satisfied with the solution and can interact with it with minimal support?
- Who is responsible for the maintenance of the solution?
- How will knowledge transfer be accomplished if the project owner is unavailable?

### 5. Success Evaluation

#### 5.1 Impact

- Security impact
- Performance impact
- Cost impact
- Impact on other components and services

#### 5.2 Metrics

- List of metrics to capture
- Tools to capture and measure metrics

### 6. Work cost

#### 6.1 Work estimates and timelines

- List of specific, measurable and time-bound tasks
- Resource needed to finish each task
- Time estimates for how long each task needs to be completed

#### 6.2 Prioritization

Categorization of tasks by urgency and impact

#### 6.3 Milestones

- Dated checkpoints when significant chunks of work will have been completed
- Metrics to indicate the passing of the milestone

#### 6.4 Future work

List of tasks that will be completed in the future.

### 7. Deliberation

#### 7.1 Discussion

Elements of the solution that members of the team do not agree on and need to be debated further to reach a consensus.

#### 7.2 Open questions

Questions about things you do not know the answers to or are unsure that you pose to the team and stakeholders for their input. These may include aspects of the problem you don’t know how to resolve yet.

### 8. End cover

#### 8.1 Related work

Any work external to the proposed solution that is similar to i in some way is worked on by different teams. It’s important to know this to enable knowledge sharing between such teams when faced with related problems.

#### 8.2 References

Links to documents and resources that were used when coming up with the desing and wish to credit.

#### 8.3 Acknowledgements

Credit people who have contributed to the desing that you wish to reorganize.

---

## Source

[article]: https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/

[Original article by Zara Cooper][article]

This note is mainly based on the above mentioned article with some minor modifications.
