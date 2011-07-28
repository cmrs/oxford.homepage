from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class HomePageView(BrowserView):  

    template = ViewPageTemplateFile('templates/homepage_view.pt')

    def __call__(self):
        return self.template() 
