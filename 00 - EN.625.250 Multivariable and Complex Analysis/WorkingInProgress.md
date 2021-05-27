## P300 - Problem set 7.7
Theorems 1-a: we change from right hand to the left hand, so we get -1?

1. Theorems 1-a) $\begin{vmatrix}
1 & 0\\
0 & 1\\
\end{vmatrix} = 1-0=1$
$\begin{vmatrix}
0 & 1\\
1 & 0\\
\end{vmatrix} = 0-1=-1$

Theorems 1-b) $\begin{vmatrix}
1 & 0\\
c & 1\\
\end{vmatrix} = 1-0=1$

Theorems 1-c) $\begin{vmatrix}
1 & 0\\
0 & c\\
\end{vmatrix} = c-0=c$

Theorems 2-a) $\begin{vmatrix}
0 & 1\\
1 & 0\\
\end{vmatrix} = 0-1=-1$

Theorems 2-b)$\begin{vmatrix}
1 & c\\
0 & 1\\
\end{vmatrix} = 1-0=1$

Theorems 2-c)$\begin{vmatrix}
1 & 0\\
0 & c\\
\end{vmatrix} = c-0=c$

Theorems 2-d) In this example, $A=A^T=1$

Theorems 2-e) $\begin{vmatrix}
1 & 0\\
0 & 0\\
\end{vmatrix} = 0-0=0$

Theorems 2-f) $\begin{vmatrix}
1 & 2\\
a & 2a\\
\end{vmatrix} = 2a-2a=0$

2. $\begin{vmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}\\
\end{vmatrix}$
$= a_{11}|a_{22}|-a_{12}|a_{21}| = a_{11}a_{22}-a_{12}a_{21}$
$= a_{11}|a_{22}|-a_{21}|a_{12}| = a_{11}a_{22}-a_{12}a_{21}$
$= a_{22}|a_{11}|-a_{12}|a_{21}| = a_{11}a_{22}-a_{12}a_{21}$
$= a_{22}|a_{11}|-a_{21}|a_{12}| = a_{11}a_{22}-a_{12}a_{21}$

3. My guess is Example 2 but not Theoream 2?

4. Not sure why we want to expand the high order determinant. Gauss elimination obviously a better option. It takes $n^3$ (I heard it can improve), which is way better than $n!$

5. $\begin{vmatrix}
1 & 0\\
0 & 1\\
\end{vmatrix} = 1-0=1, \begin{vmatrix}
k & 0\\
0 & k\\
\end{vmatrix} = k^2-0=k^2$

6. My guess is Example 2 but not Example 1?

7. $\cos\alpha \cos\beta - \sin\alpha \sin\beta = \cos(\alpha + \beta)$
8. -7.87
9. $\cos(n\theta) \cos(n\theta) + \sin(n\theta) \sin(n\theta) = \cos(n\theta - n\theta) = 1$
10. $\cosh t \cosh t - \sinh t \sinh t = \cosh(t-t) = \frac{1}{2}(e^0+e^{-0})=1$
11. 40
12. $a^3+b^3+c^3-3abc$
13. $0 \cdot (0+6+-6-0-0-0) - 4 \cdot (0+-15+2-0-0-4) + (-1) \cdot (0+0+-4--30-0--8) - 5\cdot (-12+0+6-45-0-0) = 0 - 4\cdot (-17) + (-1)\cdot (34) - 5 \cdot (-51) = 289$
14. Question: I feel we can do it in the below way, with certain condition. Can not remember what exactly it is, and it does not apply for 13. The result is same while I expand the 4th order determinants.
$\begin{vmatrix}
4 & 7\\
2 & 8\\
\end{vmatrix}\begin{vmatrix}
1 & 5\\
-2 & 2\\
\end{vmatrix} = (32-14)(2+10)=216$

P.S: it is called block matrices. for upper (lower) triangular block matrix, diagonal blocks $A_1, A_2.. A_n$, and we will get $det=det(A_1)det(A_2)..det(A_n)$.

15. $\begin{vmatrix}
1 & 2 & 0 & 0\\
2 & 4 & 2 & 0\\
0 & 2 & 9 & 2\\
0 & 0 & 2 & 16\\
\end{vmatrix} = \begin{vmatrix}
1 & 2 & 0 & 0\\
0 & 0 & 2 & 0\\
0 & 2 & 9 & 2\\
0 & 0 & 2 & 16\\
\end{vmatrix} = -\begin{vmatrix}
1 & 2 & 0 & 0\\
0 & 2 & 9 & 2\\
0 & 0 & 2 & 0\\
0 & 0 & 2 & 16\\
\end{vmatrix}= -\begin{vmatrix}
1 & 2 & 0 & 0\\
0 & 2 & 9 & 2\\
0 & 0 & 2 & 0\\
0 & 0 & 0 & 16\\
\end{vmatrix} = -64$

16. $\begin{vmatrix}
0 & 1\\
1 & 0\\
\end{vmatrix} = 0-1=-1$
$\begin{vmatrix}
0 & 1 & 1\\
1 & 0 & 1\\
1 & 1 & 0\\
\end{vmatrix} = 2$
$\begin{vmatrix}
0 & 1 & 1 & 1\\
1 & 0 & 1 & 1\\
1 & 1 & 0 & 1\\
1 & 1 & 1 & 0\\
\end{vmatrix} = -3$

So I would assume this special n order matrix have determinants $(-1)^{n-1}(n-1)$

Try to prove it by induction - Placeholder

Incidence Matrices ??

17. $\begin{vmatrix}
4 & 9\\
-8 & -6\\
\end{vmatrix} = -24+72 \ne 0$
$\begin{bmatrix}
4 & 9\\
0 & 12\\
0 & 24\\
\end{bmatrix}$, rank = 2

18. $\begin{vmatrix}
4 & 4 & 4\\
4 & 0 & 10\\
-6 & 10 & 0\\
\end{vmatrix}= 0+(-240)+(-240)-0-0-0 \gt 0$
$\begin{bmatrix}
4 & 4 & 4\\
4 & 0 & 10\\
-6 & 10 & 0\\
\end{bmatrix}=\begin{bmatrix}
4 & 4 & 4\\
0 & 4 & -6\\
0 & 16 & 6\\
\end{bmatrix}=\begin{bmatrix}
4 & 4 & 4\\
0 & 4 & -6\\
0 & 0 & 30\\
\end{bmatrix}$, rank=3

19. $\begin{vmatrix}
1 & 5 & 2\\
1 & 3 & 2\\
4 & 0 & 8\\
\end{vmatrix}= 24+40+0-24-40-0=0$
$\begin{vmatrix}
5 & 2 & 2\\
3 & 2 & 6\\
0 & 8 & 48\\
\end{vmatrix}= 480+0+48-0-48*5-48*6=0$
$\begin{vmatrix}
1 & 5 \\
1 & 3 \\
\end{vmatrix}= 3-5=-2\ne 0$
$\begin{bmatrix}
1 & 5 & 2 & 2\\
1 & 3 & 2 & 6\\
4 & 0 & 8 & 48\\
\end{bmatrix}=\begin{bmatrix}
1 & 5 & 2 & 2\\
0 & 2 & 0 & -4\\
0 & 20 & 0 & -40\\
\end{bmatrix}$, rank=2

20. b) $\begin{cases}
ax+by+cz+d*1=0\\
ax_1+by_1+cz_1+d*1=0\\
ax_2+by_2+cz_2+d*1=0\\
ax_3+by_3+cz_3+d*1=0\\
\end{cases}$

21. $D=\begin{vmatrix}
3 & -5 \\
6 & 16 \\
\end{vmatrix}= 78$
$x=\frac{1}{78}\begin{vmatrix}
15.5 & -5 \\
5 & 16 \\
\end{vmatrix}=3.5$
$y=\frac{1}{78}\begin{vmatrix}
3 & 15.5\\
6 & 5\\
\end{vmatrix}=-1$
$\begin{bmatrix}
3 & -5 & 15.5\\
6 & 16 & 5\\
\end{bmatrix}= \begin{bmatrix}
3 & -5 & 15.5\\
0 & 26 & -26\\
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 3.5\\
0 & 1 & -1\\
\end{bmatrix}$

22. $D=\begin{vmatrix}
2 & -4 \\
5 & 2 \\
\end{vmatrix}= 24$
$x=\frac{1}{24}\begin{vmatrix}
-24 & -4 \\
0 & 2 \\
\end{vmatrix}=-2$
$y=\frac{1}{24}\begin{vmatrix}
2 & -24\\
5 & 0\\
\end{vmatrix}=5$
$\begin{bmatrix}
2 & -4 & -24\\
5 & 2 & 0\\
\end{bmatrix}= \begin{bmatrix}
1 & -2 & -12\\
0 & 1 & 5\\
\end{bmatrix} = \begin{bmatrix}
1 & 0 & -2\\
0 & 1 & 5\\
\end{bmatrix}$

23. $D=\begin{vmatrix}
0 & 3 & -4 \\
2 & -5 & 7 \\
-1 & 0 & -9\\
\end{vmatrix}= 0-21+0-(-20)-0-(-54)= 53$
$x=\frac{1}{53}\begin{vmatrix}
16 & 3 & -4 \\
-27 & -5 & 7 \\
9 & 0 & -9\\
\end{vmatrix}=\frac{1}{53}(80*9+21*9+0-20*9-0-81*9)=0$
$y=\frac{1}{53}\begin{vmatrix}
0 & 16 & -4 \\
2 & -27 & 7 \\
-1 & 9 & -9\\
\end{vmatrix}= \frac{1}{53}(0-112-72+108-0+288)=212/53=4$
$z=\frac{1}{53}\begin{vmatrix}
0 & 3 & 16 \\
2 & -5 & -27 \\
-1 & 0 & 9\\
\end{vmatrix}= \frac{1}{53}(0-+81+0-80-0-54)=-1$
$\begin{bmatrix}
0 & 3 & -4 & 16\\
2 & -5 & 7 & -27\\
-1 & 0 & -9 & 9\\
\end{bmatrix}= \begin{bmatrix}
1 & 3 & 5 & 7\\
0 & 11 & 3 & 41\\
0 & 3 & -4 & 16\\
\end{bmatrix} = \begin{bmatrix}
1 & 3 & 5 & 7\\
0 & 2 & 15 & -7\\
0 & 0 & 53 & -53\\
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 4\\
0 & 0 & 1 & -1\\
\end{bmatrix}$

24.

25. 
