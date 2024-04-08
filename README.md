## Poetry Command Aliases Plugin

This plugin allows you to define aliases or shortcuts for commonly used commands in your Poetry projects. It simplifies command execution by providing custom aliases for complex or frequently used commands.

### Usage

1. **Installation**:

   Install the plugin using Poetry:

   ```bash
   pip install poetry-plugin-commands
   ```

   or

   ```bash
   pip install --user poetry-plugin-commands
   ```

   or at least

   ```bash
   poetry self add poetry-plugin-commands
   ```

2. **Define Aliases**:

   Add your aliases to the `pyproject.toml` file under the `[tool.poetry.plugins.commands]` section:

   ```toml
   [tool.poetry.plugins.commands]
   stree = "tree src"
   test_var = "echo $VAR"
   run_app = "PYTHONPATH=src:. poetry run python src/app_launch/main.py"
   ```

   Here, `stree`, `test_var`, and `run_app` are the custom aliases, and their corresponding commands are specified.

3. **Execute Commands**:

   Now you can use the defined aliases with Poetry:

   ```bash
   poetry stree
   ```

   ```bash
   poetry test_var
   ```

   ```bash
   poetry run_app
   ```

   These commands will execute the respective commands defined as aliases.

4. **List Available Commands**:

   To get a list of available aliases along with their corresponding commands, run:

   ```bash
   poetry user-commands
   ```

   This will display a list of aliases and their associated commands:

   ```plaintext
   stree -> `tree src`
   test_var -> `echo $VAR`
   run_app -> `PYTHONPATH=src:. poetry run python src/app_launch/main.py`
   ```

### Contributing

Feel free to contribute to this plugin by reporting issues, suggesting features, or submitting pull requests on [GitHub](https://github.com/BlackCatDevel0per/poetry-plugin-commands).

### License

This plugin is licensed under the Apache 2. License. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.
