---
name: research-classifier
description: Classify an AI R&D session into exactly one leaf task from a supplied taxonomy using the dominant objective, action, and research-boundary rules.
---

# Research classifier

Use this skill when the user asks to classify a session, route research work, identify research intent, or apply an AI R&D task taxonomy.

## Workflow

1. Read the objective-focused session view. Use user messages and assistant-facing summaries; treat tool outputs as omitted unless the session view explicitly includes their meaning.
2. Identify the primary objective and the dominant action: planning/specifying, implementing, operating, analyzing, or communicating.
3. Separate the object of work from supporting steps. Classify the work the user sought, not merely the tool or action used.
4. Choose the single most specific leaf task from the supplied taxonomy.
5. If several activities occur, choose the leaf representing the main objective and bulk of the work. Supporting steps, a final test, launch, review, question, status check, or write-up do not outweigh substantive preceding work.
6. Apply the boundaries below before selecting a label.
7. Return exactly one taxonomy leaf label, or `No matching AI R&D task`. Return no explanation or additional text.

## Boundaries

- **Scope:** The taxonomy covers AI for research, training and evaluation systems, model behavior, model serving, and researchers' workflows. Generic software engineering or administrative work belongs outside the taxonomy unless it directly serves an AI R&D objective.
- **Research planning:** Use research-planning leaves only for model, training, or evaluation experiments. A generic project, QA, or application-security plan is not an experiment plan unless it contains a research experiment.
- **Prediction:** A concrete, testable expected outcome stated before an experiment runs is `Predict the experiment result with a falsifiable prediction before running`, rather than a broader design or plan-writing label.
- **Experiment design:** Choosing ablations, scale, or baselines is `Design the experiment that tests the approach (which ablations, at what scale, against what baselines)`.
- **Experimental plan:** Writing the complete protocol, controls, ablations, baselines, hyperparameters, scale, and success criteria is `Write the experimental plan (full protocol with controls, ablations, baselines, hyperparams, scale, success criteria)`.
- **Specification and grading:** Writing or changing a reward function, evaluation protocol, or grading rubric is specification work. Applying a supplied rubric to one answer, search result, or performance item is not the same as creating the specification.
- **Model-behavior analysis:** `Analyze model behavior on evals` requires examining model outputs to characterize successes, failures, or behavioral patterns. Ordinary product testing is not model-behavior analysis without a broader AI R&D objective.
- **Feedback analysis:** Analyze user feedback and complaints when the objective is to understand a user-perceived model failure, including support tickets, thumbs-down reports, or user reports.
- **Run operations:** Monitoring runs concerns active training, RL, or evaluation runs: launching, monitoring health, or restoring them. Use `Experiment outcomes` for post-hoc interpretation, validity checks, or statistical analysis of results.
- **Infrastructure:** Hardware infrastructure operations concerns cluster capacity, nodes, accelerators, fabric, or storage. Inference reliability engineering concerns deployments, capacity, routing, and inference incidents.
- **AI data jobs:** For active AI-data-generation or pretokenization jobs, use Monitoring runs when babysitting or restoring the job; use Datasets when constructing or transforming the data.
- **Research implementation:** If the task is writing software or interacting with technical systems such as git and does not fit a research category, use the relevant implementation leaf, commonly `Write code to implement research and development` if that leaf exists in the taxonomy.
- **Communication:** Communication leaves require substantively authoring a report, documentation, feedback, or status update for others. A small write-up after substantial implementation, debugging, or analysis does not change the primary classification.
- **Review and questions:** Use `Review code` when code review is the dominant objective. Use `Answer a technical question` only when answering the technical question is the bulk of the session.

## Input contract

The caller must provide:

- an objective-focused session view; and
- the complete taxonomy, substituted for `{{TAXONOMY}}`.

Do not infer missing taxonomy labels. If the session view is insufficient or the primary objective is not AI R&D, return `No matching AI R&D task`.

## Output contract

Output exactly one leaf-task label from the supplied taxonomy, or:

`No matching AI R&D task`
