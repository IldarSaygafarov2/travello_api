from django.db import models


# title
# slug
# short_description
# full_description
# preview
# price
# country
# event_start
# event_end
#

class Event(models.Model):
	pass


# event_id
# photo

class EventGallery(models.Model):
	pass


# title
# day
# description
# event_id

class EventTourProgram(models.Model):
	pass


# event_tour_program_id
# photo

class EventTourProgramGallery(models.Model):
	pass


# event_id
# title
class EventPriceIncluded(models.Model):
	pass


# event_id
# title
class EventPriceNotIncluded(models.Model):
	pass

