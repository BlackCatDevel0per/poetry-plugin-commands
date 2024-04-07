from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_commands.command import ListCommandsCommand, UserCommand

if TYPE_CHECKING:
	from typing import Any, Final

	from poetry.console.application import Application
	from poetry.console.commands.command import Command
	from poetry.poetry import Poetry


class UserCommandsApplicationPlugin(ApplicationPlugin):
	"""Main class of the plugin."""

	plugin_section: Final[str] = 'commands'

	@property
	def commands(self: UserCommandsApplicationPlugin) -> list[type[Command]]:
		"""Property with plugin own commands and user's commands.

		User's commands are auto-generated from toml plugin's section shell commands.
		"""
		toml_content: dict[str, Any] = self.poetry.pyproject.data

		user_commands = toml_content['tool']['poetry']['plugins'][self.plugin_section]

		# TODO: Support python commands using toml's optioned values..
		commands = [
			UserCommand._new_cls(alias, command)  # noqa: SLF001
			for alias, command in user_commands.items()
		]

		# TODO: Add, remove, update commands
		ListCommandsCommand._user_commands = user_commands  # noqa: SLF001

		commands.insert(0, ListCommandsCommand)

		del user_commands

		return commands


	def activate(self: UserCommandsApplicationPlugin, application: Application) -> None:
		"""Add poetry app on plugin activation."""
		self.poetry: Poetry = application.poetry

		super().activate(application=application)
