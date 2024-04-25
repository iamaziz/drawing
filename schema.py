from typing_extensions import Literal, Annotated, Doc, NotRequired, Optional

from pydantic import BaseModel


class Style(BaseModel):
    corners: Annotated[
        Optional[Literal["rounded", "sharp"]],
        Doc("Corner style of the drawing elements."),
    ]
    line_thickness: Annotated[Optional[int], Doc("Thickness of the lines.")]
    line_color: Annotated[Optional[str], Doc("CSS-style color code for line color.")]
    fill_color: Annotated[Optional[str], Doc("CSS-style color code for fill color.")]
    line_style: Annotated[
        Optional[str], Doc("Style of the line: 'solid', 'dashed', 'dotted'.")
    ]


class Box(BaseModel):
    """A rectangular box defined by a coordinate system with the origin at the top left."""

    x: Annotated[int, Doc("X-coordinate of the top left corner.")]
    y: Annotated[int, Doc("Y-coordinate of the top left corner.")]
    width: Annotated[int, Doc("Width of the box.")]
    height: Annotated[int, Doc("Height of the box.")]
    text: Annotated[Optional[str], Doc("Optional text centered in the box.")]
    style: Annotated[Optional[Style], Doc("Optional style settings for the box.")]


class Ellipse(BaseModel):
    """An ellipse defined by its bounding box dimensions."""

    x: Annotated[int, Doc("X-coordinate of the top left corner of the bounding box.")]
    y: Annotated[int, Doc("Y-coordinate of the top left corner of the bounding box.")]
    width: Annotated[int, Doc("Width of the bounding box.")]
    height: Annotated[int, Doc("Height of the bounding box.")]
    text: Annotated[Optional[str], Doc("Optional text centered in the box.")]
    style: Annotated[Optional[Style], Doc("Optional style settings for the ellipse.")]


class Arrow(BaseModel):
    """A line with a directional arrow at one or both ends, defined by start and end points."""

    start_x: Annotated[int, Doc("Starting X-coordinate.")]
    start_y: Annotated[int, Doc("Starting Y-coordinate.")]
    end_x: Annotated[int, Doc("Ending X-coordinate.")]
    end_y: Annotated[int, Doc("Ending Y-coordinate.")]
    style: Annotated[Optional[Style], Doc("Optional style settings for the arrow.")]
    head_size: Annotated[Optional[int], Doc("Size of the arrowhead, if present.")]


class UnknownText(BaseModel):
    """Used for input that does not match any other specified type."""

    text: Annotated[str, Doc("The text that wasn't understood.")]


class Drawing(BaseModel):
    """A collection of graphical elements including boxes, ellipses, arrows, and unrecognized text."""

    items: Annotated[
        list[Box | Arrow | Ellipse | UnknownText], Doc("List of drawable elements.")
    ]
