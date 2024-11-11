# Proyecto de Texto a Voz

## Descripción
Este proyecto convierte un artículo de una URL proporcionada en un archivo de audio reproducible en formato MP3. Utiliza bibliotecas de Python como `newspaper3k`, `gtts` (Google Text-to-Speech) y `pygame` para realizar la conversión de texto a voz.

## Funcionalidades
- Extraer texto de artículos a partir de una URL.
- Convertir el texto extraído en un archivo de audio MP3.
- Reproducir automáticamente el archivo de audio una vez generado.

## Requisitos
Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- `newspaper3k`
- `gtts`
- `pygame`

Puedes instalar estas bibliotecas utilizando `pip`:

```bash
pip install newspaper3k gtts pygame
```

## Actualizaciones pendientes:
* Crearle una interfax gráfica de usuario
* Que no pase solo a voz una url que pase también un texto dado
* Que lea también en inglés

## Contribuir
Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, no dudes en crear un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Autor

- **Rosmén Valencia** - [PerfilGitHub](https://github.com/RosmenPro)


---

# Fast Typing Test

This desktop application allows users to take fast typing tests with a series of predefined sentences. It measures the time it takes for the user to type the displayed sentence and evaluates accuracy by comparing the typed sentence with the original.

## Features

- Random selection of test phrases.
- Measurement of the time it takes for the user to type a phrase.
- Evaluation of typing accuracy by comparing the user-typed phrase with the original.
- Simple graphical user interface using `Tkinter`.

## Requirements

To run this project, you need to have installed:

- Python 3.x
- Tkinter (usually included in standard Python installations)

## Installation

1. Clone this repository or download the files.
2. Make sure you have `Tkinter` installed. If not, you can install it by running:

   ```bash
   sudo apt-get install python3-tk  # On Debian/Ubuntu-based systems
   ```

## Usage

Run the script:

```bash
python3 typing_test.py
```

A window will appear with the following options:

- **Start**: Displays a random sentence for the user to type and begins timing.
- **Stop**: Ends the test when the user has finished typing and shows the elapsed time along with typing accuracy.

The user must type the phrase in the input field and then stop the test to see the results.

## Code Structure

- **TypingTest**: The main class that handles the application logic.
- **start_test**: Selects a random phrase and records the start time.
- **stop_test**: Calculates the total time taken to type the phrase and the typing accuracy.
- **evaluate_accuracy**: Compares the user-typed phrase with the original and calculates how many words match.

## Contributing

Contributions are welcome. If you have any suggestions or improvements, feel free to create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- **Rosmén Valencia** - [GitHubProfile](https://github.com/RosmenPro)




