import pandas as pd
import matplotlib.pyplot as plt

def main():
    excel_file = 'movies.xls'
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
    print(movies.shape)

    # Read excel from all of sheets
    xlsx = pd.ExcelFile(excel_file)
    movies_sheets = []
    for sheet in xlsx.sheet_names:
        movies_sheets.append(xlsx.parse(sheet))
        movies = pd.concat(movies_sheets)
    print(movies.shape)
    print(movies.tail())
    sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)
    print("----Sort----")
    print(sorted_by_gross["Gross Earnings"].head(10))

    # sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    # plt.show()
    #
    # movies['IMDB Score'].plot(kind="hist")
    # plt.show()

    print("----Describe----\n", movies.describe())
    print("\nmeans = ",movies["Gross Earnings"].mean())

    # Skip 5 first rows
    movies_skip_rows = pd.read_excel("movies-no-header-skip-rows.xls", header=None, skiprows=5);
    print("\n----Skiped Row----", movies_skip_rows.head(5))
    # movies_skip_rows.columns = ['Title', 'Year', 'Genres', 'Language', 'Country', 'Content Rating', 'Duration',
    #                             'Aspect Ratio', 'Budget', 'Gross Earnings', 'Director', 'Actor 1', 'Actor 2', 'Actor 3',
    #                             'Facebook Likes - Director', 'Facebook Likes - Actor 1', 'Facebook Likes - Actor 2',
    #                             'Facebook Likes - Actor 3', 'Facebook Likes - cast Total', 'Facebook likes - Movie',
    #                             'Facenumber in posters', 'User Votes', 'Reviews by Users', 'Reviews by Crtiics',
    #                             'IMDB Score']
    # print(movies_skip_rows.head(5))

    # Get only 6 first rows
    movies_subset_columns = pd.read_excel(excel_file, nrows=6)
    print(movies_subset_columns.head())

    # movies["Net Earnings"] = movies["Gross Earnings"] - movies["Budget"]
    # sorted_movies = movies.sort_values(['Net Earnings'], ascending=False)
    # sorted_movies.head(10)['Net Earnings'].plot.barh()
    # plt.show()

    # Caculate mean gross earning each year then plot pivot
    # movies_subset = movies[['Year', 'Gross Earnings']]
    # earnings_by_year = movies_subset.pivot_table(index=['Year'])
    # earnings_by_year.plot()
    # plt.show()
    #
    # movies_subset = movies[['Country', 'Language', 'Gross Earnings']]
    # earning_by_co_language = movies_subset.pivot_table(index=['Country', 'Language'])
    # earning_by_co_language.head(20).plot(kind='bar', figsize=(20, 8))
    # plt.show()

    # Exporting the results to Excel
    movies.to_excel('output.xlsx')
    writer = pd.ExcelWriter('output1.xlsx', engine='xlsxwriter')
    movies.to_excel(writer, index=False, sheet_name='report')

    writer.save()


if __name__ == '__main__':
    main()