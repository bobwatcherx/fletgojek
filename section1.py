from flet import *
from flet import colors,icons


section1= Container(
	bgcolor="#0896BA",
	padding=20,
	height=100,
	content=Column([
		Row([
		Container(
			ink=True,
			on_click=lambda e: print("test"),
			content=Row([
				Icon(name="menu",color="white",size=20),
				Text("Promosi",size=15,color="White")
				],spacing=1)
		),
		Container(
			ink=True,
			on_click=lambda e: print("test"),
			content=Row([
				Icon(name="home",color="white",size=20),
				Text("Home",size=15,color="White")
				],spacing=1)
		),
		Container(
			ink=True,
			on_click=lambda e: print("test"),
			content=Row([
				Icon(name="message",color="white",size=20),
				Text("Chat",size=15,color="White")
				],spacing=1)
		),

			],spacing=0,alignment="spaceEvenly")

		],alignment="start")
	)