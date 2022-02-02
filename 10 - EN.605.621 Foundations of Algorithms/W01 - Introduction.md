### Analysis of Algorithms

- The theoretical study of computer-program performance and resource usage
- What's more important than performance?
  - Correctness
  - Functionality
  - Maintainability
  - Robustness
  - Extensibility
  - Programmer Time
  - Simplicity
  - Modularity
  - Reliability

### Why study algorithms and performance?

- Algorithms help us to understand **scalability**
- Performance often draws the line between what is feasible and what is impossible
- Algorithmic mathematics provides a **language** for talking about program behavior
- Performance is the **currency** of computing
- The lessons of program performance generalize to other computing resources
- Speed is fun!

### Compare algorithms

Approaches

- Implement the algorithms and run a series of experiments: Not general. 
- Apply formal mathematical analysis to the algorithm to determine what the complexity bounds are.

Questions: what performance bounds to focus, worst or average?

Asymptotic performance

- We should not ignore asymptotically slower algorithms, however
- Real-world design situations often call for a careful balancing of engineering objectives
- Asymptotic analysis is a useful tool to help to structure our thinking

In practice, merge sort beats insertion sort for n >30 or so. 

### Growth Functions

Asymptotic Notation in Equations

- Right side: For **some** anonymous functions, euqation valid. The equal sign means set membership
- Left side: **No matter how** the anomymous functions are chosen on the **left** side, **there is a way** to choose the anonymous functions on the **right** hand to make the equation valid. 
- Formula: when asymptotic notation appears in a formula, we interpret it as standing for some anonymous function that we do not care to name

**Asymptotically tight bounds**: $\Theta$

Comparison of functions

- a)  transitivity
- b)  reflexitivity
- c)  symmetry
- d)  transpose symmetry
- e)  trichotomy

### Homework Expectation

**Personal statement of integrity on EVERY assignment**: ‒I, <*your name*>, attempted to answer each question honestly and to the best of my abilities. I cited any, and all, help that I received in completing this assignment.

**Every algorithm for grading**

- Pseudocode
- Natural language describe
- Asymptotic runtime analysis

**Rule of 1-2-3**

- For every single (**one**) homework problem: 

  - Read it through **TWICE** before each attempt, and

  - Make **THREE** REASONABLE attempts
    - Attempt 1: Solve it. Look for related examples. reread the chapter, then *put it down*
    - Attempt 2: Try one day later. Write down your thoughts. Reread chapter / search elsewhere in the book
    - **Attempt 3: Try it one day later. Search for solution: Summary your thoughts. write it down. Search. Cite the solution. Write the solution in your own word, think why it is correct. Compare with your previous thinking.** 

  - [Submit for grading only your final solution]

- Every Attempt

  - Put down distractions (phone, work, pets, social media, “The Office,” …)

  - Attempt the problem

  - Set a *minimum* time limit, “I’ll try this for at least 10 minutes.”

  - Consult the text – **ALWAYS** okay to read the book (or other books)

  - Review, did I answer the question?

- **Your first impulse should not be to search the Internet for a solution**

**Citation**

- Sheridan Libraries' citation guidance: ["Citing Other Things - HOW DO YOU CITE AN INTERVIEW, A TWEET, OR A PUBLIC WEB PAGE?](https://guides.library.jhu.edu/citing/other) 
- Purdue University, Purdue Online Writing Lab (OWL), College of Liberal Arts: [Reference List: Electronic Sources](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/reference_list_electronic_sources.html)
- Victoria University Library, Melbourne Australia: [Harvard Referencing: Internet/websites](https://libraryguides.vu.edu.au/harvard/internet-websites)