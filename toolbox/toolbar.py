"""
Toolbar interface and methods.
"""
import logging
import asyncio

from pyplanet.apps.custom.toolbox.views.toolbar import ToolbarView, ToolbarToggle
from pyplanet.contrib.command import Command
from pyplanet.contrib.setting import Setting

from pyplanet.apps.core.maniaplanet import callbacks as mp_signals

logger = logging.getLogger(__name__)

class ToolbarPlayer:
	def __init__(self, app):
		"""
		:param app: App instance.
		:type app: pyplanet.apps.custom.toolbox.app.Player
		"""
		self.app = app
		self.instance = app.instance

		self.view = ToolbarView(self.app)
		self.toggle = ToolbarToggle(self.app)
		self.player_dict = {}
		self.setting_enable_toolbar = Setting(
			'enable_playerbar', 'Enable the Player toolbar', Setting.CAT_DESIGN, type=bool,
			description='Enable and show the Player toolbar for Players.',
			default=True
		)

	async def on_start(self):
		await self.app.context.setting.register(self.setting_enable_toolbar)

		# Listen to connect event.
		self.app.context.signals.listen(mp_signals.player.player_connect, self.player_connect)

		# Register commands.
		await self.instance.command_manager.register(
			Command(command='playerbar', target=self.toggle_toolbar, admin=False, description='Toggle the Player toolbar')
		)

		# Display to all current online players.
		if await self.setting_enable_toolbar.get_value():
			for player in self.app.instance.player_manager.online:
				self.player_dict[player.login] = False
				await self.toggle.display([player.login])

	async def player_connect(self, player, is_spectator, source, **kwargs):
		self.player_dict[player.login] = False
		await self.toggle.display([player.login])

	async def toggle_toolbar(self, player, *args, **kwargs):
		if self.player_dict[player.login] == False:
			await self.view.display([player.login])
			message = '$s$o$fffToolBox $z$fffcreated by StupsKiesel & MosKi'
			await self.instance.chat(message, player)
			self.player_dict[player.login] = True
		else:
			self.player_dict[player.login] = False
			await self.view.hide([player.login])
		
