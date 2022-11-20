from flet import *
from flet import colors,icons

# CREATE APPBAR

appmenu = ResponsiveRow([
	Column(col={"sm":12,"md":12,"lg":12},
		controls=[
		Container(
			padding=10,
			bgcolor="#DEDEDE",
			content=Row([
				# INSERT LOGO GOJEK HERE
				Image(
					src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Gojek_logo_2019.svg/2560px-Gojek_logo_2019.svg.png",
					fit="contain",
					width=120,
					height=50
					),
				CircleAvatar(
				foreground_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnvVX91SdXFqCZ9Xn4QHoRl1kStmfxSSkF0sfFsV9v&s",

					)
				],alignment="spaceBetween")
			)
		])

	])