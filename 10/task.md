# Snø++

I sommer var det rolige tider på nordpolen, så nissens alver benyttet tiden til å lage et nytt programmeringsspråk, snø++. Snø++ er et begrenset og snålt programmeringsspråk som fungerer som følger:

- Koden må skrives i kode som visuelt ligner på snø.
- Koden parses tegn for tegn, fra venstre mot høgre, linje for linje nedover (slik man er vant til).
- Programmet starter med en tom stack, og for hvert mellomrom, så legges verdien 31 på stacken.

Utover dette så har man tilgang til følgende kommandoer:

- `:` Fjern alle verdier på stacken, summer disse, og legg resultatet på stacken.
- `|` Legg verdien 3 på stacken.
- `'` Fjern to verdier fra stacken, summer dem, legg resultatet på stacken.
- `.` Fjern en verdi A, fra stacken. Fjern en verdi B, fra stacken. Legg resultatet av A-B på stacken. Legg B-A på stacken.
- `_` Fjern en verdi A, fra stacken. Fjern en verdi B, fra stacken. Legg resultatet av A\*B på stacken. Legg A på stacken.
- `/` Fjern en verdi fra stacken.
- `i` Legg til en kopi av den siste verdien på stacken.
- `\` Inkrementer den siste verdien på stacken med 1.
- `*` Fjern en verdi A, fra stacken. Fjern en verdi B, fra stacken. Beregn A/B, rund av til heltall i retning mot 0, og legg resultatet på stacken.
- `]` Fjern en verdi fra stacken. Dersom den fjernede verdien var et partall, legg verdien 1 på stacken.
- `[` Fjern en verdi fra stacken. Dersom den fjernede verdien var et oddetall, legg verdien tilbake på stacken.
- `~` Fjern tre verdier fra stacken. Legg tilbake den største av disse.
- `K` Brukes til kommentarer i koden og betyr at resten av linjen er kommentert ut.

Hva er det største tallet som ligger på stacken etter at koden i inputfilen har blitt kjørt i snø++?

Inputfilen finner man [her](https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input.spp).
