# Treveis Stein, Saks, Papir

Alice, Bob og Charlie spiller treveis [stein, saks, papir](https://no.wikipedia.org/wiki/Stein,_saks,_papir). De loggfører alle kast med en bokstav (S for saks, R for stein, P for papir) i en rekke, der rekkefølgen på kastene er alfabetisk etter navnet på spilleren. Blir det uavgjort mellom alle tre spillerene får ingen poeng. Slår to spillere likt mot en annen spiller blir det omkamp mellom disse to spillerene.

## Eksempel

* `SPR` - Alice spiller saks, Bob spiller papir, Charlie spiller stein. Dette blir uavgjort og ingen får poeng.
* `PPP` - Alle spiller papir, dette blir uavgjort og ingen får poeng.
* `SPPRRP` - Alice spiller Saks, resten spiller papir, Alice får poeng. I neste runde spiller Charlie papir, og resten spiller stein. Charlie får poeng.
* `PSSRS` - Både Bob og Charlie spiller saks, som slår Alice som spiller papir. Omkamp mellom Bob og Charlie, der Bob spiller stein og vinner mot Charlie som spiller saks. Bob får poeng.
* `SPSRRRP` - Alice og Charlie slår Bob med saks, omkamp mellom dem der det blir uavgjort med stein mot stein, ny omkamp der Charlie slår Alice med papir mot stein og får poeng.
* `SSSSSRRPPSSSRPRPPSPPSSSSRPRRPRRPPRPPRRPPRPR` -
  * Uavgjort med tre sakser.
  * Charlie vinner med stein mot to sakser.
  * Uavgjort mellom Bob og Charlie, omkamp med saks mot saks. Ny omkamp der Charlie vinner med stein mot Bob.
  * Uavgjort mellom Alice og Charlie, begge med papir. Omkamp der Charlie vinner med saks.
  * Charlie vinner med saks mot to papir.
  * Uavgjort med tre sakser.
  * Bob vinner med papir mot to stein.
  * Bob vinner *igjen* med papir mot to stein.
  * Uavgjort mellom Bob og Charlie. Omkamp der Charlie vinner.
  * Alice vinner med papir mot dobbel stein.
  * Alice og Bob spiller uavgjort, omkamp der Alice vinner med papir.

## Oppgave

Gitt [denne loggfilen](https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-rpslog.txt), hvor mange poeng får hver av spillerene? Svaret skal gis med tre kommaseparerte tall, i rekkefølgen til navnene på spillerene (Alice, Bob, Charlie). For det siste eksempelet over ville svaret da blitt `2,2,5`.