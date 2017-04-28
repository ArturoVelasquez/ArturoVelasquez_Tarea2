all: exec shock sedov plotshock plotsedov GIF clean

GIF:
	convert -delay 50 -loop 0 $(ls *.png | sort -V) evolucion.gif

plotshock:datos.txt
	python shock.py

plotsedov:Density_sedov.data
	python sedov.py

shock [datos.txt]:shock.out
	./shock.out > datos.txt

sedov:sedov.out
	./sedov.out

exec:Sedov.c shock.c
	cc Sedov.c -lm -o sedov.out
	cc shock.c -lm -o shock.out

clean:
	rm *out *txt *png
