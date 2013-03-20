from collective.grok import gs
from wcc.document import MessageFactory as _

@gs.importstep(
    name=u'wcc.document', 
    title=_('wcc.document import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.document.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
