from flet import *
from flet import colors,icons
import appmenu
import section1
import section2
import section3
import bottombar
def main(page:Page):
	page.padding=0
	page.spacing=0		
	page.scroll ="auto"
	page.update()
	page.add(
		appmenu.appmenu,
		section1.section1,
		section2.section2,
		section3.section3,
		bottombar.bottombar

		)

flet.app(target=main)