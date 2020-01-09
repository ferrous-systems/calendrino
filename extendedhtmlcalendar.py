
from calendar import HTMLCalendar, _localized_month

month_name = _localized_month('%B')

class ExtendedHTMLCalendar(HTMLCalendar):
	"Just like HTMLCalendar except the rendering sub-functions pass around a callback which will be used to render additional info in each day"

	def formatday(self, callback, day, weekday):
		"""
		Return a day as a table cell.
		"""

		return '<td class="%s">%d%s</td>\n' % (self.cssclasses[weekday], day, callback(day))

	def formatmonth(self, callback, theyear, themonth, withyear=False):
		"""
		Return a formatted month as a table, top down
		"""
		v = []
		a = v.append
		a('<td>')
		a('\n')
		a('<table border="1" cellpadding="0" cellspacing="0" class="month">')
		a('\n')
		a(self.formatmonthname(theyear, themonth, withyear=withyear))
		a('\n')
		daycounter = 0
		for day in self.itermonthdays2(theyear, themonth):

			if day[0] == 31:
				a('<tr>')
				a(self.formatday(callback, day[0], day[1]))
				a('</tr>')
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 0 :
				continue
			elif day[0] == 0 and daycounter == 28 :
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 29 :
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 30 :
				a('<tr><td class="noday">&nbsp;</td></tr>\n')
				a('\n')
				daycounter = 0
				break
			else:
				a('<tr>')
				a(self.formatday(callback, day[0], day[1]))
				a('</tr>')
				a('\n')
				daycounter += 1
		a('</table>')
		a('\n')
		a('</td>')
		a('\n')
		return ''.join(v)

	def monthname(self, theyear, themonth, withyear=True):
		"""
		Return a month name as a table row.
		"""
		if withyear:
			s = '%s %s' % (month_name[themonth], theyear)
		else:
			s = '%s' % month_name[themonth]
		return '<tr><th colspan="31" class="%s">%s</th></tr>' % (
			self.cssclass_month_head, s)

	def formatmonthleft(self, callback, theyear, themonth, withyear=False):
		"""
		Return a formatted month as a table, left right
		"""
		v = []
		a = v.append
		a('\n')
		a('\n')
		a(self.monthname(theyear, themonth, withyear=withyear))
		a('\n')
		daycounter = 0
		for day in self.itermonthdays2(theyear, themonth):

			if day[0] == 31:
				a(self.formatday(callback, day[0], day[1]))
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 0 :
				continue
			elif day[0] == 0 and daycounter == 28 :
				a('<td class="noday">&nbsp;</td>\n')
				a('<td class="noday">&nbsp;</td>\n')
				a('<td class="noday">&nbsp;</td>\n')
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 29 :
				a('<td class="noday">&nbsp;</td>\n')
				a('<td class="noday">&nbsp;</td>\n')
				a('\n')
				daycounter = 0
				break
			elif day[0] == 0 and daycounter == 30 :
				a('<td class="noday">&nbsp;</td>\n')
				a('\n')
				daycounter = 0
				break
			else:
				a(self.formatday(callback, day[0], day[1]))
				a('\n')
				daycounter += 1
		a('\n')
		a('</tr>')
		a('\n')
		return ''.join(v)
