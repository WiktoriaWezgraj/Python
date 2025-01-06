'''In ski jumping competitions, each competitor is assessed by five judges. Each judge can award a score from 0 to 20 points. 
The highest and lowest scores are discarded. The remaining three scores are added up to form the final score obtained by the competitor. 
The ratings of four players are presented below.

[(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
Calculate and display the total points obtained by competitors.

Tip: use the Python built-in functions: map(), sum(), min(), max().

Sample result:

[48, 54, 52, 51]'''

scores = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

total_points = list(map(lambda s: sum(s) - min(s) - max(s), scores))
print(total_points)
