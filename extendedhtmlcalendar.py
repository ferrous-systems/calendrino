
from calendar import HTMLCalendar

class ExtendedHTMLCalendar(HTMLCalendar):
	"Just like HTMLCalendar except the rendering sub-functions pass around a callback which will be used to render additional info in each day"

	def formatday(self, callback, day, weekday):
		"""
		Return a day as a table cell.
		"""
		if day == 0:
			return '<tr><td class="noday">&nbsp;</td></tr>\n' # day outside month
		else:
			return '<tr><td class="%s">%d%s</td></tr>\n' % (self.cssclasses[weekday], day, callback(day))

	def formatweek(self, callback, theweek):
		"""
		Return a complete week as a table row.
		"""
		s = ''.join(self.formatday(callback, d, wd) for (d, wd) in theweek)
		return 'hekk%s' % s


	def formatmonth(self, callback, theyear, themonth, withyear=True):
		"""
		Return a formatted month as a table.
		"""
		v = []
		a = v.append
		a('<table border="1" cellpadding="0" cellspacing="0" class="month">')
		a('\n')
		a(self.formatmonthname(theyear, themonth, withyear=withyear))
		a('\n')
		for week in self.monthdays2calendar(theyear, themonth):
			a(self.formatweek(callback, week))
			a('\n')
		a('</table>')
		a('\n')
		return ''.join(v)

	def formatyear(self, callback, theyear, width=12):
		"""
		Return a formatted year as a table of tables.
		"""
		v = []
		a = v.append
		width = max(width, 1)
		a('<table border="0" cellpadding="0" cellspacing="0" class="year">')
		a('\n')
		a('<tr><th colspan="%d" class="year">%s</th></tr>' % (
			width, theyear))
		for i in range(1, 1+12, width):
			# months in this row
			months = range(i, min(i+width, 13))
			a('<tr>')
			for m in months:
				a('<td>')
				a(self.formatmonth(callback, theyear, m, withyear=True))
				a('</td>')
			a('</tr>')
		a('</table>')
		return ''.join(v)
