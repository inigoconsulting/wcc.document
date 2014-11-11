from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.document to 1009',
                description=u'Upgrade wcc.document to 1009',
                source='1008', destination='1009',
                sortkey=1, profile='wcc.document:default')
def to1009(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1008')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1009')


@gs.upgradestep(title=u'Upgrade wcc.document to 1008',
                description=u'Upgrade wcc.document to 1008',
                source='1007', destination='1008',
                sortkey=1, profile='wcc.document:default')
def to1008(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1008')


@gs.upgradestep(title=u'Upgrade wcc.document to 1007',
                description=u'Upgrade wcc.document to 1007',
                source='1006', destination='1007',
                sortkey=1, profile='wcc.document:default')
def to1007(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1007')

    catalog = getToolByName(context, 'portal_catalog')
    brains = catalog({'portal_type': 'wcc.document.document',
                     'Language': 'all'})

    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()


@gs.upgradestep(title=u'Upgrade wcc.document to 1006',
                description=u'Upgrade wcc.document to 1006',
                source='1005', destination='1006',
                sortkey=1, profile='wcc.document:default')
def to1006(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1006')

    brains = context.portal_catalog({'portal_type': 'wcc.document.document',
        'Language': 'all'})

    for b in brains:
        obj = b.getObject()
        dt = getattr(b, 'document_type', [])
        if dt:
            obj.document_type = dt[0]
        else:
            obj.document_type = None
        obj.reindexObject()

    context.portal_catalog.reindexIndex('document_type', context.REQUEST)


@gs.upgradestep(title=u'Upgrade wcc.document to 1005',
                description=u'Upgrade wcc.document to 1005',
                source='1004', destination='1005',
                sortkey=1, profile='wcc.document:default')
def to1005(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1005')

    document_type_map = {
        u'' : u'',
        u'Incoming letter': 'Incoming letter',
        u'Declaration of faith': 'Declaration of faith',
        u' Background document': 'Background document', 
        u'Advocacy report': 'Advocacy report', 
        u'Speech': 'Lecture - Speech',
        u'Article - News item': 'Article - News item',
        u'Statement': 'Statement: public statement', 
        u'Response to study document': 'Response to study document',
        u'Tribute': 'Tribute', 
        u'statement public statement': 'Statement: public statement', 
        u'Statement: minute': 'Statement: minute', 
        u'Statement: letter': 'Statement: letter', 
        u'Background document': 'Background document', 
        u'Liturgical song - music' : 'Liturgical song - music', 
        u'speech' : 'Lecture - Speech', 
        u'Letter' : 'Letter', 
        u'Report' : 'Report', 
        u'Pastoral letter' : 'Pastoral letter', 
        u'Statement: public statement': 'Statement: public statement', 
        u'Lecture - Speech': 'Lecture - Speech', 
        u'Study document': 'Study document', 
        u'Lecture-Speech': 'Lecture - Speech', 
        u'letter': 'Letter',  
        u'Minutes': 'Minutes',
        u'study document': 'Study document', 
        u'Policy document': 'Policy document', 
        u'Message: letter': 'Letter', 
        u'Liturgical text': 'Liturgical text', 
        u'pdf' : u'', 
        u'Message': 'Message', 
        u'Sermon': 'Sermon'
    }

    document_owner_map = {
        u'': '',
        u'WCC commissions': 'WCC Commisions',
        u' WCC programmes': 'WCC Programmes', 
        u'Wider ecumenical movement (incl WCC)': 'Wider ecumenical movement (incl WCC)', 
        u'WCC Presidents': 'WCC Presidents', 
        u'International Ecumenical Peace Convocation': 'International Ecumenical Peace Convocation', 
        u'Echos - Commission on youth in the ecumenical movement': 
            'Echos - Commission on youth in the ecumenical movement', 
        u'WCC Officers': 'WCC Officers', 
        u'Commission on Faith and Order': 'Commission on Faith and Order', 
        u'Commission on World Mission and Evangelism': 
            'Commission on World Mission and Evangelism', 
        u'Comission on Faith and Order': 'Commission on Faith and Order', 
        u'Assembly': 'Assembly', 
        u'Joint Consultative Group Pentecostals - WCC': 
            'Joint Consultative Group Pentecostals - WCC', 
        u'Joint Consultative Commission WCC - Christian World Communions':
            'Joint Consultative Commission WCC - Christian World Communions', 
        u'Other ecumenical bodies':
            'Other ecumenical bodies', 
        u'WC programmes':
            'WCC Programmes', 
        u'Member church':
            'Member church', 
        u'Inter-Religious Relations and Dialogue':
            'Inter-Religious Relations and Dialogue', 
        u'General Scretray': 'General Secretary', 
        u'General Secretary': 'General Secretary', 
        u'Continuation Committee on Ecumenism in the 21st Century': 
            'Continuation Committee on Ecumenism in the 21st Century', 
        u'WCC General Secretary': 'General Secretary', 
        u'WCC Programmes': 'WCC Programmes', 
        u'Conference on World Mission and Evangelism': 
            'Conference on World Mission and Evangelism', 
        u'WCC programmes': 'WCC Programmes', 
        u'Commission on International Affairs': 'Commission on International Affairs', 
        u'Report of the Joint Consultative Group Pentecostals - WCC':
            'Report of the Joint Consultative Group Pentecostals - WCC', 
        u'Moderator of Central Committee':
            'Moderator of Central Committee',
        u'Executive committee':
            'Executive committee', 
        u'Central Committee':
            'Central Committee', 
        u'Special Commission on Orthodox participation in the WCC':
            'Special Commission on Orthodox participation in the WCC', 
        u'Joint Working Group':
            'Joint Working Group'
    }

    brains = context.portal_catalog({'portal_type': 'wcc.document.document',
        'Language': 'all'})

    for b in brains:
        obj = b.getObject()
        dt = getattr(b, 'document_type', u'')
        try:
            t = document_type_map.get(dt, dt)
            obj.document_type = [t]
        except TypeError:
            pass


        do = getattr(b, 'document_owner', u'')
        try:
            o = document_owner_map.get(do, do)
            obj.document_owner = o
        except TypeError:
            pass

        obj.reindexObject()

    context.portal_catalog.reindexIndex('document_owner', context.REQUEST)
    context.portal_catalog.reindexIndex('document_type', context.REQUEST)



@gs.upgradestep(title=u'Upgrade wcc.document to 1004',
                description=u'Upgrade wcc.document to 1004',
                source='1003', destination='1004',
                sortkey=1, profile='wcc.document:default')
def to1004(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1004')
    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(portal_type=['wcc.document.document'],
                                    Language='all'):
        obj = brain.getObject()
        obj.reindexObject()


@gs.upgradestep(title=u'Upgrade wcc.document to 1003',
                description=u'Upgrade wcc.document to 1003',
                source='1002', destination='1003',
                sortkey=1, profile='wcc.document:default')
def to1003(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.document.upgrades:to1003')

    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(portal_type=['wcc.document.document'],
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
