from __future__ import annotations

from os import system
from typing import TYPE_CHECKING

from poetry.console.commands.group_command import GroupCommand
from poetry.core.packages.dependency_group import MAIN_GROUP

if TYPE_CHECKING:
	...


class ListCommandsCommand(GroupCommand):
	name = 'user-commands'
	description = "List of user's commands from toml."

	_user_commands: dict[str, str]


	@property
	def default_groups(self: ListCommandsCommand) -> set[str]:
		return {MAIN_GROUP}


	def handle(self: ListCommandsCommand) -> int:
		for alias, command in self._user_commands.items():
			self.line(f'{alias} -> `{command}`', 'info')

		return 0


class UserCommand(GroupCommand):

	name: str
	command: str


	@staticmethod
	def _new_cls(alias: str, command: str) -> type[UserCommand]:
		return type(
			'AutoGenedUserCommand',
			(UserCommand,),
			{'name': alias, 'command': command},
		)


	@property
	def default_groups(self: UserCommand) -> set[str]:
		return {MAIN_GROUP}


	def handle(self: UserCommand) -> int:
		return system(self.command)  # noqa: S605
