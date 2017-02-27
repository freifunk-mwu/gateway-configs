# -*- python -*-

# Copyright (C) 1998,1999,2000 by the Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA


"""This is the module which takes your site-specific settings.

From a raw distribution it should be copied to mm_cfg.py.  If you
already have an mm_cfg.py, be careful to add in only the new settings
you want.  The complete set of distributed defaults, with annotation,
are in ./Defaults.  In mm_cfg, override only those you want to
change, after the

  from Defaults import *

line (see below).

Note that these are just default settings - many can be overridden via the
admin and user interfaces on a per-list or per-user basis.

Note also that some of the settings are resolved against the active list
setting by using the value as a format string against the
list-instance-object's dictionary - see the distributed value of
DEFAULT_MSG_FOOTER for an example."""


#######################################################
#    Here's where we get the distributed defaults.    #

from Defaults import *

##############################################################
# Put YOUR site-specific configuration below, in mm_cfg.py . #
# See Defaults.py for explanations of the values.            #

#-------------------------------------------------------------
# The name of the list Mailman uses to send password reminders
# and similar. Don't change if you want mailman-owner to be
# a valid local part.
MAILMAN_SITE_LIST = 'mailman'

#-------------------------------------------------------------
# If you change these, you have to configure your http server
# accordingly (Alias and ScriptAlias directives in most httpds)
DEFAULT_URL_PATTERN = 'https://%s/mailman/'
IMAGE_LOGOS         = '/images/mailman/'

#-------------------------------------------------------------
# Default domain for email addresses of newly created MLs
DEFAULT_EMAIL_HOST = 'lists.freifunk-mwu.de'
#-------------------------------------------------------------
# Default host for web interface of newly created MLs
DEFAULT_URL_HOST   = 'lists.freifunk-mwu.de'
#-------------------------------------------------------------
# Required when setting any of its arguments.
add_virtualhost(DEFAULT_URL_HOST, DEFAULT_EMAIL_HOST)

#-------------------------------------------------------------
# The default language for this server.
DEFAULT_SERVER_LANGUAGE = 'de'

#-------------------------------------------------------------
# Iirc this was used in pre 2.1, leave it for now
USE_ENVELOPE_SENDER    = 0              # Still used?

#-------------------------------------------------------------
# Unset send_reminders on newly created lists
DEFAULT_SEND_REMINDERS = 0

DEB_LISTMASTER = 'postmaster@freifunk-mwu.de'

#-------------------------------------------------------------
# Uncomment this if you configured your MTA such that it
# automatically recognizes newly created lists.
# (see /usr/share/doc/mailman/README.Exim4.Debian or
# /usr/share/mailman/postfix-to-mailman.py)
# MTA=None   # Misnomer, suppresses alias output on newlist

#-------------------------------------------------------------
# Uncomment if you use Postfix virtual domains (but not
# postfix-to-mailman.py), but be sure to see
# /usr/share/doc/mailman/README.Debian first.
MTA='Postfix'

#-------------------------------------------------------------
# Uncomment if you want to filter mail with SpamAssassin. For
# more information please visit this website:
# http://www.jamesh.id.au/articles/mailman-spamassassin/
# GLOBAL_PIPELINE.insert(1, 'SpamAssassin')

# Note - if you're looking for something that is imported from mm_cfg, but you
# didn't find it above, it's probably in /usr/lib/mailman/Mailman/Defaults.py.

# The following is a three way setting.  It sets the default for the list's
# from_is_list policy which is applied to all posts except those for which a
# dmarc_moderation_action other than accept applies.
# 0 -> Do not rewrite the From: or wrap the message.
# 1 -> Rewrite the From: header of posts replacing the posters address with
#      that of the list.  Also see REMOVE_DKIM_HEADERS above.
# 2 -> Do not modify the From: of the message, but wrap the message in an outer
#      message From the list address.
DEFAULT_FROM_IS_LIST = 1
ALLOW_FROM_IS_LIST = Yes

# Do not break existing DKIM signatures
DEFAULT_SUBJECT_PREFIX  = ""
DEFAULT_MSG_HEADER = ""
DEFAULT_MSG_FOOTER = ""

# Final delivery module for outgoing mail.  This handler is used for message
# delivery to the list via the smtpd, and to an individual user.  This value
# must be a string naming a module in the Mailman.Handlers package.
#
# WARNING: Sendmail has security holes and should be avoided.  In fact, you
# must read the Mailman/Handlers/Sendmail.py file before it will work for
# you.
#
#DELIVERY_MODULE = 'Sendmail'
DELIVERY_MODULE = 'SMTPDirect'

# SMTP host and port, when DELIVERY_MODULE is 'SMTPDirect'.  Make sure the
# host exists and is resolvable (i.e., if it's the default of "localhost" be
# sure there's a localhost entry in your /etc/hosts file!)
SMTPHOST = 'localhost'
SMTPPORT = 25 

# Are archives on or off by default?
DEFAULT_ARCHIVE = Off

# Are archives public or private by default?
# 0=public, 1=private
DEFAULT_ARCHIVE_PRIVATE = 1

# The site logo/text presence, site text, site url and site logo
SITE_LINK = Yes
SITE_TEXT = 'Freifunk MWU'
SITE_URL = 'https://map.freifunk-mwu.de/'
SITE_LOGO = '/images/mailman/fflogo_red.png'

OLD_STYLE_PREFIXING = No

DEFAULT_MAX_MESSAGE_SIZE = 2048

# Set this variable to Yes to allow list owners to delete their own mailing
# lists.  You may not want to give them this power, in which case, setting
# this variable to No instead requires list removal to be done by the site
# administrator, via the command line script bin/rmlist.
OWNERS_CAN_DELETE_THEIR_OWN_LISTS = Yes

# This value specifies the default lengths of member and list admin passwords
MEMBER_PASSWORD_LENGTH = 10
ADMIN_PASSWORD_LENGTH = 20
