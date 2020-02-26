"""
Toolbar interface and methods.
"""
import logging

from pyplanet.apps.custom.donatewidget.views.toolbar import ToolbarView
from pyplanet.contrib.command import Command
from pyplanet.contrib.setting import Setting

from pyplanet.apps.core.maniaplanet import callbacks as mp_signals

logger = logging.getLogger(__name__)


class ToolbarPlayer:
	def __init__(self, app):
		"""
		:param app: App instance.
		:type app: pyplanet.apps.custom.donatewidget.app.Player
		"""
		self.app = app
		self.instance = app.instance

		self.view = ToolbarView(self.app)

		self.setting_enable_toolbar = Setting(
			'enable_donatewidget', 'Enable the donatewidget', Setting.CAT_DESIGN, type=bool,
			description='Enable the donate widget.',
			default=True
		)

	async def on_start(self):
		await self.app.context.setting.register(self.setting_enable_toolbar)

		# Listen to connect event.
		self.app.context.signals.listen(mp_signals.player.player_connect, self.player_connect)


		# Display to all current online players.
		if await self.setting_enable_toolbar.get_value():
			for player in self.app.instance.player_manager.online:
				if player.level > player.LEVEL_PLAYER:
					await self.view.display([player.login])

	async def player_connect(self, player, is_spectator, source, **kwargs):
		if player.level > player.LEVEL_PLAYER and await self.setting_enable_toolbar.get_value():
			await self.view.display([player.login])

	async def toggle_toolbar(self, player, *args, **kwargs):
		if player.level <= player.LEVEL_PLAYER:
			return

		if player.login in self.view._is_player_shown:
			await self.view.hide([player.login])
		else:
			await self.view.display([player.login])
