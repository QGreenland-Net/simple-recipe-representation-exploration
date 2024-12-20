# Apache Beam Simple OGDC Recipe Exploration

This repository has been archived.

This repo was an exploration of using Apache Beam to create a simple OGDC
recipe. The QGreenland-Net team is no longer considering the use of Apache Beam,
and instead is pursuing the use of Argo Workflows. See the
[ogdc-runner](https://github.com/QGreenland-Net/ogdc-runner/) for the latest
developments.

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
