from pathlib import Path
import yaml

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("template.py.j2")

recipe_config_file = Path("meta.yaml")
commands_file = Path("test_commands.sh")



def get_commands() -> list[str]:
    # read_lines is going to be more efficient I assume...
    lines = commands_file.read_text().split("\n")

    # Omit comments and empty lines
    commands = [line for line in lines if line and not line.startswith("#")]
    return commands


def get_recipe_config() -> dict:
    with open(recipe_config_file, mode="r") as config_file:
        return yaml.safe_load(config_file)


if __name__ == "__main__":
    commands = get_commands()
    config = get_recipe_config()
    breakpoint()

    print(template.render(
        commands=commands,
        config=config,
    ))
