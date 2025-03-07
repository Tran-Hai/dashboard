import plotly.express as px
import plotly.graph_objects as go


def create_pie_chart(df, column_name, title, mapping):
    grouped_df = df.groupby(by=[column_name], as_index=False)['Group'].count()

    custom_label = grouped_df[column_name].map(mapping)

    grouped_df['custom label'] = custom_label

    total_value = grouped_df['Group'].sum()

    fig = go.Figure(data = [go.Pie(
        labels=grouped_df['custom label'],
        values=grouped_df['Group'],
        textposition='inside',
        hole=.33,
        textinfo='percent',
        hoverinfo='label+value',
        direction='clockwise',
        marker=dict(
            colors=px.colors.sequential.Plasma
        )
    )])
    fig.update_layout(
        title = title,
        showlegend=False,
        annotations = [
            dict(
                x=1.0,
                y=1.05,
                xref = 'paper',
                yref = 'paper',
                text=f'Total: {total_value}',
                showarrow=False,
                font=dict(size=19),
                align='left',
            )
        ]
    )
    return fig


def create_bar_chart(df, column_name):
    @grouped_df = df.groupby(by=[column_name], as_index=False)['Line'].count()
    grouped_df = df[column_name].value_count()

    grouped_df = grouped_df.sort_values(by='Line', ascending=True)

    fig = px.bar(grouped_df, x=grouped.index, y=grouped.value, template='seaborn')

    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    fig.update_xaxes(title = '')
    fig.update_yaxes(title = '')

    fig.update_traces(hovertemplate='%{x}<br>%{y}')

    return fig
