

# W01

## Question

2 options, which do you prefer: $Θ(n^3)$, or $Ο(n^4)$ and $Ω(n^2)$. And why



## Answer

**Left, right, or create a third way**



The information provided is pretty limited, so I would like to introduce a few thoughts before we make a decision. 



**Requirement:** 

- The requirement is always the most critical factor in picking an algorithm. It will guide us in the various trade-off, such as runtime/memory(or storage). In most cases, the runtime is the most crucial factor, but it might not always be true. 
- Stability. It looks like algorithm 1 might be more stable than algorithm 2. It might be worth double-checking with the requirement. 

**Data**

- Data volume. For a small amount of data, runtime might not be the primary factor in making a decision.  But if data is big enough, then Ο(n^4) might completely not acceptable. So we might have to pick algorithm 1. 
- Data distribution: Regardless of the complexity, the data distribution will impact the overall runtime cost.  If most of the data on algorithm 2 will get Ω(n^2) and only minimal cases will on Ο(n^4), then overall algorithm 2 might have a chance to perform better than algorithm 1. On the other hand, if the data is pretty balanced, then Θ(n^3) might provide better runtime with extra stability. 

**Technical** 

- Runtime: Discussed above. We have introduced Big-O as qualitative analysis but not go one deep further to talk about the constant, the c before Big-O for quantitative analysis. If the data volume is small, the situation is complex, as mentioned in the lecture. In some cases, Θ(n^3) might be worse than Ο(n^4) depends on the constant c and data range. 
- Memory/Storage: Not provided. 
- Other factors, such as network communication: Not provided

**Non-technical** 

- Maturity, Robust: Stability might be a perspective we need to consider. 
- Overhead cost. Such as easy to development and test, long-term maintenance cost, and match with the current technical architect or roadmap. 



There are many things that need to consider, but we already go pretty far.  Last but not least, I would provide a third option: to create a **Hybrid solution**. Suppose we are dealing with a massive amount of data and this program plays an essential role in the business. In this case, 

- Engineering perspective: it might be worth pre-processing the data, dividing them into two groups, and applying both algorithms to get a hybrid solution. 
- Service perspective: If we can process the cases in parallel, then we can set an upper limit of the processing time. As long as 99% of cases get processed quick enough, we are good. We might create a separate process to deal with the 1%. 