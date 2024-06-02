# ObjetivosApp

ObjetivosApp is a simple and intuitive desktop application built using Python's Tkinter library. The application allows users to input, manage, and track their daily objectives through an interactive graphical user interface.

## Features

- **Add Objectives:** Easily add daily objectives through a text input dialog.
- **Track Progress:** Use checkboxes to mark objectives as complete.
- **Always on Top:** The application window remains on top of other windows for quick access.
- **Persistent:** Prompts the user to complete all tasks before exiting.
- **Mark/Unmark All:** Quickly mark or unmark all objectives with a single click.

## Prerequisites

- Python 3.x (Make sure Python is installed and added to your system PATH)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Installation

1. **Download and Install Python:**

    Download and install Python from the official website: [Python.org](https://www.python.org/downloads/)

    Ensure you check the option to add Python to your system PATH during installation.

2. **Download the Code:**

    Download the project as a ZIP file from the GitHub repository:

    ```url
    https://github.com/yourusername/ObjetivosApp/archive/refs/heads/main.zip
    ```

    Extract the ZIP file to a directory of your choice.

3. **Install the Dependencies:**

    Open Command Prompt and navigate to the extracted directory.

    ```bash
    cd path\to\extracted\directory
    ```

    Install the required dependencies:

    ```bash
    pip install tk
    ```

### Running the Application

1. **Run the Application:**

    After installing Python and extracting the code, run the application by executing the `DayPlan+.bat` file.

    Double-click on the `DayPlan+.bat` file or run it from the Command Prompt:

    ```bash
    DayPlan+.bat
    ```

    This will start the application, presenting a dialog to input your daily objectives.

## Usage

1. **Input Objectives:**
   - Enter each objective in the text box and press "Adicionar" or hit Enter.
   - Once all objectives are entered, press "Concluir" or hit Ctrl + Enter.

2. **Track Objectives:**
   - Check off each objective as you complete it.
   - Use the "Marcar Todos" button to mark all objectives as complete.
   - Use the "Desmarcar Todas" button to unmark all objectives.

3. **Exit:**
   - Attempting to close the window will prompt you to complete all objectives before exiting.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository (`https://github.com/Mateus-Lacerda/daily_planner_python/fork`)
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
