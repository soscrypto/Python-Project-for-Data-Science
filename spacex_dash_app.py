# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
data=spacex_df
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(
                                    id='site-dropdown',
                                    options=[
                                        {'label':'All Sites', 'value':'All'},
                                        {'label':'CCAFS LC-40', 'value':'CCAFS LC-40'},
                                        {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'},
                                        {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
                                        {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'}
                                    ],
                                    value='ALL',
                                    placeholder='Select a Launch Site here',
                                    searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',min=min_payload,max=max_payload,step=1000,value=[min_payload,max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart'))
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
        names='Launch Site', 
        title='Launch data for all sites')
        return fig
    else:
        if entered_site == 'CCAFS LC-40':
            data1=filtered_df[filtered_df['Launch Site']=='CCAFS LC-40']   
            class_counts = data1['class'].value_counts().reset_index()
            class_counts.columns = ['class', 'Count']
            fig = px.pie(class_counts, values='Count', names='class', title='Launch data for '+entered_site)
            return fig
        elif entered_site == 'CCAFS SLC-40':
            data2=filtered_df[filtered_df['Launch Site']=='CCAFS SLC-40']    
            class_counts = data2['class'].value_counts().reset_index()
            class_counts.columns = ['class', 'Count']
            fig = px.pie(class_counts, values='Count', names='class', title='Launch data for '+entered_site)
            return fig
        elif entered_site == 'KSC LC-39A':
            data3=filtered_df[filtered_df['Launch Site']=='KSC LC-39A']  
            class_counts = data3['class'].value_counts().reset_index()
            class_counts.columns = ['class', 'Count']
            fig = px.pie(class_counts, values='Count', names='class', title='Launch data for '+entered_site)
            return fig
        elif entered_site == 'VAFB SLC-4E':
            data4=filtered_df[filtered_df['Launch Site']=='VAFB SLC-4E']  
            class_counts = data4['class'].value_counts().reset_index()
            class_counts.columns = ['class', 'Count']
            fig = px.pie(class_counts, values='Count', names='class', title='Launch data for '+entered_site)
            return fig            
        # return the outcomes piechart for a selected site


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
def get_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
        fig = px.scatter(filtered_df, x='class', y='Payload Mass (kg)', color='Booster Version Category')
        fig.update_layout(title_text='Launch data for all sites')
        return fig
    else:
        if entered_site == 'CCAFS LC-40':
            filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
            data1 = filtered_df[filtered_df['Launch Site'] == 'CCAFS LC-40']
            fig = px.scatter(data1, x='class', y='Payload Mass (kg)',color='Booster Version Category')
            fig.update_layout(title_text='Launch data for CCAFS LC-40')
            return fig
        elif entered_site == 'CCAFS SLC-40':
            filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
            data2 = filtered_df[filtered_df['Launch Site'] == 'CCAFS SLC-40']
            fig = px.scatter(data2, x='class', y='Payload Mass (kg)',color='Booster Version Category')
            fig.update_layout(title_text='Launch data for CCAFS SLC-40')
            return fig
        elif entered_site == 'KSC LC-39A':
            filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
            data3 = filtered_df[filtered_df['Launch Site'] == 'KSC LC-39A']
            fig = px.scatter(data3, x='class', y='Payload Mass (kg)',color='Booster Version Category')
            fig.update_layout(title_text='Launch data for KSC LC-39A')
            return fig
        elif entered_site == 'VAFB SLC-4E':
            filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
            data4 = filtered_df[filtered_df['Launch Site'] == 'VAFB SLC-4E']
            fig = px.scatter(data4, x='class', y='Payload Mass (kg)',color='Booster Version Category')
            fig.update_layout(title_text='Launch data for VAFB SLC-4E')
            return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
