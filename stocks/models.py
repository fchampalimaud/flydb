# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AclframeworkAcltemplate(models.Model):
    acltemplate_id = models.AutoField(primary_key=True)
    acltemplate_table_id = models.IntegerField()
    acltemplate_permissions = models.IntegerField()
    acltemplate_read = models.IntegerField()
    acltemplate_update = models.IntegerField()
    acltemplate_delete = models.IntegerField()
    acltemplate_nread = models.IntegerField()
    acltemplate_nupdate = models.IntegerField()
    acltemplate_ndelete = models.IntegerField()
    group_id = models.IntegerField()
    applyto_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aclframework_acltemplate'
        unique_together = (('group_id', 'applyto_id', 'acltemplate_table_id'),)


class AdminToolsDashboardPreferences(models.Model):
    user_id = models.IntegerField()
    data = models.TextField()
    dashboard_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'admin_tools_dashboard_preferences'


class AdminToolsMenuBookmark(models.Model):
    user_id = models.IntegerField()
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'admin_tools_menu_bookmark'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthMessage(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_message'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CmsCmsplugin(models.Model):
    language = models.CharField(max_length=15)
    position = models.SmallIntegerField(blank=True, null=True)
    creation_date = models.DateTimeField()
    plugin_type = models.CharField(max_length=50)
    parent_id = models.IntegerField(blank=True, null=True)
    tree_id = models.PositiveIntegerField()
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    placeholder_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_cmsplugin'


class CmsGlobalpagepermission(models.Model):
    can_publish = models.IntegerField()
    group_id = models.IntegerField(blank=True, null=True)
    can_moderate = models.IntegerField()
    can_change = models.IntegerField()
    can_change_permissions = models.IntegerField()
    can_recover_page = models.IntegerField()
    can_add = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    can_delete = models.IntegerField()
    can_move_page = models.IntegerField()
    can_change_advanced_settings = models.IntegerField()
    can_view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission'


class CmsGlobalpagepermissionSites(models.Model):
    globalpagepermission_id = models.IntegerField()
    site_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission_sites'


class CmsPage(models.Model):
    rght = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    navigation_extenders = models.CharField(max_length=80, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    reverse_id = models.CharField(max_length=40, blank=True, null=True)
    login_required = models.IntegerField()
    soft_root = models.IntegerField()
    creation_date = models.DateTimeField()
    lft = models.PositiveIntegerField()
    publication_end_date = models.DateTimeField(blank=True, null=True)
    template = models.CharField(max_length=100)
    tree_id = models.PositiveIntegerField()
    publication_date = models.DateTimeField(blank=True, null=True)
    in_navigation = models.IntegerField()
    moderator_state = models.SmallIntegerField()
    published = models.IntegerField()
    site_id = models.IntegerField()
    changed_by = models.CharField(max_length=70)
    created_by = models.CharField(max_length=70)
    publisher_is_draft = models.IntegerField()
    publisher_state = models.SmallIntegerField()
    publisher_public_id = models.IntegerField(unique=True, blank=True, null=True)
    limit_visibility_in_menu = models.SmallIntegerField(blank=True, null=True)
    changed_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cms_page'


class CmsPagePlaceholders(models.Model):
    page_id = models.IntegerField()
    placeholder_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_page_placeholders'
        unique_together = (('page_id', 'placeholder_id'),)


class CmsPagemoderator(models.Model):
    moderate_page = models.IntegerField()
    moderate_children = models.IntegerField()
    page_id = models.IntegerField()
    user_id = models.IntegerField()
    moderate_descendants = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_pagemoderator'


class CmsPagemoderatorstate(models.Model):
    created = models.DateTimeField()
    page_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=3, blank=True, null=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'cms_pagemoderatorstate'


class CmsPagepermission(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    can_publish = models.IntegerField()
    page_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    can_delete = models.IntegerField()
    can_change_permissions = models.IntegerField()
    can_moderate = models.IntegerField()
    can_add = models.IntegerField()
    grant_on = models.IntegerField()
    can_move_page = models.IntegerField()
    can_change = models.IntegerField()
    can_change_advanced_settings = models.IntegerField()
    can_view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_pagepermission'


class CmsPageuser(models.Model):
    user_ptr_id = models.IntegerField(primary_key=True)
    created_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_pageuser'


class CmsPageusergroup(models.Model):
    group_ptr_id = models.IntegerField(primary_key=True)
    created_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_pageusergroup'


class CmsPlaceholder(models.Model):
    slot = models.CharField(max_length=50)
    default_width = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_placeholder'


class CmsTitle(models.Model):
    language = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    page_id = models.IntegerField()
    path = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    slug = models.CharField(max_length=255)
    has_url_overwrite = models.IntegerField()
    application_urls = models.CharField(max_length=200, blank=True, null=True)
    redirect = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    menu_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_title'
        unique_together = (('page_id', 'language'),)


class CmspluginFile(models.Model):
    cmsplugin_ptr_id = models.IntegerField(unique=True)
    file = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmsplugin_file'


class CmspluginFlash(models.Model):
    width = models.CharField(max_length=6)
    cmsplugin_ptr_id = models.IntegerField(unique=True)
    file = models.CharField(max_length=100)
    height = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'cmsplugin_flash'


class CmspluginGooglemap(models.Model):
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    cmsplugin_ptr_id = models.IntegerField(primary_key=True)
    zoom = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=30)
    lng = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    route_planer = models.IntegerField()
    route_planer_title = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmsplugin_googlemap'


class CmspluginLink(models.Model):
    url = models.CharField(max_length=200, blank=True, null=True)
    cmsplugin_ptr_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    page_link_id = models.IntegerField(blank=True, null=True)
    mailto = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmsplugin_link'


class CmspluginPicture(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100)
    cmsplugin_ptr_id = models.IntegerField(unique=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    page_link_id = models.IntegerField(blank=True, null=True)
    float = models.CharField(max_length=10, blank=True, null=True)
    longdesc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cmsplugin_picture'


class CmspluginSnippetptr(models.Model):
    cmsplugin_ptr_id = models.IntegerField(unique=True)
    snippet_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmsplugin_snippetptr'


class CmspluginTeaser(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    cmsplugin_ptr_id = models.IntegerField(primary_key=True)
    page_link_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmsplugin_teaser'


class CmspluginText(models.Model):
    body = models.TextField()
    cmsplugin_ptr_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'cmsplugin_text'


class CmspluginTwitterrecententries(models.Model):
    cmsplugin_ptr_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=75)
    twitter_user = models.CharField(max_length=75)
    count = models.PositiveSmallIntegerField()
    link_hint = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'cmsplugin_twitterrecententries'


class CmspluginTwittersearch(models.Model):
    count = models.PositiveSmallIntegerField()
    query = models.CharField(max_length=200)
    cmsplugin_ptr_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'cmsplugin_twittersearch'


class CmspluginVideo(models.Model):
    cmsplugin_ptr_id = models.IntegerField(primary_key=True)
    movie = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    auto_play = models.IntegerField()
    loop = models.IntegerField()
    bgcolor = models.CharField(max_length=6)
    fullscreen = models.IntegerField()
    width = models.PositiveSmallIntegerField()
    movie_url = models.CharField(max_length=255, blank=True, null=True)
    buttonhighlightcolor = models.CharField(max_length=6)
    auto_hide = models.IntegerField()
    seekbarcolor = models.CharField(max_length=6)
    buttonoutcolor = models.CharField(max_length=6)
    textcolor = models.CharField(max_length=6)
    seekbarbgcolor = models.CharField(max_length=6)
    loadingbarcolor = models.CharField(max_length=6)
    buttonovercolor = models.CharField(max_length=6)
    height = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cmsplugin_video'


class CnpframeworkGroupacl(models.Model):
    groupacl_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(unique=True)
    groupacl_model = models.CharField(max_length=50)
    groupacl_filter = models.TextField()

    class Meta:
        managed = False
        db_table = 'cnpframework_groupacl'


class CnpframeworkLab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cnpframework_lab'


class CnpframeworkPerson(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_first = models.CharField(max_length=60)
    person_last = models.CharField(max_length=60)
    person_pass = models.CharField(max_length=60)
    person_email = models.CharField(max_length=255)
    lab_id = models.IntegerField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'cnpframework_person'
        unique_together = (('person_first', 'person_last'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoAuthopenidAssociation(models.Model):
    server_url = models.TextField()
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_authopenid_association'


class DjangoAuthopenidNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'django_authopenid_nonce'


class DjangoAuthopenidUserassociation(models.Model):
    openid_url = models.CharField(primary_key=True, max_length=255)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_authopenid_userassociation'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class FlyLegacysource(models.Model):
    legacysource_id = models.AutoField(primary_key=True)
    legacysource_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fly_legacysource'


class FlyLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fly_location'


class FlySource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fly_source'


class FlySpecie(models.Model):
    specie_id = models.AutoField(primary_key=True)
    specie_name = models.CharField(max_length=100)
    specie_ncbitax = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fly_specie'


class FlyStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_ccuid = models.CharField(max_length=40, blank=True, null=True)
    specie_id = models.IntegerField()
    stock_entrydate = models.DateTimeField()
    stock_updated = models.DateTimeField()
    stock_chrx = models.CharField(max_length=60, blank=True, null=True)
    stock_chry = models.CharField(max_length=60, blank=True, null=True)
    stock_bal1 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr2 = models.CharField(max_length=60, blank=True, null=True)
    stock_bal2 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr3 = models.CharField(max_length=60, blank=True, null=True)
    stock_bal3 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr4 = models.CharField(max_length=60, blank=True, null=True)
    stock_chru = models.CharField(max_length=230, blank=True, null=True)
    stock_comments = models.TextField(blank=True, null=True)
    stock_hospital = models.IntegerField()
    stock_died = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    stock_loc1_location = models.CharField(max_length=30, blank=True, null=True)
    stock_loc2_person_id = models.IntegerField(blank=True, null=True)
    stock_loc3_data = models.CharField(max_length=30, blank=True, null=True)
    lab_id = models.IntegerField()
    legacysource_id = models.IntegerField()
    stock_legacy1 = models.CharField(max_length=30, blank=True, null=True)
    stock_legacy2 = models.CharField(max_length=30, blank=True, null=True)
    stock_legacy3 = models.CharField(max_length=30, blank=True, null=True)
    stock_flydbid = models.CharField(max_length=50, blank=True, null=True)
    stock_genotype = models.CharField(max_length=255, blank=True, null=True)
    stock_print = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fly_stock'


class FlyStockacl(models.Model):
    acltable_id = models.AutoField(primary_key=True)
    acltable_permissions = models.IntegerField()
    acltable_read = models.IntegerField()
    acltable_update = models.IntegerField()
    acltable_delete = models.IntegerField()
    acltable_nread = models.IntegerField()
    acltable_nupdate = models.IntegerField()
    acltable_ndelete = models.IntegerField()
    group_id = models.IntegerField()
    foreign_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fly_stockacl'
        unique_together = (('group_id', 'foreign_id'),)


class FlySupplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_contact = models.CharField(max_length=30, blank=True, null=True)
    supplier_email = models.CharField(max_length=75, blank=True, null=True)
    supplier_url = models.CharField(max_length=200, blank=True, null=True)
    supplier_address = models.TextField(blank=True, null=True)
    supplier_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fly_supplier'


class MenusCachekey(models.Model):
    language = models.CharField(max_length=255)
    site = models.PositiveIntegerField()
    key = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'menus_cachekey'


class RegistrationRegistrationprofile(models.Model):
    user_id = models.IntegerField(unique=True)
    activation_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class SnippetSnippet(models.Model):
    name = models.CharField(unique=True, max_length=255)
    html = models.TextField()
    template = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'snippet_snippet'


class SouthMigrationhistory(models.Model):
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'
