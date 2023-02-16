def header_adder(df):
    d = df['Position'].to_list()
    final_value_list = []
    for i in d:
        value_list = list(i.split(","))
        final_value_list.append(value_list[0])
    df['Main position'] = final_value_list
    df.rename(columns = {'Accurate passes, %':'Pass accuracy (%)', 'Accurate forward passes, %':'Forward pass accuracy (%)'},inplace = True)
    df['% of passes not backwards'] = 100 - (df['Back passes per 90'] / df['Passes per 90'] * 100)
    df['% of passes forward'] = (df['Forward passes per 90'] / df['Passes per 90']) * 100
    df['Progressive passes (%)'] = (df['Progressive passes per 90'] / df['Passes per 90']) * 100
    df['Long passes (%)'] = (df['Long passes per 90'] / df['Passes per 90']) * 100
    df['Non-cross passes to box'] = df['Passes to penalty area per 90'] - df['Crosses per 90']
    df['Dribbles completed per 90'] = df['Dribbles per 90'] * (df['Successful dribbles, %'] / 100)
    df['Tackles + interceptions (pAdj)'] = df['PAdj Interceptions'] + df['PAdj Sliding tackles']
    df['xG/Shot'] = df['xG'] / df['Shots']
    df['Aerial wins'] = df['Aerial duels per 90'] * (df['Aerial duels won, %'] / 100)
    df['Crosses completed per 90'] = df['Crosses per 90'] * (df['Accurate crosses, %'] / 100)
    return df