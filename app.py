import dash
import os
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from urllib.request import urlopen
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate
import numpy as np
import json

#need to import this stuff to somehow



stylesheets = ['bootstrap.min.css']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.MINTY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

#token = 'pk.eyJ1IjoiemVtbTE2IiwiYSI6ImNrNGhwM2JtMzFjYngzbnFkcXBmM2xjbDYifQ.u4Ld1s5PrOKdrbvBK0r9rg'
token = os.getenv('TOKEN')


with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
	
	

#read in data

df_2 = pd.read_csv('data/total_census_county_grouped.csv', dtype = {"FIPS":str})

df_2['FIPS'] = df_2['FIPS'].apply(lambda x: x.zfill(5))

df_2['STCOUNTYFP'] = df_2['STCOUNTYFP'].astype(str).apply(lambda x: x.zfill(5))



df_education = pd.read_csv('data/census_county_data_education.csv')


test_data_education = df_education[df_education['COUNTYNAME'] == 'Dane County']

census_occ = pd.read_csv('data/census_data_occ.csv')

test_data_occ = census_occ[census_occ['COUNTYNAME'] == 'Abbeville County']

census_nat = pd.read_csv('data/census_nat.csv')

test_data_nat =  census_nat[census_nat['COUNTYNAME'] == 'Hennepin County']





#df = pd.read_csv('census_data.csv')

#data = df_to_geojson(df, properties = ['median_income_individ'])


#first_card = dbc.Card(
#    dbc.CardBody(
#        [
#            html.H5("Card title", className="card-title"),
#            html.P("This card has some text content, but not much else"),
#            dbc.Button("Go somewhere", color="primary"),
#        ]
#    )
#)


def update_scatter_axis(dd_select):
	if dd_select == "UNEMPL_RATE":
		return "Unemployment Rate (%) "
	
	elif dd_select == "POVERTY_RATE":
		return "Poverty Rate (%)"
	
	elif dd_select == "PER_FOREIGN_NOT_US":
		return "Population Foreign Born, Not Citizen (%)"
	
	elif dd_select == "PER_FOREIGN_US":
		return "Population Foreign Born, Citizen (%)"
	
	elif dd_select == "PER_NATIVE":
		return "Population Native (%)"
	
	elif dd_select == "BIKED":
		return "Biked to Work (%)"
	
	elif dd_select == "WALKED":
		return "Walked to Work (%)"
	
	elif dd_select == "PUBLIC_TRANSIT":
		return "Used Public Transit for Commute (%)"
	
	elif dd_select == "MEAN_TIME_TO_WORK_MIN":
		return "Mean Time to Work (Min)"
	
	elif dd_select == "EDUCATION_LESS_9TH":
		return "Education Less than 9th (%)"
	
	elif dd_select == "EDUCATION_NO_DIPLOMA":
		return "Education No Diploma (%)"
	
	elif dd_select == "EDUCATION_HIGHSCHOOL":
		return "Education Highschool (%)"
	
	elif dd_select == "EDUCATION_SOME_COLLEGE":
		return "Education Some College (%)"
	
	elif dd_select == "EDUCATION_ASSOCIATES":
		return "Education Associates (%)"
	
	elif dd_select == "EDUCATION_BACHELORS":
		return "Education Bachelors (%)"
	
	elif dd_select == "EDUCATION_GRADUATE":
		return "Education Graduate (%)"
	
	elif dd_select == "MALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS":
		return "Management, Business, Science, or Arts Occupations Men (%)"
	
	elif dd_select == "FEMALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS":
		return "Management, Business, Science, or Arts Occupations Women (%)"
	
	elif dd_select == "MALE_SERVICE":
		return "Service Occupations Men (%)"
	
	elif dd_select == "FEMALE_SERVICE":
		return "Service Occupations Women (%)"
	
	elif dd_select == "MALE_CONSTRUCTION_NATURAL_RESOURCES":
		return "Construction or Natural Resources Occupations Men (%)"
	
	elif dd_select == "FEMALE_CONSTRUCTION_NATURAL_RESOURCES":
		return "Construction or Natural Resources Occupations Women (%)"
	
	elif dd_select == "MALE_PRODUCTION_TRANSPORTATION_MATERIAL":
		return "Production, Transportation  Occupations Men (%)"
	
	elif dd_select == "FEMALE_PRODUCTION_TRANSPORTATION_MATERIAL":
		return "Production, Transportation Occupations Women (%)"
	
	elif dd_select == "PERCENT_RENTER_UNITS":
		return "Households Renting (%)"
	
	elif dd_select == "PERCENT_OWNER_UNITS":
		return "Households Own House (%)"
	
	elif dd_select == "MEDIAN_HOUSEHOLD_VALUE":
		return "Median Household Value ($)"
	
	elif dd_select == "PERCENT_HOUSES_MORTGAGE":
		return "Households with Mortgage (%)"
	
	elif dd_select == "MEDIAN_RENT":
		return "Median Rent ($)"
	
	elif dd_select == "MEDIAN_INCOME_DOLLARS":
		return "Median Household Income ($)"
	
	

dropdown1 = dcc.Dropdown(
		id = "dropdown1",
		options = [
			{"label": "Unemployment Rate", "value":"UNEMPL_RATE"},
			{"label": "Poverty Rate", "value":"POVERTY_RATE"},
			{"label": "Percent Population Foreign Born, Not Citizen", "value":"PER_FOREIGN_NOT_US"},
			{"label": "Percent Population Foreign Born, Citizen", "value":'PER_FOREIGN_US'},
			{"label": "Percent Population Native", "value":'PER_NATIVE'},
			{"label": "Biked to Work", "value":"BIKED"},			
			{"label": "Walked to Work", "value":"WALKED"},
			{"label": "Public Transit", "value":"PUBLIC_TRANSIT"},
			{"label": "Mean Time to Work", "value":"MEAN_TIME_TO_WORK_MIN"},
			
			
			
			{"label": "Percent Education Less than 9th", "value":"EDUCATION_LESS_9TH"},	
			{"label": "Percent Education No Diploma", "value":"EDUCATION_NO_DIPLOMA"},
			{"label": "Percent Education Highschool", "value":'EDUCATION_HIGHSCHOOL'},
			{"label": "Percent Education Some College", "value":'EDUCATION_SOME_COLLEGE'},	
			{"label": "Percent Education Associates", "value":'EDUCATION_ASSOCIATES'},
			{"label": "Percent Education Bachelors", "value":'EDUCATION_BACHELORS'},
			{"label": "Percent Education Graduate", "value":'EDUCATION_GRADUATE'},
			
			{"label": "Percent of Management, Business, Science, or Arts Occupations Men", "value":"MALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS"},	
			{"label": "Percent of Management, Business, Science, or Arts Occupations Women", "value":"FEMALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS"},
			{"label": "Percent of Service Occupations Men ", "value":'MALE_SERVICE'},
			{"label": "Percent of Service Occupations Women", "value":'FEMALE_SERVICE'},
			{"label": "Percent of Construction or Natural Resources Occupations Men ", "value":'MALE_CONSTRUCTION_NATURAL_RESOURCES'},
			{"label": "Percent of Construction or Natural Resources Occupations Women", "value":'FEMALE_CONSTRUCTION_NATURAL_RESOURCES'},
			{"label": "Percent of Production, Transportation  Occupations Men ", "value":'MALE_PRODUCTION_TRANSPORTATION_MATERIAL'},
			{"label": "Percent of Production, Transportation Occupations Women", "value":'FEMALE_PRODUCTION_TRANSPORTATION_MATERIAL'},
			{"label": "Percent of Households Renting", "value":'PERCENT_RENTER_UNITS'},
			{"label": "Percent of Households Own House", "value":'PERCENT_OWNER_UNITS'},
			{"label": "Median Household Value", "value":'MEDIAN_HOUSEHOLD_VALUE'},
			{"label": "Percent of Households with Mortgage", "value":'PERCENT_HOUSES_MORTGAGE'},
			{"label": "Median Rent", "value":'MEDIAN_RENT'},
			{"label": "Median Household Income", "value":'MEDIAN_INCOME_DOLLARS'},
		
		


			
		], 
		value = "UNEMPL_RATE"
)

dropdown2 = dcc.Dropdown(
		id = "dropdown2",
				options = [
			{"label": "Unemployment Rate", "value":"UNEMPL_RATE"},
			{"label": "Poverty Rate", "value":"POVERTY_RATE"},
			{"label": "Percent Population Foreign Born, Not Citizen", "value":"PER_FOREIGN_NOT_US"},
			{"label": "Percent Population Foreign Born, Citizen", "value":'PER_FOREIGN_US'},
			{"label": "Percent Population Native", "value":'PER_NATIVE'},
			{"label": "Biked to Work", "value":"BIKED"},			
			{"label": "Walked to Work", "value":"WALKED"},
			{"label": "Public Transit", "value":"PUBLIC_TRANSIT"},
			{"label": "Mean Time to Work", "value":"MEAN_TIME_TO_WORK_MIN"},
			
			
			
			{"label": "Percent Education Less than 9th", "value":"EDUCATION_LESS_9TH"},	
			{"label": "Percent Education No Diploma", "value":"EDUCATION_NO_DIPLOMA"},
			{"label": "Percent Education Highschool", "value":'EDUCATION_HIGHSCHOOL'},
			{"label": "Percent Education Some College", "value":'EDUCATION_SOME_COLLEGE'},	
			{"label": "Percent Education Associates", "value":'EDUCATION_ASSOCIATES'},
			{"label": "Percent Education Bachelors", "value":'EDUCATION_BACHELORS'},
			{"label": "Percent Education Graduate", "value":'EDUCATION_GRADUATE'},
			
			{"label": "Percent of Management, Business, Science, or Arts Occupations Men", "value":"MALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS"},	
			{"label": "Percent of Management, Business, Science, or Arts Occupations Women", "value":"FEMALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS"},
			{"label": "Percent of Service Occupations Men ", "value":'MALE_SERVICE'},
			{"label": "Percent of Service Occupations Women", "value":'FEMALE_SERVICE'},
			{"label": "Percent of Construction or Natural Resources Occupations Men ", "value":'MALE_CONSTRUCTION_NATURAL_RESOURCES'},
			{"label": "Percent of Construction or Natural Resources Occupations Women", "value":'FEMALE_CONSTRUCTION_NATURAL_RESOURCES'},
			{"label": "Percent of Production, Transportation  Occupations Men ", "value":'MALE_PRODUCTION_TRANSPORTATION_MATERIAL'},
			{"label": "Percent of Production, Transportation Occupations Women", "value":'FEMALE_PRODUCTION_TRANSPORTATION_MATERIAL'},
			{"label": "Percent of Households Renting", "value":'PERCENT_RENTER_UNITS'},
			{"label": "Percent of Households Owning House", "value":'PERCENT_OWNER_UNITS'},
			{"label": "Median Household Value", "value":'MEDIAN_HOUSEHOLD_VALUE'},
			{"label": "Percent of Household with Mortgage", "value":'PERCENT_HOUSES_MORTGAGE'},
			{"label": "Median Rent", "value":'MEDIAN_RENT'},
			{"label": "Median Household Income", "value":'MEDIAN_INCOME_DOLLARS'},
		
		


			
		],
		value = "POVERTY_RATE"
)

#dropdown2 = dcc.Dropdown(
#		id = "dropdown2",
#		options = [
#			{"label": "Public Transit", "value":"PUBLIC_TRANSIT"},
#			{"label": "Walked", "value":"WALKED"}
#		], 
#		value = "MEDIAN_RENT"
#)


tenth_card = dbc.Card(dbc.CardBody([
	dbc.Row([dbc.Col([dbc.Row([dbc.Col([html.H4("Select a Field to Show in Map and on Y axis of Scatterplot") ])]),dropdown1],width = 6), dbc.Col([dbc.Row([dbc.Col([html.H4("Select a Field to show on X axis of Scatter Plot") ])]),dropdown2],width = 6)])
]
))

def update_tooltip(dd_select, value):
	if dd_select == "UNEMPL_RATE":
		return  "<b>%{text}</b><br>Unemployment Rate: %{" + value + ":.0f}%"
	
	elif dd_select == "POVERTY_RATE":
		return "<b>%{text}</b><br>Poverty Rate: %{" + value + ":.0f}%"
	
	elif dd_select == "PER_FOREIGN_NOT_US":
		return "<b>%{text}</b><br>Population Foreign Born, Not Citizen: %{" + value + ":.1f}%"
	
	elif dd_select == "PER_FOREIGN_US":
		return "<b>%{text}</b><br>Population Foreign Born, Citizen: %{" + value + ":.1f}%"
	 
	elif dd_select == "PER_NATIVE":
		return "<b>%{text}</b><br>Population Native: %{" + value + ":.1f}%"
	
	elif dd_select == "BIKED":
		return "<b>%{text}</b><br>Biked to Work:  %{" + value + ":.1f}%"
	
	elif dd_select == "WALKED":
		return "<b>%{text}</b><br>Walked to Work: %{" + value + ":.1f}%"
	
	elif dd_select == "PUBLIC_TRANSIT":
		return "<b>%{text}</b><br>Used Public Transit for Commute: %{" + value + ":.1f}%"
	
	elif dd_select == "MEAN_TIME_TO_WORK_MIN":
		return "<b>%{text}</b><br>Mean Time to Work (Min): %{" + value + ":.1f}"
	
	elif dd_select == "EDUCATION_LESS_9TH":
		return "<b>%{text}</b><br>Education Less than 9th: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_NO_DIPLOMA":
		return "<b>%{text}</b><br>Education No Diploma: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_HIGHSCHOOL":
		return "<b>%{text}</b><br>Education Highschool: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_SOME_COLLEGE":
		return "<b>%{text}</b><br>Education Some College: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_ASSOCIATES":
		return "<b>%{text}</b><br>Education Associates: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_BACHELORS":
		return "<b>%{text}</b><br>Education Bachelors: %{" + value + ":.0f}%"
	
	elif dd_select == "EDUCATION_GRADUATE":
		return "<b>%{text}</b><br>Education Graduate: %{" + value + ":.0f}%"
	
	elif dd_select == "MALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS":
		return "<b>%{text}</b><br>Management, Business, Science, or Arts Occupations Men: %{" + value + ":.1f}%"
	
	elif dd_select == "FEMALE_MANAGEMENT_BUSINESS_SCIENCE_ARTS":
		return "<b>%{text}</b><br>Management, Business, Science, or Arts Occupations Women: %{" + value + ":.1f}%"
	
	elif dd_select == "MALE_SERVICE":
		return "<b>%{text}</b><br>Service Occupations Men: %{" + value + ":.1f}%"
	
	elif dd_select == "FEMALE_SERVICE":
		return "<b>%{text}</b><br>Service Occupations Women: %{" + value + ":.1f}%"
	
	elif dd_select == "MALE_CONSTRUCTION_NATURAL_RESOURCES":
		return "<b>%{text}</b><br>Construction or Natural Resources Occupations Men: %{" + value + ":.1f}%"
	
	elif dd_select == "FEMALE_CONSTRUCTION_NATURAL_RESOURCES":
		return "<b>%{text}</b><br>Construction or Natural Resources Occupations Women: %{" + value + ":.1f}%"
	
	elif dd_select == "MALE_PRODUCTION_TRANSPORTATION_MATERIAL":
		return "<b>%{text}</b><br>Production, Transportation  Occupations Men: %{" + value + ":.1f}%"
	
	elif dd_select == "FEMALE_PRODUCTION_TRANSPORTATION_MATERIAL":
		return "<b>%{text}</b><br>Production, Transportation Occupations Women: %{" + value + ":.1f}%"
	
	elif dd_select == "PERCENT_RENTER_UNITS":
		return "<b>%{text}</b><br>Households Renting: %{" + value + ":.0f}%"
	
	elif dd_select == "PERCENT_OWNER_UNITS":
		return "<b>%{text}</b><br>Households Own House: %{" + value + ":.0f}%"
	
	elif dd_select == "MEDIAN_HOUSEHOLD_VALUE":
		return "<b>%{text}</b><br>Median Household Value: $%{" + value + ":.1f}"
	
	elif dd_select == "PERCENT_HOUSES_MORTGAGE":
		return "<b>%{text}</b><br>Households with Mortgage: %{" + value + ":.1f}%"
	
	elif dd_select == "MEDIAN_RENT":
		return "<b>%{text}</b><br>Median Rent: $%{" + value + ":.1f}"
	
	elif dd_select == "MEDIAN_INCOME_DOLLARS":
		return "<b>%{text}</b><br>Median Household Income: $%{" + value + ":.1f}"



def generate_choro(dd_select,value = None):
	"""
    :param dd_select: dropdown select value.
    :param start: start date from date-picker.
    :param end: end date from date-picker.
    :return: Choropleth map displaying average delay time.
    """
	#selected_points = df_2[df_2['COUNTYNAME'] == value].index,
	#selected_points = [[733]]
	#print("selected points: " + str(selected_points))
	test = update_tooltip(dd_select, 'z')
	
	if value is not None:
	
		center_long = df_2.iloc[value[0], -3]
		print(df_2.iloc[value[0], -3])
		print("center_long:" + str(center_long))
		center_lat = df_2.iloc[value[0], -4]
		print(center_lat)
		county_data = [
		go.Choroplethmapbox(
				   name = "",
				   geojson = counties,
				   showscale = True,
				   locations = df_2['FIPS'].values,
				   z = df_2[dd_select].values,
				   marker_opacity=0.5,
				   text=df_2['Geographic Area Name'],
				   colorscale='deep',
			   	 hovertemplate = test,
				   selectedpoints =value,
			 selected = {
						'marker' :  { 'opacity': 1},
						#'marker': {'color': '#85144b'}

				},
			unselected = {

				'marker': {'opacity': .3}
			},
				#reversescale=True,
			   marker=dict(line={"color": "rgb(255,255,255)"}),
				customdata=df_2[dd_select].values,

				   #color = 'rgba(163,22,19,0.8)

	)
		]

	#	title = (
	#		"Average Departure Delay <b>(Minutes)</b> <br> By Original State"
	#		if dd_select == "WALKED"
	#		else "Average Arrival Delay <b>(Minutes)</b> <br> By Destination State"
	#	)

		layout = dict(
	#		title=dict(
	#			text=title,
	#			font=dict(family="Open Sans, sans-serif", size=15, color="#515151"),
	#		),
			hovermode= 'closest',
			hoverlabel = dict(bgcolor = "#CED2CC" ),
		
			  autosize = True,
			margin=go.layout.Margin(
			l=0,
			r=0,
			b=0,
			t=0,
			pad=0,
			autoexpand=True
		),	

			automargin=False,
			clickmode="event+select",
			mapbox = dict(
			accesstoken=token,
			style="light",
			autosize = True,
			
			marker=dict(
				size=20,
			



			),
			
			center=dict(lon = center_long, lat=center_lat),
			zoom = 5,

#			hovermode = None,
#			hoverlabel = dict(
#			bgcolor = "white",
#			font_size = 12,
#			font_family = "Rockwell"
#			)




				)
		)

		return {"data": county_data, "layout": layout}
	
	else:
		center_long = df_2.iloc[713, -3]
		print("center_long:" + str(center_long))
		center_lat = df_2.iloc[713, -4]
		print(center_lat)
		county_data = [
		go.Choroplethmapbox(
				   name = "",	
				   geojson = counties,
				   showscale = True,
				   locations = df_2['FIPS'].values,
				   z = df_2[dd_select].values,
				   marker_opacity=0.5,
				   text=df_2['Geographic Area Name'],
				   hovertemplate = test,
				   colorscale='deep',

				#reversescale=True,
			   marker=dict(line={"color": "rgb(255,255,255)"}),
				customdata=df_2[dd_select].values,

				   #color = 'rgba(163,22,19,0.8)

	)
		]

	#	title = (
	#		"Average Departure Delay <b>(Minutes)</b> <br> By Original State"
	#		if dd_select == "WALKED"
	#		else "Average Arrival Delay <b>(Minutes)</b> <br> By Destination State"
	#	)

		layout = dict(
	#		title=dict(
	#			text=title,
	#			font=dict(family="Open Sans, sans-serif", size=15, color="#515151"),
	#		),
			  autosize = True,
				 margin=go.layout.Margin(
			l=0,
			r=0,
			b=0,
			t=0,
			pad=0,
			autoexpand=True
		),	

			automargin=False,
			clickmode="event+select",
			hovermode= 'closest',
			hoverlabel = dict(bgcolor = "#CED2CC" ),
			mapbox = dict(
			accesstoken=token,
			style="light",
			autosize = True,
			marker=dict(
				size=20,
			


			),
				
			

			center=dict(lon = center_long, lat=center_lat),
			zoom = 3,




				)
		)

		return {"data": county_data, "layout": layout}
	

		

def generate_scatter(dd_select_x,dd_select_y, value,):
	selected_points = [value]
	test_x = update_tooltip(dd_select_x, 'x')
	
	test_y = update_tooltip(dd_select_y, 'y').replace('<b>%{text}</b><br>', '')
	
	scatter_data = [
		 go.Scatter(
			 		name = "",
                    x=df_2[dd_select_x],
                    y=df_2[dd_select_y],
                    text=df_2['Geographic Area Name'],
                    mode='markers',
                    opacity=0.8,
					hoverlabel = dict(bgcolor = "#CED2CC" ),
                    marker={
                        'size': 10,
                        'line': {'width': 1, 'color': 'Black'}
                    },
			 
                   selectedpoints = selected_points, 
			 
			 	    unselected = {
                	'marker' :  { 'opacity': 0.15, "color":'gray'},
					
                # make text transparent when not selected
                'textfont' :  { 'color': 'rgba(0, 0, 0, 0)' }
            },
			 selected = {
                	'marker' :  { 'opacity': 1, "color":'#D32D41'},
					
                # make text transparent when not selected
                'textfont' :  { 'color': 'rgba(0, 0, 0, 0)' }
            },
			 
			  line_width=2,
			  hovertemplate = test_x + '<br>' + test_y
			 	
                ) 
		
	]
	


	layout = go.Layout(
			hovermode= 'closest',
                xaxis={'title':update_scatter_axis(dd_select_x) },
                yaxis={'title': update_scatter_axis(dd_select_y)},
                margin={'l': 60, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                
				#transition={'duration': 300, 'easing': 'cubic-in-out'},
				
				
            )
	
	return {"data": scatter_data, "layout":layout}

first_card =  dbc.Card(dbc.CardBody([
    dbc.Row([dbc.Col([html.H2(html.Strong("How Counties Compare")),html.H4("Click on a county to see more detailed information about that county further down on the dashboard", id = "map-text") ], width = 10)]),
    dcc.Graph(
        
      

        id='main-map',
#        config={'scrollZoom':True, 'staticPlot':False, 'responsive':True},
		figure = generate_choro(dd_select = "UNEMPL_RATE")

       
  

    
)]), color="light")


second_card = dbc.Card(dbc.CardBody([
        dbc.Row([dbc.Col([html.H2(html.Strong("Comparing Census Fields")),html.H4("Select a point to see where the county is on the map on the left") ])]),
 dcc.Graph(
        id='scatter',
        figure = generate_scatter(dd_select_y = "UNEMPL_RATE", dd_select_x = "POVERTY_RATE", value = None)
    )
])
, color = "light")

def generate_box1(value):
	if value == None:
		selected_points = []
	selected_points = [value]
	box_data = [
		go.Box(
			y = df_2["MEDIAN_RENT"],
			text=df_2['COUNTYNAME'], 
			boxpoints = 'all',
			jitter = 0,	
			marker = dict(color = "#1F3F49"),
			name = '',
#			hoverinfo= 'none',
			selectedpoints = selected_points, 
			 
			 selected = {
                	'marker' :  { 'opacity': 1, "color":'black'},
					
              
            },
			
				 unselected = {
                	'marker' :  { 'opacity': .01, "color":'grey'},
					
              
            }
		
		)
	]
	
	layout = go.Layout(
				 margin=dict(
						l=40,
						r=30,
						b=50,
					 	t =50
						
					),
		
		 yaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
		
		xaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
              
            )
	
	return {"data": box_data, "layout":layout}

third_card = dbc.Card(dbc.CardBody([
       
		dbc.Row([dbc.Col(html.Span([html.H4('Median Rent for:  '), html.H3(html.B('Dane County', style = {"font-size":"18px"}, id = "county_text1"))]), style = {"text-align":"center"})]),
		dbc.Row([dbc.Col(html.H1("", id = "rent_text", style = {"text-align":"center"}))]),
		
		
		dcc.Graph(
        id='box1',
        figure= generate_box1(value = 713 )
    )
		
		
		
		
])
, color = "light")

def generate_box2(value):
	
	selected_points = [value]
	box_data = [
		go.Box(
			y = df_2["MEDIAN_HOUSEHOLD_VALUE"],
			text=df_2['COUNTYNAME'], 
			boxpoints = 'all',
			jitter = 0,	
			marker = dict(color = "#1F3F49"),
			selectedpoints = selected_points, 
			name = "",
			 selected = {
                	'marker' :  { 'opacity': 1, "color":'black'},
					
              
            },
			
				 unselected = {
                	'marker' :  { 'opacity': .01,"color":'grey'},
					
              
            }
		
		)
	]
	
	layout = go.Layout(
            
              	 margin=dict(
						l=40,
						r=30,
						b=50,
					 	t =50
						
					),
              
		  yaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
		
		xaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
            )
	
	return {"data": box_data, "layout":layout}

fourth_card = dbc.Card(dbc.CardBody([
     	dbc.Row([dbc.Col(html.Span([html.H4('Median House Value:  '), html.H3(html.B('Dane County', style = {"font-size":"18px"}, id = "county_text2"))]), style = {"text-align":"center"})]),

		dbc.Row([dbc.Col(html.H1("", id = "house_price_text", style = {"text-align":"center"}))]),
		
		
		dcc.Graph(
        id='box2',
        figure= generate_box2(value = 713 )
    )
		
		
		
		
])
, color = "light")


def generate_box3(value):

	selected_points = [value]

	box_data = [
		go.Box(
			y = df_2["MEAN_TIME_TO_WORK_MIN"],
			text=df_2['COUNTYNAME'], 
			boxpoints = 'all',
			
			jitter = 0,	
			marker = dict(color = "#1F3F49"),
			selectedpoints = selected_points, 
			name = "",
			 selected = {
                	'marker' :  { 'opacity': 1, "color":'black'},
					
              
            },
			
				 unselected = {
                	'marker' :  { 'opacity': .008,"color":'grey'},
					
              
            }
		
		)
	]
	
	layout = go.Layout(
                
			 margin=dict(
						l=40,
						r=30,
						b=50,
					 	t =50
						
					),
        yaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
		
		xaxis = dict(
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ),
              
            )
	
	return {"data": box_data, "layout":layout}

fifth_card = dbc.Card(dbc.CardBody([
       	dbc.Row([dbc.Col(html.Span([html.H4('Avg. Commute (min):  '), html.H3(html.B('Dane County', style = {"font-size":"18px"}, id = "county_text3"))]), style = {"text-align":"center"})]),
	
		dbc.Row([dbc.Col(html.H1("", id = "commute_text", style = {"text-align":"center"}))]),
		
		
		dcc.Graph(
        id='box3',
        figure= generate_box3(value = 713)
    )
		
		
		
		
])
, color = "light")

def generate_dist(value):
	dist_county = df_2.iloc[value]
	dist_data = [
		
		{			
					'x':['<$10K'],
					'y' : [dist_county["INCOME_LESS_10000"]],
					"name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1", "line": {"width":"1", "color":"black"}},
					
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
					
				
				
				},
				
					{
					'x':['$10-15K'],
					'y' : [dist_county["INCOME_10000_14999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1", "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				
				},
				
				{
					'x':['$15-25K'],
					'y' : [dist_county["INCOME_15000_24999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate':"<b>%{y}</b> of people make %{x}",
				
				},
				
					{
					'x':['$25-35K'],
					'y' : [dist_county["INCOME_25000_34999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				},
				
						{
					'x':['$35-50K'],
					'y' : [dist_county["INCOME_35000_49999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1", "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				},
					
				{
					'x':['$50-75K'],
					'y' : [dist_county["INCOME_50000_74999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				},
				
				{
					'x':['$75-100K'],
					'y' : [dist_county["INCOME_75000_99999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				},
				
				{
					'x':['$100 - 150K'],
					'y' : [dist_county["INCOME_100000_149999"]],
					 
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				},
				
				{
					'x':['$150-200K'],
					'y' : [dist_county["INCOME_150000_199999"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1",  "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				},
				
						{
					'x':['> $200K'],
					'y' : [dist_county["INCOME_200000"]],
					 "name":"",
					'type':'bar',
					'marker':{"color":"#407D72", "opacity":"1", "line": {"width":"1", "color":"black"}},
					'hovertemplate': "<b>%{y}</b> of people make %{x}",
				
				}, 
	
	]
	layout = go.Layout(
			showlegend = False,
			bargap = .03,
			hovermode = "closest",
			hoverlabel = dict(bgcolor = "#CED2CC" ),
			
			margin=dict(	pad = 20,
                            b=80, #bottom margin 40px
                            l=100, #left margin 40px
                            r=40, #right margin 20px
                            t=40, #top margin 20px
                        ),
			yaxis = dict(
						#tickformat = '%.00%',
						ticksuffix="%",
							
			  		zerolinecolor='rgb(255, 255, 255)'
			  
			  ,

			)
		
			)
	
	return {"data":dist_data, "layout":layout}

sixth_card = dbc.Card(dbc.CardBody([
        dbc.Row([dbc.Col(html.Span([html.H3('Income Distribution For Dane County', style = {"font-size":"18px"},id = 'inc'), html.H4('Median Household Income: ', )]), style = {"text-align":"center"})]),
		dbc.Row([dbc.Col(html.H1("", id = "inc_text", style = {"text-align":"center"}))]),
		
 dcc.Graph(
        id='distribution',
        figure = generate_dist(value = 713)
    )
]), className = "mb-2"
, color = "light")	

def generate_treemap(value):
	county = df_2.iloc[value]['COUNTYNAME']
	state = df_2.iloc[value]['STATE']
	df_ed_county = df_education[(df_education['COUNTYNAME'] == county) & (df_education['STATE'] == state)]

	tree_data = [
		go.Treemap(
			name = "",
         	labels = df_ed_county['EDUCATION_LEVEL'].replace( {'EDUCATION_BACHELORS':'Bachelors', 'EDUCATION_GRADUATE':'Graduate',
															  'EDUCATION_HIGHSCHOOL':'Highschool Diploma', 
															   'EDUCATION_SOME_COLLEGE': 'Some College', 'EDUCATION_ASSOCIATES':'Associates',
															  'EDUCATION_NO_DIPLOMA':'Highschool No Diploma', 'EDUCATION_LESS_9TH':'Finished less than 9th'}),
			#labels = ['Finished less than 9th', 'No Highschool Diploma', 'Highschool Diploma', 
			#		 'Some College', 'Bachelors', 'Associates', 'Graduate'],
            parents = [""]*len(df_ed_county['EDUCATION_LEVEL'].unique()),
            values = df_ed_county['PERCENT TOTAL'],
			marker = dict(colors = ["#f5874c","#407D72","#B1836A","#6AB187" ,"#B16A7F","#CED2CC",'#1F3F49' ],line = dict(width = 1, color = "black")
			
            ),
			textfont = dict(size = 14),
			textinfo = 'label+percent entry',
			texttemplate = "%{label}<br><b>%{value:.0f}%</b>",
			hovertemplate = "%{label}<br><b>%{value:.0f}%</b>",
		)

		
				]
	layout = go.Layout(
		#uniformtext=dict(minsize=100, mode='show')
	  
	   	hovermode = "closest",
		hoverlabel = dict(bgcolor = "#CED2CC" ),
	   uniformtext = dict( minsize = 10,mode='hide'),margin=dict(pad = 0,t=10, b=10, r=10, l=10)
	)
	
	#print(df_ed_county['EDUCATION_LEVEL'].values)
	
	return {"data": tree_data, "layout":layout}

seventh_card = dbc.Card(dbc.CardBody([
        dbc.Row([dbc.Col([html.H2(html.Strong("Educational Makeup of a County")),html.H4("How Educated is Dane County, Wisconsin?", id = "education") ])]), 
		
		
		
		dcc.Graph(
        id='treemap',
        figure=generate_treemap(713))
    
		
		
		
		
])
, color = "light")	


def generate_bar(value):
	county = df_2.iloc[value]['COUNTYNAME']
	state = df_2.iloc[value]['STATE']
	census_occ_county = census_occ[(census_occ['COUNTYNAME'] == county) & (census_occ['STATE'] == state)]
	
	trace0 = go.Bar(
	
	y =  ['Management/Business/Science/Arts'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'MANAGEMENT_BUSINESS_SCIENCE_ARTS']['MALE'].values[0]],
	orientation = 'h' ,
	name = "Men",
	
	marker = dict(color = "#1F3F49", line = dict(width = 1, color = 'black')),
	customdata =  census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'MANAGEMENT_BUSINESS_SCIENCE_ARTS']['PERCENT_MALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Men",
	)

	trace1 = go.Bar(
	
	y =  ['Management/Business/Science/Arts'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'MANAGEMENT_BUSINESS_SCIENCE_ARTS']['FEMALE'].values[0]],
	orientation = 'h',
	text =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'MANAGEMENT_BUSINESS_SCIENCE_ARTS']['TOTALS'].values[0]],
	texttemplate='%{text:.4s}', 
	textposition='auto',
	name = "Women",
	marker = dict(color = "#CED2CC", line = dict(width = 1, color = 'black')),
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'MANAGEMENT_BUSINESS_SCIENCE_ARTS']['PERCENT FEMALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Women"
	)

	trace2 = go.Bar(
	name = "",
	y =  ['Service'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SERVICE']['MALE'].values[0]],
	orientation = 'h',
	marker = dict(color = "#1F3F49", line = dict(width = 1, color = 'black')),
	showlegend = False,
		customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SERVICE']['PERCENT_MALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Men",
	)

	trace3 = go.Bar(
	name = "",
	y =  ['Service'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SERVICE']['FEMALE'].values[0]],
	orientation = 'h' ,
	text =   [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SERVICE']['TOTALS'].values[0]],
	texttemplate='%{text:.4s}', 
	textposition='auto',
	marker = dict(color = "#CED2CC", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SERVICE']['PERCENT FEMALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Women"
	)

	trace4 = go.Bar(
	name = "",
	y =  ['Sales/Office'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SALES_OFFICE']['MALE'].values[0]],
	orientation = 'h',
	marker = dict(color = "#1F3F49", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SALES_OFFICE']['PERCENT_MALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Men",
	)

	trace5 = go.Bar(
	name = "",
	y =  ['Sales/Office'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SALES_OFFICE']['FEMALE'].values[0]],
	orientation = 'h',
	text =   [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SALES_OFFICE']['TOTALS'].values[0]],
	texttemplate='%{text:.4s}', 
	textposition='auto',
	marker = dict(color = "#CED2CC", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'SALES_OFFICE']['PERCENT FEMALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Women"
	)


	trace6 = go.Bar(
	name = "",
	y =  ['Construction/Natural Resources'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'CONSTRUCTION_NATURAL_RESOURCES']['MALE'].values[0]],
	orientation = 'h',
	marker = dict(color = "#1F3F49", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'CONSTRUCTION_NATURAL_RESOURCES']['PERCENT_MALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Men",
	)

	trace7 = go.Bar(
	name = "",
	y =  ['Construction/Natural Resources'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'CONSTRUCTION_NATURAL_RESOURCES']['FEMALE'].values[0]],
	orientation = 'h',
	text =   [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'CONSTRUCTION_NATURAL_RESOURCES']['TOTALS'].values[0]],
	texttemplate='%{text:.4s}', 
	textposition='auto',
	marker = dict(color = "#CED2CC", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'CONSTRUCTION_NATURAL_RESOURCES']['PERCENT FEMALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Women"
	)

	trace8 = go.Bar(
	name = "",
	y =  ['Production/Transportation/Material'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'PRODUCTION_TRANSPORTATION_MATERIAL']['MALE'].values[0]],
	orientation = 'h',
	marker = dict(color = "#1F3F49", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'PRODUCTION_TRANSPORTATION_MATERIAL']['PERCENT_MALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Men",
	)

	trace9 = go.Bar(
	name = "",
	y =  ['Production/Transportation/Material'],
	x =  [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'PRODUCTION_TRANSPORTATION_MATERIAL']['FEMALE'].values[0]],
	orientation = 'h',
	text =   [census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'PRODUCTION_TRANSPORTATION_MATERIAL']['TOTALS'].values[0]],
	texttemplate='%{text:.4s}', 
	textposition='auto',
	marker = dict(color = "#CED2CC", line = dict(width = 1, color = 'black')),
	showlegend = False,
	customdata = census_occ_county[census_occ_county['OCCUPATION_LEVEL'] == 'PRODUCTION_TRANSPORTATION_MATERIAL']['PERCENT FEMALE'],
	hovertemplate = "%{y}<br><b>%{customdata:.1f}%</b> are Women"
	)


	bar_data = [
		trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9
		
				]
	layout = go.Layout(
          	hovermode = "closest",
		hoverlabel = dict(bgcolor = "#CED2CC" ),
			barmode = "stack",
			bargap = .1,
			showlegend = True,
			margin=dict(	
                            b=40,
                            l=230, 
                            r=0, 
                            t=40, 
                        ),
            )
	
	return {"data": bar_data, "layout":layout}



eighth_card = dbc.Card(dbc.CardBody([
        dbc.Row([dbc.Col([html.H2(html.Strong("Comparing Occupations for Dane County, WI"), id = "occup"),html.H4("How many men and women work in each occupation sector?") ])]), 
		
		
		
		dcc.Graph(
        id='bar',
        figure=generate_bar(713 )
    )
		
		
		
		
])
, color = 'light')




def generate_pie(value):
	county = df_2.iloc[value]['COUNTYNAME']
	state = df_2.iloc[value]['STATE']
	pie_data = [
		go.Pie(
	name = "",
    labels =  ['Native', 'Foreign: Naturalized Citizen', 'Foreign: Not U.S. Citizen'],
	customdata =[census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_NATIVE'].values[0],
       census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_FOREIGN_BORN_NATURALIZED_CITIZEN'].values[0],
        census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_FOREIGN_BORN_NOT_US_CITIZEN'].values[0]],
			
    values = [census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_NATIVE'].values[0],
       census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_FOREIGN_BORN_NATURALIZED_CITIZEN'].values[0],
        census_nat[(census_nat['COUNTYNAME'] == county) & (census_nat["STATE"] == state)]['TOTAL_FOREIGN_BORN_NOT_US_CITIZEN'].values[0]],
	marker = dict(colors = ["#1F3F49","#407D72","#CED2CC"], line = dict(width = 1, color = 'black')),
				  textfont = dict(size = 14),
		hovertemplate = "<b>%{percent}</b> of population is %{label}"
            )

		
	]
	layout = go.Layout(
		         	hovermode = "closest",
		hoverlabel = dict(bgcolor = "#CED2CC" ),
	
	)
	return {"data": pie_data, "layout":layout}

#ninth_card = dbc.Card(dbc.CardBody([
#        dbc.Row([dbc.Col(html.H3("Column2"))]), 
#		
#		
#		
#		dcc.Graph(
#        id='life-exp-vs-gdp9',
#        figure={
#            "data": [go.Pie(
#    labels =  ['Native', 'Foreign: Naturalized Citizen', 'Foreign: Not U.S. Citizen'],
#    values = [test_data_nat['TOTAL_NATIVE'].values[0],
#       test_data_nat['TOTAL_FOREIGN_BORN_NATURALIZED_CITIZEN'].values[0],
#       test_data_nat['TOTAL_FOREIGN_BORN_NOT_US_CITIZEN'].values[0]]
#)]
#          
#        }
#    )
#		
#		
#		
#		
#])
#, color = 'light')

ninth_card = dbc.Card(dbc.CardBody([
        dbc.Row([dbc.Col([html.H2(html.Strong("Nativity in the US")),html.H4("How many people have immigrated to Dane County, Wisconsin?", id = "nativ") ])]), 
		
		
		
		dcc.Graph(
        id='pie',
        figure=generate_pie(713)
    )
		
		
		
		
])
, color = 'light')


#
#@app.callback(
#    Output("choropleth", "figure"),
#    [
#        Input("dropdown-select", "value"),
#      
#    ],
#)
#def update_choro(dd_select):
#    # Update choropleth when dropdown or date-picker change
#    if dd_select is None:
#        dd_select = "POVERTY_RATE"
#
#    return generate_dest_choro(dd_select)


cards5 = dbc.Row(dbc.Col([html.H1(html.B("How Does Your County Compare? Comparing Counties across the US through Census Data"),style = {"font-size":"30px","top-margin":"10px", "color":"#333333", "text-align":"center"}),html.H3("Data from the 2018 American Community 5-year Survey",style = {"font-size":"20px","top-margin":"10px", "color":"#333333", "text-align":"center"}) ]), className = "mb-3", style = {"background-color":"#407D72","padding":"30px" })
cards4 = dbc.Row([dbc.Col(tenth_card, width=12,style={"height": "100%"})], className = "mb-3")
cards1 = dbc.Row([dbc.Col(first_card, width=8, style={"height": "100%"} ), dbc.Col(second_card, width=4,style={"height": "100%"})],className = "mb-3")
cards2 = dbc.Row([dbc.Col(third_card, width=2), dbc.Col(fourth_card,width = 2),
				  dbc.Col(fifth_card, width = 2), dbc.Col(sixth_card, width=6)], className = 'mb-3')
cards3 = dbc.Row([dbc.Col(seventh_card, width = 4),dbc.Col(eighth_card, width= 4,style={"height": "100%"}),dbc.Col(ninth_card, width= 4)], className = 'mb-3')

app.layout =dbc.Container( 
	
	
	children =

  [cards5, cards4, cards1, cards2, cards3] ,id = "content", className = "h-100", style = {"padding":"20px", "margin":"5px" }, fluid = True)





@app.callback(
    Output("main-map", "figure"),
    [Input("dropdown1", "value"), Input("scatter", "clickData")],
)

def update_choro(dd_select, scatterclick):
	
	
	if scatterclick is not None:
		value = []
		pointnumbers = []
		for point in scatterclick["points"]:
			value.append(point["text"])
			pointnumbers.append(point["pointNumber"])
			
			
			return generate_choro(dd_select, [pointnumbers[0]])
	
	
	return generate_choro(dd_select, None)




@app.callback(
	Output("scatter", "figure"),
	[Input("dropdown2", "value"),Input("dropdown1", "value"),Input("main-map", "clickData")  ]
)

def update_scatter(dd_select_x,dd_select_y, choroclick):
	
	if dd_select_y is None:
		dd_select_y = "UNEMPL_RATE"
	if dd_select_x is None:
		dd_select_x = "POVERTY_RATE"
	if choroclick is not None:
		value = []
		for point in choroclick["points"]:
			value.append(point["pointNumber"])
			print(value[0])
			return generate_scatter(dd_select_x,dd_select_y,value[0])
	else:
		return generate_scatter(dd_select_x, dd_select_y,713)
	
	
@app.callback(
	Output("county_text1", "children"),
	[Input("main-map", "clickData")]

)
def update_rent_text(choro_click):
		if choro_click is not None:
			value= []
			for point in choro_click["points"]:
			
				value.append(point["pointNumber"])
				
				return df_2.iloc[value[0]]["COUNTYNAME"]
	
		else:
	
				return "Dane County"
	
	
@app.callback(
	Output("rent_text", "children"),
	[Input("main-map", "clickData")]
)
def update_rent(choro_click):
		if choro_click is not None:
			value= []
			for point in choro_click["points"]:
			
				value.append(point["pointNumber"])
				rent = df_2.iloc[value[0]]["MEDIAN_RENT"]
			
				return "$" + str(rent)
	
		else:
			rent = df_2.iloc[713]["MEDIAN_RENT"]
			print(rent)
			return "$" + str(rent)
	

	
	
@app.callback(
	Output("box1", "figure"),
	[ Input("main-map", "clickData")]
)

def update_box1( choroclick):
	

	if choroclick is not None:
		value = []
		for point in choroclick["points"]:
			value.append(point["pointNumber"])
			return generate_box1(value[0])
	else:
		return generate_box1(713)
	
	
	
	
@app.callback(
	Output("county_text2", "children"),
	[Input("main-map", "clickData")]

)
def update_house_text(choro_click):
	
		if choro_click is not None:
			value= []
			for point in choro_click["points"]:
			
				value.append(point["pointNumber"])
				
				return df_2.iloc[value[0]]["COUNTYNAME"]
	
		else:
	
				return "Dane County"
	
	

@app.callback(
	Output("house_price_text", "children"),
	[Input("main-map", "clickData")]
)
def update_house_price(choro_click):
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			house_price = df_2.iloc[value[0]]["MEDIAN_HOUSEHOLD_VALUE"]

			return "$" + str(house_price)

	else:
		house_price = df_2.iloc[713]["MEDIAN_HOUSEHOLD_VALUE"]
		
		return "$" + str(house_price)

	
	
	

		
	
	
@app.callback(
	Output("box2", "figure"),
	[ Input("main-map", "clickData")]
)

def update_box2( choroclick):
	

	if choroclick is not None:
		value = []
		for point in choroclick["points"]:
			value.append(point["pointNumber"])
			return generate_box2(value[0])
	else:
		return generate_box2(713)
	
	

	
@app.callback(
	Output("county_text3", "children"),
	[Input("main-map", "clickData")]

)
def update_commute_text(choro_click):
		if choro_click is not None:
			value= []
			for point in choro_click["points"]:
			
				value.append(point["pointNumber"])
				
				return df_2.iloc[value[0]]["COUNTYNAME"]
	
		else:
	
				return "Dane County"
	
	
	

@app.callback(
	Output("commute_text", "children"),
	[Input("main-map", "clickData")]
)
def update_commute(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			commute = round(float(df_2.iloc[value[0]]["MEAN_TIME_TO_WORK_MIN"]))
			
			return str(commute)

	else:
		commute = round(float(df_2.iloc[713]["MEAN_TIME_TO_WORK_MIN"]))
		
		return  str(commute)

	

		
	
	
@app.callback(
	Output("box3", "figure"),
	[ Input("main-map", "clickData")]
)

def update_box3(choroclick):
	

	if choroclick is not None:
		value = []
		for point in choroclick["points"]:
			value.append(point["pointNumber"])
			return generate_box3(value[0])
	else:
		return generate_box3(713)
	
	
@app.callback(
	Output("inc", "children"),
	[Input("main-map", "clickData")]

)
def update_dist_text(choro_click):
		if choro_click is not None:
			value= []
			for point in choro_click["points"]:
			
				value.append(point["pointNumber"])
				
				return "Income Distribution for " + df_2.iloc[value[0]]["COUNTYNAME"]
	
		else:
	
				return "Income Distribution for Dane County"
	
	
	

@app.callback(
	Output("inc_text", "children"),
	[Input("main-map", "clickData")]
)
def update_inc(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			inc = round(float(df_2.iloc[value[0]]["MEDIAN_INCOME_DOLLARS"]))
			
			return '$' + str(inc)

	else:
		inc = round(float(df_2.iloc[713]["MEDIAN_INCOME_DOLLARS"]))
		
		return  '$' + str(inc)

	
	
@app.callback(	
	Output('distribution', 'figure'),
	[Input('main-map', "clickData")]
)
def update_dist(choroclick)	:
	if choroclick is not None:
		value= []
		for point in choroclick["points"]:

			value.append(point["pointNumber"])

		return generate_dist(value[0])
		#county = "Abbeville County"
	else:
		
		return generate_dist(713)
	
	

@app.callback(
	Output("education", "children"),
	[Input("main-map", "clickData")]
)
def update_education_text(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			county = df_2.iloc[value[0]]["COUNTYNAME"]
			state =  df_2.iloc[value[0]]["state"]
			return "How educated is " + county + ', ' + state

	else:
		
		return  "How educated is Dane County, Wisconsin?"

@app.callback(
	Output("occup", "children"),
	[Input("main-map", "clickData")]
)
def update_occup_text(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			county = df_2.iloc[value[0]]["COUNTYNAME"]
			state =  df_2.iloc[value[0]]["state"]
			return "Comparing Occupations for " + county + ', ' + state

	else:
		
		return  "Comparing Occupations for Dane County, Wisconsin"
	
	
@app.callback(
	Output("nativ", "children"),
	[Input("main-map", "clickData")]
)
def update_occup_text(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:

			value.append(point["pointNumber"])
			county = df_2.iloc[value[0]]["COUNTYNAME"]
			state =  df_2.iloc[value[0]]["state"]
			return "How many people have immigrated to " + county + ', ' + state

	else:
		
		return  "How many people have immigrated to Dane County, Wisconsin?"

	
@app.callback(
Output('treemap', 'figure'),
[Input('main-map', "clickData")]
)
def update_treemap(choroclick):
	
	if choroclick is not None:
		value= []
		for point in choroclick["points"]:
			
			value.append(point["pointNumber"])
		
		return generate_treemap(value[0])
		#county = "Abbeville County"
	else:
		
		return generate_treemap(713)


	
@app.callback(
Output('bar', "figure"),
[Input('main-map', "clickData")]
)	
def update_bar(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:
			
			value.append(point["pointNumber"])
		
		return generate_bar(value[0])
		#county = "Abbeville County"
	else:
		
		return generate_bar(713)

@app.callback(
Output("pie", "figure"),
[Input('main-map', "clickData")]

	
)

def update_pie(choro_click):
	
	if choro_click is not None:
		value= []
		for point in choro_click["points"]:
			
			value.append(point["pointNumber"])
		
		return generate_pie(value[0])
		#county = "Abbeville County"
	else:
		
		return generate_pie(713)

	
	
#def update_label(n1, n2):
#    # use a dictionary to map ids back to the desired label
#    # makes more sense when there are lots of possible labels
#    id_lookup = {"item-1": "Item 1", "item-2": "Item 2"}
#
#    ctx = dash.callback_context
#
#    if (n1 is None and n2 is None) or not ctx.triggered:
#        # if neither button has been clicked, return "Not selected"
#        return "Not selected"
#
#    # this gets the id of the button that triggered the callback
#    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
#    return id_lookup[button_id]
#
#


if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)
