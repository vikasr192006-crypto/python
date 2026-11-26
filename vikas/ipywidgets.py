import ipywidgets as widgets
from IPython.display import display

# Sample notes
sample_notes = "Enter your notes here..."

# Notes text area
notes_box = widgets.Textarea(
    value=sample_notes,
    placeholder="Enter your notes here...",
    description="Notes:",
    layout=widgets.Layout(
        width='95%',
        height='170px'
    ),
    style={
        "description_width": "initial"
    }
)

# Mode selection buttons
mode_box = widgets.ToggleButtons(
    options=[
        ("offline", "offline"),
        ("GEMINI FLASH 3.8", "LIVE")
    ],
    value="offline",
    description="Mode:",
    style={
        "description_width": "initial"
    }
)

# Display widgets
display(notes_box, mode_box) 