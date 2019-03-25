import PySimpleGUI as sg

def ask_desktop():
    """Asks user to specify Desktop folder and returns folder path as string"""
    # Layout for window used.
    lay_desktop_select = [[sg.Text('Please select your Desktop folder')],
                      [sg.InputText(), sg.FolderBrowse()],
                      [sg.Submit(), sg.Cancel()]]
    path = ''
    # Prompts user for desktop folder. If blank string entered, error is raised and try again.
    while True:
        window = sg.Window('ZipOR').Layout(lay_desktop_select)
        event, values = window.Read()
        window.Close()
        text_input = values[0]
        if text_input == '':
            sg.Popup('You did not enter a file path, please try again.')
        else:
            path = text_input
            break
    return path


def ask_depths():
    """Asks user how many depth breaks there will be and return that number as integer"""
    layout = [[sg.Text('How many depth breaks do you have? Maximum: 20')],
          [sg.InputCombo(list(range(1, 21)), size=(20, 3))],
          [sg.Submit(), sg.Cancel()]]
    window = sg.Window('ZipOR').Layout(layout)
    event, values = window.Read()
    window.Close()
    input = values[0]
    return int(input)


def gui_instructions():
    """Presents a GUI with instructions to the user."""
    layout = [[sg.Text('Instructions', size=(25, 1), font='bold')],
        [sg.Text(' - A file has been created on your desktop called "data.xlsx"')],
        [sg.Text(' - The file has one tab for EACH of your different depth breaks.')],
        [sg.Text(' - For each tab, copy all owners in the depth as you would when building a WI recap.')],
        [sg.Text(' - Do not edit the column headers of the file.')],
        [sg.Text(' - Then SAVE the file and exit.', size=(25, 3))],
        [sg.Text(' - Do this now.', size=(25, 3))],
        [sg.Text(' - If all your depths have been entered AND the file has been saved AND CLOSED.')],
        [sg.Text(' - Then Press OK')],
        [sg.Ok(size=(10, 1))]]
    window = sg.Window('ZipOR').Layout(layout)
    event, values = window.Read()
    window.Close()
    sg.Popup('REMINDER: Has the file been closed? If, not CLOSE the file now.')


def gui_complete():
    """Informs the user output has been completed and the program with quit."""
    layout = [[sg.Text('Output Completed', size=(25, 1), font='bold')],
          [sg.Text(' - The "data.xlsx" file has been appended with OUTPUT tabs for each break')],
          [sg.Text('Enjoy')],
          [sg.Ok(size=(10, 1))]]

    window = sg.Window('ZipOR').Layout(layout)
    event, values = window.Read()
    window.Close()



