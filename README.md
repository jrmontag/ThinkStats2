ThinkStats2
===========

Text and supporting code for Think Stats, 2nd Edition

----


# JM notes 

## Chapter 1

*Exercise 1-1*

In ``.ipynb``, but without ``--pylab``; update the notebook code to more recent practices while working through it. 

*Exercise 1-2*

Using Python 2.7.9. Compare with [NSFG codebook](http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835).

    $ python chap01ex.py 
    'pregnum' value counts from data:
    0     2610
    1     1267
    2     1432
    3     1110
    4      611
    5      305
    6      150
    7       80
    8       40
    9       21
    10       9
    11       3
    12       2
    14       2
    19       1 


## Chapter 2

- using ``ch02-scratch.ipynb`` to execute the code in the text

 
*Exercise 2-1*

> Suppose you were asked to summarize what you learned about whether first babies arrive late. Which summary statistics would you use if you wanted to get a story on the evening news?

Given that the audience of the news is broad and generally looks for succinct sound bites, I'd stick to simple, colloquial statistics like the mean. The punchline would be approximately "the difference in mean pregnancy length for first and other babies is negligible." 

> Which ones would you use if you wanted to reassure an anxious patient?

Probably the same mean comparison, but I'd also add the additional context of the relative percentage difference, and - depending on their inclanation - also talk about/show the distribution. An individual patient seems more likely to care about the subtlety of these values. 

> Finally, ... Cecil Adams... clearly, precisely, honestly.

I'd say this is largely as presented in the text: "For all live births, the mean pregnancy length is 38.6 weeks, the standard deviation is 2.7 weeks, which means we should expect deviations of 2-3 weeks to be common. ... In this example, the difference in means is 0.029 standard deviations, which is small. To put that in perspective, the difference in height between men and women is about 1.7 standard deviations (see Wikipedia)."


*Exercise 2-2*

- use ``chap02ex.ipynb``


*Exercise 2-3*

- use ``chap02ex.py`` 


*Exercise 2-4*

- return to ``chap02ex.ipynb``  


## Chapter 3

*Exercise 3-1, 3-2, 3-3, 3-4*

- use ``chap03ex.ipynb``


## Chapter 4








## TODO

### chapter 1

- page 10, ``preg_map[]`` isn't defined. needs: ``>>> preg_map = nsfg.MakePregMap(df)``



 
