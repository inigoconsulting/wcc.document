from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from eea.faceted.vocabularies.catalog import CatalogIndexesVocabulary


class document_sort(CatalogIndexesVocabulary):

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        indexes = ['sortable_title', 'effective', 'document_owner', 'document_type']
        return self._create_vocabulary(context, indexes)


grok.global_utility(document_sort, name="wcc.document.document_sort")
