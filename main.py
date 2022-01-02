# Die Fibonacci-Folge ist die unendliche Folge natürlicher Zahlen, die (ursprünglich) mit zweimal der Zahl 1 beginnt
# oder (häufig, in moderner Schreibweise) zusätzlich mit einer führenden Zahl 0 versehen ist.
# Im Anschluss ergibt jeweils die Summe zweier aufeinanderfolgender Zahlen die unmittelbar danach folgende Zahl:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 -> Hier fangen wir mit der 0 an zu zählen.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 -> Hier fangen wir mit der 1 an zu zählen.

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)  # Hier ruft sich die Funktion selbst auf (Rekursion), bis die Bedingung erfüllt ist.
