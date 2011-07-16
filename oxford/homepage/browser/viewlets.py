from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class HomePageViewlet(ViewletBase):
    render = ViewPageTemplateFile('homepage.pt')

    def update(self):
        self.computed_value = 'any output'
