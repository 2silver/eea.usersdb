import colander

INVALID_PHONE_MESSAGE = (
    "Invalid telephone number. It must be written "
    "using international notation, starting with \"+\"."
)

class UserInfoSchema(colander.MappingSchema):
    """
    Schema for Eionet LDAP user information. Can be used by front-end tools
    to verify data before sending it to `eea.usersdb`. The `eea.usersdb`
    library does very little validation of its own.
    """

    first_name     = colander.SchemaNode(colander.String())
    last_name      = colander.SchemaNode(colander.String())
    job_title      = colander.SchemaNode(colander.String(), missing='')
    email          = colander.SchemaNode(colander.String())
    url            = colander.SchemaNode(colander.String(), missing='')
    postal_address = colander.SchemaNode(colander.String(), missing='')
    phone          = colander.SchemaNode(colander.String(), missing='')
    mobile         = colander.SchemaNode(colander.String(), missing='')
    fax            = colander.SchemaNode(colander.String(), missing='')
    organisation   = colander.SchemaNode(colander.String(), missing='')

_phone_validator = colander.Regex(r'^\+[\d ]+$', msg=INVALID_PHONE_MESSAGE)
UserInfoSchema.phone.validator = _phone_validator
UserInfoSchema.mobile.validator = _phone_validator
UserInfoSchema.fax.validator = _phone_validator

_description_map = {
    'first_name': "First name",
    'last_name': "Last name",
    'job_title': "Job title",
    'email': "E-mail",
    'url': "URL",
    'postal_address': "Postal address",
    'phone': "Telephone number",
    'mobile': "Mobile telephone number",
    'fax': "Fax number",
    'organisation': "Organisation",
}

for name, description in _description_map.iteritems():
    getattr(UserInfoSchema, name).description = description

user_info_schema = UserInfoSchema()
