from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.document to 1002',
                description=u'Upgrade wcc.document to 1002',
                source='1', destination='1002',
                sortkey=1, profile='wcc.document:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1002')
