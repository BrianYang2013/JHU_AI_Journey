1. $\begin{bmatrix}
2 & -1 & 3\\
0 & 0 & 0\\
\end{bmatrix}$, Rank=1, $\{[2, -1, 3]\}$

$A^T=\begin{bmatrix}
2 & -1\\
0 & 0\\
0 & 0\\
\end{bmatrix}$,$\{[2, -1]^T\}$

2. $\begin{bmatrix}
a & b \\
a & \frac{a^2}{b} \\
\end{bmatrix}$,
if $a=b=0$, rank = 0, $\{0\}$, $\{0\}$
if $b=\pm a$, rank = 1, $\{[1, -1]\}$, $\{[1, -1]^T\}$
The rest, rank = 2, $\{[a, b], [b, a]\}$, $\{[a, b]^T, [b, a]^T\}$
$~\\$

3. $\begin{bmatrix}
1 & 0 & 2\\
0 & 3 & 5\\
0 & 5 & 6\\
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 2\\
0 & 1 & 5/3\\
0 & 0 & 1\\
\end{bmatrix}$, rank = 3, $\{[1,0,0], [0, 1, 0], [0, 0, 1]\}$,$\{[1,0,0]^T, [0, 1, 0]^T, [0, 0, 1]^T\}$,
$~\\$

4. $\begin{bmatrix}
2 & 0 & 1\\
0 & 1 & 3\\
6 & -4 & 0\\
\end{bmatrix}=\begin{bmatrix}
2 & 0 & 1\\
0 & 1 & 3\\
0 & 0 & 1\\
\end{bmatrix}$, rank = 3, $\{[1,0,0], [0, 1, 0], [0, 0, 1]\}$,$\{[1,0,0]^T, [0, 1, 0]^T, [0, 0, 1]^T\}$,
$~\\$

5. $\begin{bmatrix}
1 & 0 & -21\\
0 & 11 & -3\\
2 & -1 & 4\\
\end{bmatrix}=\begin{bmatrix}
1 & 0 & -21\\
0 & 11 & -3\\
0 & 0 & 1\\
\end{bmatrix}$, rank = 3, $\{[1,0,0], [0, 1, 0], [0, 0, 1]\}$,$\{[1,0,0]^T, [0, 1, 0]^T, [0, 0, 1]^T\}$,
$~\\$

6. $\begin{bmatrix}
1 & 1 & 4\\
0 & 1 & 0\\
0 & 4 & 0\\
\end{bmatrix}=\begin{bmatrix}
1 & 1 & 4\\
0 & 1 & 0\\
0 & 0 & 0\\
\end{bmatrix}$, rank = 2, $\{[1,1,4], [0, 1, 0]\}$,

$A^T=\begin{bmatrix}
0 & -1 & 0\\
1 & 0 & 4\\
0 & -4 & 0\\
\end{bmatrix}=\begin{bmatrix}
1 & -1 & 4\\
0 & 1 & 0\\
0 & 0 & 0\\
\end{bmatrix}$,
$\{[1,-1,4]^T, [0, 1, 0]^T, \}$,
$~\\$

7. $\begin{bmatrix}
2 & 0 & 1 & 0\\
0 & 1 & 0 & 2\\
0 & 0 & 0 & 0\\
\end{bmatrix}$, rank = 2, $\{[2, 0, 1, 0], [0, 1, 0, 2]\}$,
$A^T=\begin{bmatrix}
8 & 0 & 4\\
0 & 2 & 0\\
4 & 0 & 2\\
0 & 4 & 0\\
\end{bmatrix}=\begin{bmatrix}
2 & 0 & 1\\
0 & 1 & 0\\
0 & 0 & 0\\
0 & 0 & 0\\
\end{bmatrix}$, $\{[2, 0, 1]^T, [0, 1, 0]^T\}$,

8. $\begin{bmatrix}
1 & 2 & 4 & 8\\
0 & 12 & 30 & 63\\
0 & 0 & 0 & 1\\
0 & 6 & 0 & -6\\
\end{bmatrix}=\begin{bmatrix}
1 & 2 & 4 & 8\\
0 & 1 & 0 & -1\\
0 & 12 & 30 & 63\\
0 & 0 & 0 & 1\\
\end{bmatrix}=\begin{bmatrix}
1 & 2 & 4 & 8\\
0 & 1 & 0 & -1\\
0 & 0 & 30 & 75\\
0 & 0 & 0 & 1\\
\end{bmatrix}$, rank = 4, $\{[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]\}$,
$\{[1, 0, 0, 0]^T, [0, 1, 0, 0]^T, [0, 0, 1, 0]^T, [0, 0, 0, 1]^T\}$

9. $\begin{bmatrix}
1 & 1 & 1 & 1\\
0 & 0 & 1 & 0\\
0 & 0 & 1 & 0\\
9 & 0 & 1 & 0\\
\end{bmatrix}=\begin{bmatrix}
1 & 1 & 1 & 1\\
0 & 9 & 8 & 9\\
0 & 0 & 1 & 0\\
0 & 0 & 1 & 0\\
\end{bmatrix}$, rank = 3, $\{[1, 1, 1, 1], [0, 9, 8, 9], [0, 0, 1, 0]\}$,

$A^T=\begin{bmatrix}
9 & 0 & 1 & 0\\
0 & 0 & 1 & 0\\
1 & 1 & 1 & 1\\
0 & 0 & 1 & 0\\
\end{bmatrix}$, $\{[9, 0, 1, 0]^T, [0, 0, 1, 0]^T, [1, 1, 1, 1]^T \}$

10. $\begin{bmatrix}
1 & -4 & -11 & 2\\
0 & 1 & 2 & 0\\
5 & -2 & 1 & 0\\
-2 & 0 & -4 & 1\\
\end{bmatrix}=\begin{bmatrix}
1 & -4 & -11 & 2\\
0 & 1 & 2 & 0\\
0 & 0 & 2 & -1\\
0 & 0 & 2 & -1\\
\end{bmatrix}$, rank = 3, $\{[1, -4, -11, 2], [0, 1, 2, 0], [0, 0, 2, -1]\}$,

$A^T=A$, $\{[1, -4, -11, 2]^T, [0, 1, 2, 0]^T, [0, 0, 2, -1]^T\}$

11. New row 1 = row 2 - row 1 = [1, 1, ... , 1]
Add new row 1 to row k will get row k+1. so rank = 2, base is row 1 and row 2.
b) Same
c) All rows similar to row 1, just matter of factor 2^k. So rank = 1

12. $Rank(AB)=Rank[(AB)^T]=Rank(B^TA^T)$

13. $\begin{bmatrix}
1 & 0\\
0 & 0\\
\end{bmatrix}\begin{bmatrix}
1 & 0\\
0 & 0\\
\end{bmatrix}=\begin{bmatrix}
1 & 0\\
0 & 0\\
\end{bmatrix}$

$\begin{bmatrix}
0 & 1\\
0 & 0\\
\end{bmatrix}\begin{bmatrix}
0 & 1\\
0 & 0\\
\end{bmatrix}=\begin{bmatrix}
0 & 0\\
0 & 0\\
\end{bmatrix}$

14. Let A is a $m \times n$ matrix, and assume $m \gt n$
$Rank(A) \le n \lt m$. so A is linearly dependent on the row vectors
verse vise, L.D on the column vectors

15. n = Rank of row = rank of column

16. Matrix A, B, AB.
Let A as the base of the vector space V(A), then V(AB) is the subset of V(A).
$Rank(A)=dim[V(A)] \ge dim[V(AB)] = Rank(AB)$
If B is nonsingular, then Rank(A)=Rank(AB)
Vise verse on B.

17.  $\begin{bmatrix}
1 & 16 & -12 & -22\\
3 & 4 & 0 & 2\\
2 & -1 & 3 & 7\\
\end{bmatrix} = \begin{bmatrix}
1 & 16 & -12 & -22\\
0 & 11 & -9 & -17\\
0 & 33 & -37 & -51\\
\end{bmatrix}=\begin{bmatrix}
1 & 16 & -12 & -22\\
0 & 11 & -9 & -17\\
0 & 0 & 10 & 0\\
\end{bmatrix} $
Linear independent.

18. $\begin{bmatrix}
1 & 1/2 & 1/3 & 1/4\\
30 & 20 & 15 & 12\\
20 & 15 & 12 & 10\\
105 & 84 & 70 & 60\\
\end{bmatrix} = \begin{bmatrix}
1 & 1/2 & 1/3 & 1/4\\
0 & 1 & 1 & 0.9\\
0 & 15 & 16 & 15\\
0 & 126 & 140 & 135\\
\end{bmatrix}=\begin{bmatrix}
1 & 1/2 & 1/3 & 1/4\\
0 & 1 & 1 & 0.9\\
0 & 0 & 1 & 0.1\\
0 & 0 & 14 & 21.6\\
\end{bmatrix} $
Rank = 4, Linear independent.

19. $\begin{bmatrix}
1 & 1 & 1\\
0 & 1 & 1\\
0 & 0 & 1\\
\end{bmatrix}$
Rank = 3, Linear independent.

20. $\begin{bmatrix}
1 & 2 & 3 & 4\\
1 & 1 & 1 & 1\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
\end{bmatrix}$
Rank = 2, Linear Dependent.

21. $\begin{bmatrix}
2 & 0 & 0 & 7\\
2 & 0 & 0 & 8\\
2 & 0 & 0 & 9\\
2 & 0 & 1 & 0\\
\end{bmatrix}=\begin{bmatrix}
2 & 0 & 0 & 7\\
0 & 0 & 0 & 1\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & -7\\
\end{bmatrix}$
Rank = 3, Linear Dependent.

22. V1 * 30/4 = V3, rank=1. Linear Dependent.

23. $\begin{bmatrix}
9 & 8 & 7 & 6 & 5\\
0 & 1 & 2 & 3 & 4\\
\end{bmatrix}$
Rank = 2, Linear independent.

24. 4 rows 3 column, Linear Dependent.

25. $\begin{bmatrix}
1 & 1 & 1 & 1\\
6 & 0 & -1 & 3\\
2 & 2 & 5 & 0\\
\end{bmatrix} = \begin{bmatrix}
1 & 1 & 1 & 1\\
0 & 6 & 7 & 3\\
0 & 0 & 3 & 0\\
\end{bmatrix}$
Rank = 3, Linear independent.

26. $V_4=2V_1$, discard $V_4$
$\begin{bmatrix}
3 & 0 & 1 & 2\\
6 & 1 & 0 & 0\\
12 & 1 & 2 & 4\\
9 & 0 & 1 & 2\\
\end{bmatrix} = \begin{bmatrix}
3 & 0 & 1 & 2\\
0 & 1 & -2 & -4\\
0 & 1 & -2 & -4\\
0 & 0 & -2 & -4\\
\end{bmatrix}
discard $V_3$

27. Yes, dimension=2, {[-2, 0, 1], [0, 2, 1]}

28. k=0, Yes, dimension=2,  {[1, 0, 0], [0, 1, -3]}
if k!=0, No. 2*V is not in the set.

29. No.

30. n = 2, dimension = 1, {0}.
$n\gt 2$. dimension = 2, {[0, 0 ... 1, 0], [0, 0 ... 0, 1]}

31. No. -1 * V not include in the set.

32. Yes, dimension=1, {[-5/4, 1, -23/4]}

33. Yes, dimension=1, {[1, 10/3, 3]}

34. No. 2 * V not in the set.

35. Yes, dimension=1, {[1, 1/2, 1/3, 1/4]}
