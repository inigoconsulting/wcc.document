from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.document to 1003',
                description=u'Upgrade wcc.document to 1003',
                source='1002', destination='1003',
                sortkey=1, profile='wcc.document:default')
def to1003(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1003')

    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(portal_type=['wcc.churches.churchmember',
                                    'wcc.churches.churchfamily',
                                    'wcc.churches.churchbody'],
                                    Language='all'):
        obj = brain.getObject()
        obj.reindexObject()
        adapted = IExcludeFromNavigation(obj)
        adapted.exclude_from_nav = False
        obj.reindexObject()

@gs.upgradestep(title=u'Upgrade wcc.document to 1002',
                description=u'Upgrade wcc.document to 1002',
                source='1', destination='1002',
                sortkey=1, profile='wcc.document:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1002')
