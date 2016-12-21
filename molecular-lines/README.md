```
copy-molecules.py                   Rudimentary script used to create files *.newtitulo
smart-merge-old-new.py              Project of script to merge some molecules in 'mghc2cnr_cn3ch13chtiog3tio.dat'
                                    with others in 'moleculagrade-paula.dat.newtitulo' in order to make the most
                                    complete list possible
mghc2cnr_cn3ch13chtiog3tio.dat      Older molecular lines file with 12 molecules only, 
                                    however wavelengths are more precise with 3 decimal places, whereas
                                    files moleculagrade* have wavelengths truncated to 2 decimal places
moleculagrade-marina.dat            file 'moleculagrade.dat' supplied to JT by Marina Trevisan around Mar/2015
moleculagrade-marina.dat.newtitulo  Same contents as before, plus molecule header line ('titulo') updated to
                                    have structure "<description> # <symbols> # <transitions>"
                                    **some wavelengths are wrong**
moleculagrade-paula.dat             file 'moleculagrade.dat' taken from pfant04 source code
moleculagrade-paula.dat.newtitulo   Same contents as before, plus molecule header line ('titulo') updated to
                                    have structure "<description> # <symbols> # <transitions>"
                                    **some wavelengths are wrong**
molecules-no-branches.dat           Same contents as moleculagrade-marina.dat,
                                    but some wavelengths with obvious typos were fixed, 
                                    but **missing branches information** (JT's fault)
```
