import numpy as np
import matplotlib.pyplot as plt

def main():
    datos = []
    print("Ingresa los datos numéricos uno por uno. Escribe 'Start' para iniciar el cálculo.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "start":
            if len(datos) < 2:
                print("Se necesitan al menos 2 datos para calcular la desviación estándar.")
                continue
            break

        try:
            valor = float(entrada)
            datos.append(valor)
        except ValueError:
            print("Entrada no válida. Ingresa un número o 'Start'.")

    # Cálculos
    media = np.mean(datos)
    desviacion = np.std(datos)

    print("\n Resultados:")
    print(f"Media aritmética: {media:.4f}")
    print(f"Desviación estándar: {desviacion:.4f}")

    # Graficar la campana de Gauss
    x = np.linspace(min(datos) - 3*desviacion, max(datos) + 3*desviacion, 500)
    y = (1 / (desviacion * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desviacion) ** 2)

    plt.plot(x, y, label='Campana de Gauss')
    plt.axvline(media, color='red', linestyle='--', label=f"Media: {media:.2f}")
    plt.title("Distribución Normal")
    plt.xlabel("Valores")
    plt.ylabel("Densidad de probabilidad")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()