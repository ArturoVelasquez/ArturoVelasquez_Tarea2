evolucion.gif:empty.png
	rm empty.png
	convert -delay 50 -loop 0 $(ls tiempo_*.png | sort -V) evolucion.gif
empty.png:densidad_sedov.txt
	numpy sedov.py
densidad_sedov.txt:sedov.out
	./sedov.out > densidad_sedov.txt
sedov.out:Sedov.c
	cc Sedov.c -lm
clen:
	rm *out *txt
