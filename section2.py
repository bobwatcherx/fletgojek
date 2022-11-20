from flet import *
from flet import colors,icons



section2 = ResponsiveRow([
	Container(
		bgcolor="#FFFFFF",
		border_radius = border_radius.only(topLeft=30,topRight=30),
		padding=0,
		margin = margin.symmetric(vertical=-30),
		content=Column(col={"sm":12,"md":12,"lg":12},
			controls=[
			# FOR INPUT SEARCH LUNCH
				Container(
				bgcolor="#FCFCFC",
				border_radius=30,
				content=Row([
					TextField(
					border="none",
					prefix_icon=icons.SEARCH,
					label="Search Lunch ? "
					),
				IconButton(icon=icons.ACCOUNT_CIRCLE,
					icon_color="green",
					icon_size=30
					),


					])
					),
				# FOR BLUE CARD,
			Card(
			elevation=30,
			content=Container(
			border_radius=30,
			bgcolor="#01ADD5",
			content=Row([
				Container(
				margin=10,
				height=70,
				padding=10,
				width=120,
				border_radius=10,
				bgcolor="white",
				content=Column([
					Text("Gopay",weight="bold",
						size=15
						),
					Text("Rp.7.029",weight="bold",
						size=17
						),
					Text("Tap to Top Up",

						size=11
						),
					],alignment="center",spacing=0)
					),
				# FOR CHILD ICON
				Column([
				Icon(name="bolt",color="white",
					size=30
					),
				Text("Pay",color="white",
					size=15,
					weight="bold"
					)
					]),
				Column([
				Icon(name="add_box",color="white",
					size=30
					),
				Text("Top Up",color="white",
					size=15,
					weight="bold"
					)
					]),
					Column([
				Icon(name="drag_indicator",color="white",
					size=30
					),
				Text("More",color="white",
					size=15,
					weight="bold"
					)
					]),
				],alignment="spaceEvenly")

				)
				)
			])
		)

	])