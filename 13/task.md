# JULAMSEKVENS

Vi definerer en sekvens der hvert nummer i sekvensen er det minste mulige tallet som er den summen av to distinkte tall som har forekommet tidligere i sekvensen. De to første tallene i sekvensen må være definert.

En sekvens kan for eksempel begynne på (1, 2), der N<sub>1</sub> = 1, N<sub>2</sub> = 2. Da sier vi at for hver n > 2, defineres N<sub>n</sub> som det minste positive heltallet større enn N<sub>n-1</sub> som kan uttrykkes som summen av to distinkte tall som har forekommet tidligere i sekvensen. De ti første tallene i denne sekvensen er da:

1:  
2:  
3: (1+2)  
4: (1+3)  
6: (2+4)  
8: (2+6)  
11: (3+8)  
13: (11+2)  
16: (13+3)  
18: (16+2)

De følgende tallene er ikke med i denne sekvensen fordi de ikke er distinkte summer:

5: (2+3, 4+1)  
7: (4+3, 6+1)  
9: (8+1, 6+3)  
10: (2+8, 6+4)  
12: (8+4, 11+1)  
14: (11+3, 13+1)  
15: (13+2, 4+11)  
17: (11+6, 13+4)

Hva er summen av de hundre første primtallene i en slik sekvens som begynner med verdiene N<sub>1</sub>=1 og N<sub>2</sub>=3?
