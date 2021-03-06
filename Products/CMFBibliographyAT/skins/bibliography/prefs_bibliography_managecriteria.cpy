## Controller Python Script "prefs_bibliography_duplicates"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=Reconfigure the Bibliography Tool

REQUEST=context.REQUEST

from Products.CMFCore.permissions import ManagePortal

criteria_object = None
if context.portal_membership.checkPermission(ManagePortal, context.portal_url.getPortalObject()):
    criteria_object = context.portal_bibliography

try:
    for ref_type in context.portal_bibliography.getReferenceTypes():
        REQUEST.set('%s_reference_type' % ref_type, 1)
    criteria_object.manage_changeCriteria(REQUEST)
    return state.set(portal_status_message=context.translate(domain='cmfbibliographyat', msgid='bibliography_tool_updated_criteriamanager', default='Updated Bibliography Settings - Duplicates Criteria Manager.'))
except:
    return state.set(portal_status_message=context.translate(domain='cmfbibliographyat', msgid='bibliography_tool_update_criteriamanager_failed', default='Updated Bibliography Settings - Failure in update of Duplicates Criteria Manager.'))

