from pathlib import Path
import yaml

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("template.py.j2")

recipe_config_file = Path("meta.yaml")
commands_file = Path("test_commands.sh")

input_subkeys = {
    "url": "beam.io.SomeTransformThatCanReadAFileFromAUrl",
    "dataone_doi": "our_custom_transforms.DataOneDoiInput",
}



def get_commands() -> list[str]:
    # read_lines is going to be more efficient I assume...
    lines = commands_file.read_text().split("\n")

    # Omit comments and empty lines
    commands = [line for line in lines if line and not line.startswith("#")]
    return commands


def get_recipe_config() -> dict:
    with open(recipe_config_file, mode="r") as config_file:
        return yaml.safe_load(config_file)


def get_input_constructor_and_arg(config: dict) -> tuple[type, any]:
    acceptable_values = f"Acceptable values: {input_subkeys.keys()}"
    if num_keys := len(config["input"].keys()) > 1:
        raise RuntimeError(
            f"Expected 1 sub-key for the `input` key; got {num_keys}."
            f" {acceptable_values}"
        )

    key, val = list(config["input"].items())[0]

    try:
        clss = input_subkeys[key]
    except KeyError as e:
        raise RuntimeError(
            f"Received unexecpected sub-key for `input` key: {key}"
            f" {acceptable_values}"
        )

    return clss, val



if __name__ == "__main__":
    commands = get_commands()
    config = get_recipe_config()

    input_constructor, input_constructor_arg = get_input_constructor_and_arg(config)

    print(template.render(
        commands=commands,
        input_constructor=input_constructor,
        input_constructor_arg=input_constructor_arg,
    ))
