"""
Toolbar View.
"""

from pyplanet.views import TemplateView

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
		:type app: pyplanet.apps.custom.chatsymbols.Player
		"""
		super().__init__(app.context.ui)

		self.app = app
		self.instance = app.instance
		self.id = 'chatsymbols_toolbar2'


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



	async def action_list(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)
		
	async def action_mf(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)
		
	async def action_jb(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)

	async def action_skip(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z$900$z'
		await self.instance.chat.execute(message)
		
	async def action_extend(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z$393$z'
		await self.instance.chat.execute(message)
			
	async def action_players(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)
		
	async def action_topdons(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)
		
	async def action_topsums(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z$F60$z'
		await self.instance.chat.execute(message)
		
	async def action_mxinfo(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z'
		await self.instance.chat.execute(message)
		
	async def action_help(self, player, *args, **kwargs):
		message  = "$z[" + player.nickname + "$z]" + ' $z$cc0🏆$z'
		await self.instance.chat.execute(message)

	