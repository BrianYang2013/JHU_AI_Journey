## P318 - Problem set 7.9
1. {[1, 0]， [0, 1]}, {[2, 0]， [0, 1]}, {[2, 0]， [1, 1]}

2. $a_{(1)}, ..., a_{(n)}$ are linearly indepdent.
If $v=c_1a_{(1)}+...+c_na_{(n)} = d_1a_{(1)}+...+d_na_{(n)}$
$(c_1-d_1)a_{(1)}+...+(c_n-d_n)a_{(n)}=0$
per page 311 (1), impliess $(c_1-d_1)=0, ... (c_n-d_n)=0.$

3. The solution to the 2 equations is: [t, 11t, -7t]. so it is a vector space, the dimention is 1 and basis is $[t, 11t, -7t]^T, t \ne 0$

4. All skew-symmetric can present as $\begin{bmatrix}
0 & a & b\\
-a & 0 & c\\
-b & -c & 0
\end{bmatrix}$ , so dimentino is 3 and a basis could be $\begin{bmatrix}
0 & a & 0\\
-a & 0 & 0\\
0 & 0 & 0
\end{bmatrix}$$\begin{bmatrix}
0 & 0 & b\\
0 & 0 & 0\\
-b & 0 & 0
\end{bmatrix}$$\begin{bmatrix}
0 & 0 & 0\\
0 & 0 & c\\
0 & -c & 0
\end{bmatrix}$, $(a, b, c \ne 0)$

5. No. -1*v not in the set.

6. If we consider the function as the object in the vector space, then it is dimention 2, ${\cos (2x), \sin (2x)}$ is a set of basis.

If we evalute each function's vector space, then
if $a=b=0$, it is a {0}, with dimention 0 (I would assume)
if one of a b equals 0, assume a=0, then it is a vector space. dimension =1 and basis is $\sin (2x)$
if none of a b is 0, then $|y(x)| < |a|+|b|$, so it has upper and lower limit. Not a vector space.

7. dimension = 2, $\{xe^{-x}, x\}$

8. No.
$\begin{bmatrix}
1 & 0 \\
1 & 0\\
\end{bmatrix}+\begin{bmatrix}
0 & 0 \\
1 & 1\\
\end{bmatrix}=\begin{bmatrix}
1 & 0 \\
2 & 1\\
\end{bmatrix}$, which has determinant 1

9. Yes. $\begin{bmatrix}
a & b \\
c & -a\\
\end{bmatrix}$, so dimention=3, $\{\begin{bmatrix}
a & 0 \\
0 & -a\\
\end{bmatrix}, \begin{bmatrix}
0 & b \\
0 & 0\\
\end{bmatrix}, \begin{bmatrix}
0 & 0 \\
c & 0\\
\end{bmatrix}\}$, $(a, b, c \ne 0)$

10. $\textcolor{red}{Mark：}$ The first column is a 3x1 vector, can not multiply with a 3x1 vector.
If it means the objects in the first column multiple the 3, 0, -5 separately, then it means a matrix as
$\begin{bmatrix}
a & b \\
0 & c\\
d & e\\
\end{bmatrix}$, and a, b, c, d, e $\in R$. it is a vector space. with a set of basis
$\begin{bmatrix}
a & 0 \\
0 & 0\\
0 & 0\\
\end{bmatrix}, \begin{bmatrix}
0 & b \\
0 & 0\\
0 & 0\\
\end{bmatrix}, \begin{bmatrix}
0 & 0 \\
0 & c\\
0 & 0\\
\end{bmatrix}, \begin{bmatrix}
0 & 0 \\
0 & 0\\
d & 0\\
\end{bmatrix}, \begin{bmatrix}
0 & 0 \\
0 & 0\\
0 & e\\
\end{bmatrix}$, and a, b, c, d, e $\ne 0$

11. $\begin{bmatrix}
0.5 & -0.5 & 1 & 0\\
1.5 & -2.5 & 0 & 1\\
\end{bmatrix} = \begin{bmatrix}
1 & -1 & 2 & 0\\
0 & 1 & 3 & -1\\
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 5 & -1\\
0 & 1 & 3 & -1\\
\end{bmatrix} $
