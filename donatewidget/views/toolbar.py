"""
Toolbar View.
"""

from pyplanet.views import TemplateView


class ToolbarView(TemplateView):
	"""
	Toolbar View Class.
	"""
	template_name = 'donatewidget/toolbar/toolbar.xml'

	def __init__(self, app):
		"""
		Initiate the toolbar view.

		:param app: Player app instance.
		:type app: pyplanet.apps.custom.donatewidget.Player
		"""
		super().__init__(app.context.ui)

		self.app = app
		self.id = 'donatewidget'

		self.subscribe('bar_button_100P', self.action_100P)
		self.subscribe('bar_button_500P', self.action_500P)
		self.subscribe('bar_button_1000P', self.action_1000P)
		self.subscribe('bar_button_2000P', self.action_2000P)
		self.subscribe('bar_button_5000P', self.action_5000P)

	async def get_context_data(self):
		data = await super().get_context_data()
		data['game'] = self.app.instance.game.game
		return data



	async def action_100P(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/donate 100')

	async def action_500P(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/donate 500')	
		
	async def action_1000P(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/donate 1000')

	async def action_2000P(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/donate 2000')
		
	async def action_5000P(self, player, *args, **kwargs):
		return await self.app.instance.command_manager.execute(player, '/donate 5000')
			
	