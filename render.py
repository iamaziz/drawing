import tkinter as tk
from typing import List, Union
from schema import Drawing, Box, Ellipse, Arrow, UnknownText, Style


def render_drawing(canvas: tk.Canvas, drawing: Drawing) -> None:
    for item in drawing.items:
        if isinstance(item, Box):
            render_box(canvas, item)
        elif isinstance(item, Ellipse):
            render_ellipse(canvas, item)
        elif isinstance(item, Arrow):
            render_arrow(canvas, item)
        elif isinstance(item, UnknownText):
            render_unknown_text(canvas, item)


def render_box(canvas: tk.Canvas, box: Box) -> None:
    x1, y1 = box.x, box.y
    x2, y2 = box.x + box.width, box.y + box.height
    options = {
        "outline": box.style.line_color
        if box.style and box.style.line_color
        else "black",
        "width": box.style.line_thickness
        if box.style and box.style.line_thickness
        else 1,
        "dash": (4, 4) if box.style and box.style.line_style == "dashed" else None,
    }
    canvas.create_rectangle(x1, y1, x2, y2, **options)
    if box.text:
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=box.text, fill="black")


def render_ellipse(canvas: tk.Canvas, ellipse: Ellipse) -> None:
    x1, y1 = ellipse.x, ellipse.y
    x2, y2 = ellipse.x + ellipse.width, ellipse.y + ellipse.height
    options = {
        "outline": ellipse.style.line_color
        if ellipse.style and ellipse.style.line_color
        else "black",
        "width": ellipse.style.line_thickness
        if ellipse.style and ellipse.style.line_thickness
        else 1,
    }
    canvas.create_oval(x1, y1, x2, y2, **options)
    if ellipse.text:
        canvas.create_text(
            (x1 + x2) / 2, (y1 + y2) / 2, text=ellipse.text, fill="black"
        )


def render_arrow(canvas: tk.Canvas, arrow: Arrow) -> None:
    options = {
        "arrow": tk.LAST,
        "fill": arrow.style.line_color
        if arrow.style and arrow.style.line_color
        else "black",
        "width": arrow.style.line_thickness
        if arrow.style and arrow.style.line_thickness
        else 1,
    }
    canvas.create_line(
        arrow.start_x, arrow.start_y, arrow.end_x, arrow.end_y, **options
    )


def render_unknown_text(canvas: tk.Canvas, unknown_text: UnknownText) -> None:
    canvas.create_text(100, 500, text=unknown_text.text, fill="red")


def draw(drawing: Drawing) -> None:
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Drawing")
    window.configure(bg="white")  # Set the background color of the window

    # Create a canvas widget
    canvas = tk.Canvas(window, width=800, height=600, bg="white", highlightthickness=0)
    canvas.pack(padx=10, pady=10)  # Adds 10 pixels of padding on all sides

    # Render the drawing on the canvas
    render_drawing(canvas, drawing)

    # Start the Tkinter event loop
    window.mainloop()


def main() -> None:
    # Example drawing data with a default head_size for Arrow
    drawing = Drawing(
        items=[
            Box(x=50, y=50, width=100, height=100, text="Box", style=None),
            Ellipse(x=200, y=50, width=100, height=50, text="Ellipse", style=None),
            Arrow(
                start_x=50, start_y=200, end_x=150, end_y=250, style=None, head_size=10
            ),
            UnknownText(text="This is some unknown text"),
        ]
    )

    draw(drawing)


if __name__ == "__main__":
    main()
