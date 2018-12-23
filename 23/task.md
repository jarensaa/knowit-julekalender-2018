# Fødselsnummervalidering

Fødselsnummer inneholder en del informasjon:

- De består av elleve siffer.
- De første seks sifferene er fødselsdato, på format DDMMÅÅ.
- De tre neste sifferene utgjør individnummeret.
- Det siste sifferet i individnummeret indikerer kjønn, med partall for kvinner og oddetall for menn.
- De to siste sifferene i fødselsnummeret er kontrollsiffer og beregnes på bakgrunn av de første ni sifferene. Kontrollsifferene skal blant annet beskytte mot å behandle feil person ved en enkelt skrivefeil. Kontrollsiffer regnes ut på følgende måte:
  - De ni første sifferene (fødselsdato og individnummer) ganges med korresponderende siffer i rekken `3,7,6,1,8,9,4,5,2`, og disse produktene summeres sammen. Om denne summen modulo elleve blir null er første kontrollsiffer null. Om det ikke blir null er første kontrollsiffer 11 minus summen av produktene.
  - For det andre kontrollsifferet gjenntas prosessen med de ni første sifferene _samt det første kontrollsifferet_ med rekken `5,4,3,2,7,6,5,4,3,2`.
  - Om resultatet av modulo-operasjonen er 1 blir kontrollsifferet 10. Dette er ugyldig, og dette individnummeret kan da ikke brukes for denne datoen.

## Eksempel

Ole ble født 7. oktober 1991 og fikk tildelt individnr `411`. Siste siffer er et oddetall, som indikerer at Ole er en mann. De ni første sifferene i fødselsnummeret hans er `071091411`. Det første kontrollsifferet finner vi slik:

| Fødselsnr | 0   | 7   | 1   | 0   | 9   | 1   | 4   | 1   | 1   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rekke     | 3   | 7   | 6   | 1   | 8   | 9   | 4   | 5   | 2   |
| Produkt   | 0   | 49  | 6   | 0   | 72  | 9   | 16  | 5   | 2   |

- Produktene summert blir da 159. 159 mod 11 = 5. Kontrollsiffer blir da 11 - 5 = 6.

For det andre kontrollsifferet gjenntar vi prosessen, _inkludert kontrollsifferet vi alt har funnet_.

| Fødselsnr | 0   | 7   | 1   | 0   | 9   | 1   | 4   | 1   | 1   | 6   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rekke     | 5   | 4   | 3   | 2   | 7   | 6   | 5   | 4   | 3   | 2   |
| Produkt   | 0   | 28  | 3   | 0   | 63  | 6   | 20  | 4   | 3   | 12  |

Produktene summert = 139. 139 mod 11 = 7. 11-7 = 4. Siste kontrollsiffer er altså 4.

## Oppgave

Hvor mange av fødselsnummerene i [denne filen](https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-fnr.txt) er gyldige fødselsnummer (med gyldige kontrollsiffer og fødselsdato) og tilhører kvinner født i august?
