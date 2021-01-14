# autoreporter

Autoreporter generates beautiful reports laid out using a customizable PowerPoint template. It interfaces with matplotlib for producing figures, and it does text variable substitution as well.

## Installation

## Example

Autoreporter fills in the template  
<img src="assets/template.jpg" width="480">  
to create the report  
<img src="assets/report.jpg" width="480">.

To create this, this function is called:

```python
from autoreporter import builder

builder.builder("report.pptx", "test.pptx", fig_dict, var_dict = {"a":"123"})
```

PowerPoint shapes with text of form "!(key)" is replaced with the matplotlib figure, `fig_dict[key]`.  

Text of the form "$[key]" is replaced with a variable, `var_dict[key]`.

Any other shape, image or text is kept the same.