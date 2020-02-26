"""
Toolbar View.
"""

from pyplanet.views import TemplateView
import datetime

class ToolbarToggle(TemplateView):
	template_name = 'chatsymbols/toggle/toggle.xml'

	def __init__(self, app):
		"""
		Initiate the toolbar view.

		:param app: Player app instance.
		:type app: pyplanet.apps.custom.chatsymbols.toggle.Player
		"""
		super().__init__(app.context.ui)

		self.app = app
		self.instance = app.instance
		self.id = 'chatsymbols_toolbar_toggle'


		self.subscribe('bar_button_view', self.action_view)


	async def get_context_data(self):
		data = await super().get_context_data()
		data['game'] = self.app.instance.game.game
		return data



	async def action_view(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/chatbar')



class ToolbarView(TemplateView):
	"""
	Toolbar View Class.
	"""
	template_name = 'chatsymbols/toolbar/toolbar.xml'

	def __init__(self, app):
		"""
		Initiate the toolbar view.

		:param app: Player app instance.
		:type app: pyplanet.apps.custom.menu.player.Player
		"""
		super().__init__(app.context.ui)

		self.app = app
		self.id = 'chatsymbols_toolbar'
		self.instance = app.instance
		self.player_cooldown = {}

		self.subscribe('bar_button_list', self.action_list)
		self.subscribe('bar_button_mf', self.action_mf)
		self.subscribe('bar_button_jb', self.action_jb)
		self.subscribe('bar_button_skip', self.action_skip)
		self.subscribe('bar_button_extend', self.action_extend)
		
		self.subscribe('bar_button_players', self.action_players)
		self.subscribe('bar_button_topdons', self.action_topdons)
		self.subscribe('bar_button_topsums', self.action_topsums)
		self.subscribe('bar_button_mxinfo', self.action_mxinfo)
		self.subscribe('bar_button_help', self.action_help)
		
	async def get_context_data(self):
		data = await super().get_context_data()
		data['game'] = self.app.instance.game.game
		return data

	async def on_start(self):

		self.app.context.signals.listen(mp_signals.player.player_connect, self.player_connect)

		for player in self.app.instance.player_manager.online:
			self.player_cooldown[player.login] = datetime.datetime.now().timestamp()

	async def player_connect(self, player, is_spectator, source, **kwargs):
		self.player_cooldown[player.login] = datetime.datetime.now().timestamp()

	async def action_list(self, player, *args, **kwargs):
		if player_cooldown[player.login] < datetime.datetime.now().timestamp():
			message  = "[" + player.nickname + "]" + '$z'
			await self.instance.chat.execute(message)
			self.player_cooldown[player.login] = datetime.datetime.now().timestamp() + 10000
		else:
			seconds_left = (self.player_cooldown[player.login] - datetime.datetime.now().timestamp())/ 1000
			message = "{} seconds of cooldown".format(seconds_left)
			await self.instance.chat(message, player)
			
		
	async def action_mf(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')	
		
	async def action_jb(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')

	async def action_skip(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
		
	async def action_extend(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
			
	async def action_players(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
		
	async def action_topdons(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
		
	async def action_topsums(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
		
	async def action_mxinfo(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '')
		
	async def action_help(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '🏆')

	