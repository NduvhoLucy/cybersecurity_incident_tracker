## Reflection: Modeling Challenges and Alignment with Agile

### 1. Challenges in Choosing Granularity for States and Actions

One of the main challenges in creating both state and activity diagrams was determining the right level of granularity. Including too much detail made diagrams cluttered and harder to follow, while too little detail made them overly simplistic and lacking context.

For state diagrams, it was tempting to model every internal status an object could possibly enter, such as “Queued for Review,” “Reassigned,” or “Awaiting Evidence.” However, to maintain readability and coherence, we focused on high-level, meaningful states such as “Open,” “In Progress,” “Resolved,” and “Closed.” These states reflected clear transitions relevant to both developers and stakeholders, balancing abstraction with clarity.

Similarly, in activity diagrams, we had to carefully select which actions to show. For example, in the "Log Security Incident" workflow, including every micro-step (e.g., "Click submit," "Wait for confirmation") would overwhelm the reader. Instead, we emphasized major functional actions like “Fill Incident Form,” “Attach Evidence,” and “Submit for Review.” This choice made the diagrams more digestible while still conveying core logic.

### 2. Aligning Diagrams with Agile User Stories

Aligning the diagrams with Agile user stories was another thoughtful process. Each use case and workflow diagram needed to reflect the functionality defined in the user stories. For example, the user story *"As a Security Analyst, I want to log incidents so that they are properly documented"* directly maps to both the state diagram of the `Incident` object and the activity diagram for the "Log Security Incident" workflow.

This alignment helped validate that the diagrams were grounded in actual requirements. However, because Agile stories tend to be concise and user-focused, expanding them into complete visual flows required thoughtful interpretation. We had to infer system responses and user interactions not explicitly stated in the stories, all while maintaining consistency with the intended value of each user story.

### 3. Comparing State Diagrams vs. Activity Diagrams

State diagrams and activity diagrams serve different but complementary purposes. State diagrams focus on the lifecycle of a single object (like an `Incident` or `User`), showing how it transitions from one state to another based on events or actions. This is useful for understanding object behavior and internal state logic.

In contrast, activity diagrams model the entire process or workflow, often involving multiple roles (via swimlanes) and decision points. For example, the "Generate Security Report" activity diagram involves user input, system filtering, and multiple output options—all in a single flow.

In essence, state diagrams answer *"What happens to this object over time?"* while activity diagrams answer *"What steps are followed in this process?"* Using both gave a holistic understanding of the system from both a data and user interaction perspective.

