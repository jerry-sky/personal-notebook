---
lang: 'en-GB'
title: 'Writing technical specification'
author: 'Jerry Sky'
description: |
    Writing code before writing a good technical spec document can be disastrous to the project being worked on. The idea of writing code and figuring out the “what and how” of a solution to a given problem is irresponsible.\
    *This note is based on [an article by Zara Cooper][article].*
keywords: 'software, engineering, specification, technical, code, document, data, solutions, proposed'
---



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

### Front cover

- Title
- Author(s)
- Team
- Reviewers
- Date (creation and last modification)

### Introduction

#### Overview

*Problem description, summary, abstract*

High-level abstract description (from the perspective of a standard user). Gives information about the “what and how” in simple terms, the context and a proposed solution to the problem.

#### Terminology

*Set of definitions specific to this project*

For better communication between various users and creators of the solution a set of terms and their clear definitions should be established.

#### Context

- Reason(s) to why the problem is worth solving
- Origin of the problem
- How the problem affects others
- If there were any: past efforts made to solve the solution and why they were not sufficient
- How the proposed solution fits the problem

#### Technical requirements

List of all technical utilities that are necessary to create a solution to the problem. These include both what hardware and software has to be used to accomplish tasks set out in the proposed solution.

#### User wish-list

A set of stories, requirements and wish-lists of the actual to-be-users of this solution.

#### Out of scope

List of all goals that will not be achieved.

#### Future goals

Future research that can be conducted on the problem and list of all concerns that may be a problem after the solution is implemented.

### Solutions

#### Current handling of the problem

- Current solution description
- Advantages and drawbacks of the currently utilised solution or half-solution

#### Proposed solution

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

#### Test Plan

- Explanations of how the tests will make sure user requirements are met
- Unit tests
- Integration tests
- Quality Assurance

#### Monitoring and altering plans

- Logging and monitoring plans and tools
- Metrics to be used to measure health
- How to ensure observability?
- Altering plan and tools

#### Deployment plans

- Deployment architecture
- Deployment environments
- Phased roll-out plan e.g. using feature flags
- Plan outlining how to communicate changes to the users, for example, with release notes

#### Rollback plan

- Detailed and specific liabilities
- Plan to reduce liabilities
- Plan describing how to prevent other components, services, and systems from being affected

#### Alternate solutions

- Short summery statement for each alternative solution
- Advantages and drawback for each alternative solution
- Reasons why each solution is not applicable
- Ways in which alternatives were inferior to the proposed solution
- Migration plan to next best alternative in case the proposed solution isn’t sufficient

### Further Considerations

#### Impact on other teams

How will this increase the work of other people?

#### Third-party services and platforms considerations

- Is it really worth i compared to building the service in-house?
- What are some of the security and privacy concerns associated with the services/platoforms?
- How much will it cost?
- How will it scale?
- What possible future issues are anticipated?

#### Cost analysis

- What is the cost to run the solution per day?
- What does it cost to roll it out?

#### Security considerations

- What are the potential threats?
- How will they be mitigated?
- How will the solution affect the security of other components, services and systems?

#### Privacy considerations

- Does the solution follow local laws and legal policies on data privacy?
- How does the solution protect users’ data privacy?
- What are some of the trade-offs between personalization and privacy in the solution?

#### Regional considerations

- What is the impact of the internationalization and localization on the solution?
- What are the latency issues?
- What are the legal concerns?
- What is the state of service availability?
- How will data transfer across regions be achieved and what are the concerns here?

#### Accessibility considerations

- How accessible is the solution?
- What tools will you use the evaluate its accessibility?
- Are there users that will need other means of communicating/interacting with the proposed solution?

#### Operational considerations

- Does this solution cause adverse after-effects?
- How will data be recovered in case of failure?
- How will the solution recover in case of a failure?
- How will operational costs be kept low while delivering increased value to the users?

#### Risks

- What risks are being undertaken with this solution?
- Are there risks once taken can’t be walked back?
- What is the cost-benefit analysis of taking these risks?

#### Support considerations

- How will the support team get across information to users about common issue they may face while interacting with the changes?
- How will we ensure that the users are satisfied with the solution and can interact with it with minimal support?
- Who is responsible for the maintenance of the solution?
- How will knowledge transfer be accomplished if the project owner is unavailable?

### Success Evaluation

#### Impact

- Security impact
- Performance impact
- Cost impact
- Impact on other components and services

#### Metrics

- List of metrics to capture
- Tools to capture and measure metrics

### Work cost

#### Work estimates and timelines

- List of specific, measurable and time-bound tasks
- Resource needed to finish each task
- Time estimates for how long each task needs to be completed

#### Prioritization

Categorization of tasks by urgency and impact

#### Milestones

- Dated checkpoints when significant chunks of work will have been completed
- Metrics to indicate the passing of the milestone

#### Future work

List of tasks that will be completed in the future.

### Deliberation

#### Discussion

Elements of the solution that members of the team do not agree on and need to be debated further to reach a consensus.

#### Open questions

Questions about things you do not know the answers to or are unsure that you pose to the team and stakeholders for their input. These may include aspects of the problem you don’t know how to resolve yet.

### End cover

#### Related work

Any work external to the proposed solution that is similar to i in some way is worked on by different teams. It’s important to know this to enable knowledge sharing between such teams when faced with related problems.

#### References

Links to documents and resources that were used when coming up with the desing and wish to credit.

#### Acknowledgements

Credit people who have contributed to the desing that you wish to reorganize.

---


## Source

[article]: https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/

[Original article by Zara Cooper][article]

This note is mainly based on the above mentioned article with some minor modifications.
