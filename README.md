The point of this spike is to show an example of a very simple representation that works
for a very constrained use case. This makes some chunk of use cases much more
accessible, similar to what `repo2docker` does for managing Docker image builds.
Anything beyond the simplest string of shell commands should be a custom recipe.

The current program emits:

```python
recipe = (
  beam.io.SomeTransformThatCanReadAFileFromAUrl(https://example.com/something)
  | CommandPTransform("""gdalwarp -t_srs EPSG:3413 {input} {output}""")
  | CommandPTransform("""echo "Heya!"""")
)

```


## Thoughts

* The list of commands could be represented as a `PCollection` that is handled by a
  `PTransform` that generates "sub-`PTransforms`" (`.expand()` method on a
  `PTransform` class?)? Could that help us skip the step of generating a Python
  executable and instead pass that raw `PCollection` data to a static recipe.
