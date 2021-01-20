bits = 16
amostras = 5000
bits_por_segundo = bits * amostras
bits_por_minuto = bits_por_segundo * 60
bits_por_hora = bits_por_minuto * 60
storage = bits_por_hora / 8000000

print(f"Seu arquivo terá {storage} MB")